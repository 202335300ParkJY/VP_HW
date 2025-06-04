import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QTreeView, QVBoxLayout,
    QHBoxLayout, QPushButton, QInputDialog, QMessageBox
)
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import Qt
from datetime import datetime

# ==================================================================

# 가상 파일 관리자를 위한 메인 윈도우 클래스 정의
class MW(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()          # 윈도우 타이틀 및 크기 설정
        self.set_main_window() # UI 요소 및 이벤트 핸들러 구성

    def init_ui(self):
        """메인 윈도우 설정"""
        self.setWindowTitle("Virtual File Manger")     # 윈도우 상단 제목
        self.setGeometry(100, 100, 800, 600)           # 위치(x, y), 크기(width, height)
        self.show()                                    # 윈도우 표시

    def set_main_window(self):
        """트리 뷰와 버튼 UI 구성"""

        # 중앙 위젯과 레이아웃 생성
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout()    # 메인 수직 레이아웃
        button_layout = QHBoxLayout()  # 상단 버튼 가로 레이아웃

        # 버튼들 생성
        self.add_folder_button = QPushButton("폴더 추가")
        self.add_file_button = QPushButton("파일 추가")
        self.remove_button = QPushButton("삭제")
        self.rename_button = QPushButton("이름 변경")
        self.expand_button = QPushButton("모두 펼치기")
        self.collapse_button = QPushButton("모두 접기")

        # 버튼 클릭 시 동작할 슬롯 연결
        self.add_folder_button.clicked.connect(self.add_folder)
        self.add_file_button.clicked.connect(self.add_file)
        self.remove_button.clicked.connect(self.remove_item)
        self.rename_button.clicked.connect(self.rename_item)
        self.expand_button.clicked.connect(self.tree_view_expand_all)
        self.collapse_button.clicked.connect(self.tree_view_collapse_all)

        # 버튼들을 버튼 레이아웃에 추가
        button_layout.addWidget(self.add_folder_button)
        button_layout.addWidget(self.add_file_button)
        button_layout.addWidget(self.remove_button)
        button_layout.addWidget(self.rename_button)
        button_layout.addStretch()  # 오른쪽 정렬용 stretch
        button_layout.addWidget(self.expand_button)
        button_layout.addWidget(self.collapse_button)

        # QTreeView 생성 및 설정
        self.tree_view = QTreeView()
        self.tree_view.setAlternatingRowColors(True)               # 줄마다 색상 교차
        self.tree_view.setSelectionBehavior(QTreeView.SelectRows)  # 행 단위로 선택. 행단위로 처리.
        # self.tree_view.setSelectionBehavior(QTreeView.SelectItems)  #  item 단위로 선택. 하지만 TreeView에선 의미 없음.
        # QTreeView에서 트리 구조상의 드래그앤드롭 이동은 항상 0번 열의 아이템을 기준으로 처리.
        # QTreeView에서는 0번 열의 Item만이 자식이나 부모가 될 수 있음: 
        # 즉, QStandardItemModel은 각 열(column)을 독립적인 계층 구조로 보지 않음.
        # 그래서 드래그앤드롭 대상이 0번 열의 아이템이 아닌 경우,
        # 해당 아이템은 자식(appendRow)이나 부모가 될 수 없고, 트리 내의 위치를 옮길 수도 없음

        self.tree_view.setSelectionMode(QTreeView.ExtendedSelection) # 클릭 등의 선택 모드
        self.tree_view.setAnimated(True)                           # 확장/축소 애니메이션
        self.tree_view.setSortingEnabled(True)                     # 정렬 기능

        self.tree_view.setDragDropMode(QTreeView.InternalMove) # 내부 항목 드래그 지원

        # 트리 뷰에 연결할 모델 생성 및 헤더 설정
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(['이름', '타입', '크기', '수정일'])
        self.tree_view.setModel(self.model)

        # 컬럼 너비 지정
        self.tree_view.setColumnWidth(0, 250)  # 이름
        self.tree_view.setColumnWidth(1, 100)  # 타입
        self.tree_view.setColumnWidth(2, 100)  # 크기
        self.tree_view.setColumnWidth(3, 150)  # 수정일

        # 선택이 변경될 때 버튼 상태 업데이트
        self.tree_view.selectionModel().selectionChanged.connect(
            self.update_button_states
        )

        # 초기 샘플 데이터 삽입
        self.populate_sample_data()

        # 전체 레이아웃 정리
        main_layout.addLayout(button_layout)
        main_layout.addWidget(self.tree_view)
        central_widget.setLayout(main_layout)

        # 버튼 활성화 여부 초기화
        self.update_button_states()

    def make_item(self, text):
        """QStandardItem 객체를 생성하는 헬퍼 메서드"""
        return QStandardItem(text)

    def create_folder_item(self, name, type_name):
        """폴더용 4열 항목 리스트 생성 (이름, 타입, 크기, 수정일)"""
        name_item = self.make_item(name)

        name_item.setDropEnabled(True)  # Drop을 허용 (폴더처럼): 
        # 사실 StandardItem은 기본이 Drag와 Drop이 가능하므로 위 라인은 주석처리해도 됨.

        type_item = self.make_item(type_name)
        size_item = self.make_item("")  # 폴더는 크기 없음
        date_item = self.make_item(datetime.now().strftime("%Y-%m-%d %H:%M"))
        return [name_item, type_item, size_item, date_item]

    def create_file_item(self, name, type_name, size):
        """파일용 4열 항목 리스트 생성"""
        name_item = self.make_item(name)
        type_item = self.make_item(type_name)
        size_item = self.make_item(size)
        date_item = self.make_item(datetime.now().strftime("%Y-%m-%d %H:%M"))
        return [name_item, type_item, size_item, date_item]

    def get_selected_item(self):
        """현재 선택된 트리 항목의 첫 열 항목 반환"""
        index = self.tree_view.currentIndex()
        if index.isValid():
            return self.model.itemFromIndex(index.siblingAtColumn(0))
        return None

    def populate_sample_data(self):
        """샘플 파일/폴더 구조를 트리에 추가"""
        try:
            # Documents 폴더 생성 및 파일 추가
            docs = self.create_folder_item("Documents", "폴더")
            docs[0].appendRow(
                self.create_file_item("report.pdf", "PDF 파일", "2.5 MB")
            )
            docs[0].appendRow(
                self.create_file_item("presentation.pptx", "PPT 파일", "5.1 MB")
            )
            self.model.appendRow(docs)

            # Pictures 폴더 > Vacation 폴더 > 사진 파일들
            pics = self.create_folder_item("Pictures", "폴더")
            vacation = self.create_folder_item("Vacation", "폴더")
            vacation[0].appendRow(
                self.create_file_item("beach.jpg", "JPEG 이미지", "3.2 MB")
            )
            vacation[0].appendRow(
                self.create_file_item("sunset.jpg", "JPEG 이미지", "2.8 MB")
            )
            pics[0].appendRow(vacation)
            self.model.appendRow(pics)

            # Downloads 폴더 생성
            downloads = self.create_folder_item("Downloads", "폴더")
            downloads[0].appendRow(
                self.create_file_item("setup.exe", "실행 파일", "45.2 MB")
            )
            self.model.appendRow(downloads)
        except Exception as e:
            QMessageBox.critical(self, "오류", f"샘플 데이터를 불러오는 중 오류 발생: {e}")

    def add_folder(self):
        """새 폴더 추가 다이얼로그"""
        folder_name, ok = QInputDialog.getText(
                            self, "폴더 추가", 
                            "폴더 이름:", text="새 폴더",
                          )
        if ok and folder_name:
            try:
                folder_items = self.create_folder_item(
                                        folder_name, 
                                        "폴더",
                                    )
                parent = self.get_selected_item()
                if parent:
                    parent.appendRow(folder_items)
                    self.tree_view.expand(parent.index())
                else:
                    self.model.appendRow(folder_items)
            except Exception as e:
                QMessageBox.critical(self, "오류", f"폴더 추가 중 오류 발생: {e}")

    def add_file(self):
        """새 파일 추가 다이얼로그"""
        file_name, ok = QInputDialog.getText(
                            self, "파일 추가", 
                            "파일 이름:", text="새파일.txt",
                        )
        if ok and file_name:
            try:
                extension = file_name.split('.')[-1] if '.' in file_name else 'txt'
                file_items = self.create_file_item(
                                file_name, 
                                f"{extension.upper()} 파일", 
                                "1.0 KB",
                             )
                parent = self.get_selected_item()
                if parent:
                    parent.appendRow(file_items)
                    self.tree_view.expand(parent.index())
                else:
                    self.model.appendRow(file_items)
            except Exception as e:
                QMessageBox.critical(self, "오류", f"파일 추가 중 오류 발생: {e}")

    def remove_item(self):
        """선택된 항목 삭제"""
        item = self.get_selected_item()
        if item:
            reply = QMessageBox.question(
                self, "삭제 확인", f"'{item.text()}' 항목을 삭제하시겠습니까?",
                QMessageBox.Yes | QMessageBox.No
            )
            if reply == QMessageBox.Yes:
                # 부모가 없으면 루트 아이템으로 간주
                parent = item.parent() or self.model.invisibleRootItem()
                parent.removeRow(item.row())
        else:
            QMessageBox.information(self, "선택 없음", "삭제할 항목을 선택하세요.")

    def rename_item(self):
        """선택된 항목의 이름 변경"""
        item = self.get_selected_item()
        if item:
            old_name = item.text()
            new_name, ok = QInputDialog.getText(self, "이름 변경", "새 이름:", text=old_name)
            if ok and new_name:
                item.setText(new_name)
                # 수정일도 현재 시각으로 갱신
                date_item = self.model.item(item.row(), 3)
                if date_item:
                    date_item.setText(datetime.now().strftime("%Y-%m-%d %H:%M"))
        else:
            QMessageBox.information(self, "선택 없음", "이름을 변경할 항목을 선택하세요.")

    def tree_view_expand_all(self):
        """모든 항목을 펼침"""
        self.tree_view.expandAll()

    def tree_view_collapse_all(self):
        """모든 항목을 접음"""
        self.tree_view.collapseAll()

    def update_button_states(self):
        """선택 상태에 따라 버튼의 활성화 여부를 조정"""
        # has_selection = self.tree_view.currentIndex().isValid()
        has_selection = self.tree_view.selectionModel().hasSelection()
        self.remove_button.setEnabled(has_selection)
        self.rename_button.setEnabled(has_selection)

# =============================================================

# 프로그램 진입점
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MW()  # 윈도우 클래스 인스턴스 생성
    sys.exit(app.exec())  # 이벤트 루프 실행