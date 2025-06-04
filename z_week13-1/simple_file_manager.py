# 시스템 관련 표준 모듈
import sys
import os

# PySide6에서 필요한 GUI 관련 클래스들 가져오기
from PySide6.QtWidgets import (
    QApplication,         # Qt 애플리케이션 객체
    QMainWindow,          # 메인 윈도우 프레임
    QTreeView,            # 트리 형태의 뷰 (파일 탐색용)
    QFileSystemModel,     # 파일 시스템을 모델로 사용 (MVC의 M)
    QLabel,               # 텍스트 표시용 위젯
    QPushButton,          # 클릭 가능한 버튼
    QMessageBox,          # 팝업 메시지 박스 (경고/정보)
    QWidget,              # 일반적인 위젯 (컨테이너용)
    QVBoxLayout,          # 수직 방향 레이아웃 관리자
    QHBoxLayout,          # 수평 방향 레이아웃 관리자
    QInputDialog,         # 입력 다이알로그
    QStatusBar,           # 하단 상태 표시줄
)

# 파일 경로 및 URL 관련 클래스
from PySide6.QtCore import (
    QDir, 
    QUrl, 
    Qt,
)    

# 폰트, URL 열기 기능 포함
from PySide6.QtGui import (
    QFont, 
    QDesktopServices,
)

# QMainWindow 기반의 파일 탐색기 메인 클래스 정의
class FileExplorerMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()  # 부모 생성자 호출
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("파일 탐색기 (QMainWindow 기반)")  # 윈도우 제목 설정
        self.setGeometry(100, 100, 1000, 700)  # 윈도우 위치(x, y) 및 크기(width, height)
        self.set_main_wnd()
        self.show()

    def set_main_wnd(self):
        # 중앙 위젯과 레이아웃 설정
        central_widget = QWidget()                # 중앙 콘텐츠용 위젯 생성
        self.setCentralWidget(central_widget)     # QMainWindow의 중앙 위젯으로 설정
        
        # -----------------------
        # central_widget의 layout manager.
        main_layout = QVBoxLayout(central_widget) # 수직 박스 레이아웃을 중앙 위젯에 설정

        # -----------------------
        # 파일 시스템 모델 생성 및 설정
        self.model = QFileSystemModel()                # 실제 파일 시스템을 반영하는 모델 생성
        self.model.setRootPath(QDir.rootPath())        # 모델의 루트 경로를 파일 시스템 전체로 설정
        self.model.setFilter(
            QDir.AllDirs | QDir.NoDotAndDotDot | QDir.Files
        )  # '.' 및 '..' 제외, 디렉토리 + 파일 표시
        self.model.setNameFilters(
            ["*.txt", "*.py", "*.md", "*.png", "*.jpg",]
        )  # 필터된 확장자만 표시
        self.model.setNameFilterDisables(False)        # 필터링을 활성화하여 필터된 파일만 보여줌

        # -----------------------
        # QTreeView 생성 및 설정
        self.tree = QTreeView()
        self.tree.setModel(self.model)    # 위에서 만든 파일 시스템 모델과 연결
        self.tree.setRootIndex(
            self.model.index(QDir.homePath())
        ) # 홈 디렉토리를 기본 표시 위치로 설정

        self.tree.setSortingEnabled(True)  # 정렬 허용
        self.tree.setAnimated(True)        # 트리 확장 시 애니메이션 적용
        self.tree.setColumnWidth(0, 300)   # 첫 번째 열(파일/폴더 이름)의 너비 설정

        # -----------------------
        # Signals and Slots

        # 더블 클릭 시 파일 열기 함수 연결
        self.tree.doubleClicked.connect(
            self.open_file_on_double_click
        )

        # 선택 변경 시 하단 라벨 갱신 함수 연결
        # selectionChanged 시그널은 2개의 QItemSelection객체를 인자로 넘김:
        # - selected : 새롭게 선택된 항목들의 집합.
        # - deselected : 이전 선택에서 해제된 항목들의 집합
        self.tree.selectionModel().selectionChanged.connect(
            self.update_path_label
        )

        # 현재 선택된 경로를 표시하는 라벨 생성
        self.path_label = QLabel("선택된 파일/폴더 경로:")
        self.path_label.setFont(QFont("Arial", 11))  # 라벨 폰트 설정

        # 버튼 레이아웃 및 버튼 생성
        button_layout = QHBoxLayout()

        self.btn_add_folder = QPushButton("새 폴더 만들기")
        self.btn_add_folder.clicked.connect(self.create_new_folder)  # 클릭 시 새 폴더 생성 함수 실행
        button_layout.addWidget(self.btn_add_folder)

        self.btn_add_file   = QPushButton("빈 파일 만들기")
        self.btn_add_file.clicked.connect(self.create_new_file)      # 클릭 시 빈 파일 생성 함수 실행
        button_layout.addWidget(self.btn_add_file)

        self.btn_rename   = QPushButton("이름 바꾸기")
        self.btn_rename.clicked.connect(self.rename_item)      # 클릭 시 이름 변경 함수 실행
        button_layout.addWidget(self.btn_rename)

        self.btn_delete   = QPushButton("삭제")
        self.btn_delete.clicked.connect(self.delete_item)      # 클릭 시 삭제 함수 실행
        button_layout.addWidget(self.btn_delete)

        # 메인 레이아웃에 트리 뷰, 라벨, 버튼 레이아웃 추가
        main_layout.addWidget(self.tree)
        main_layout.addWidget(self.path_label)
        main_layout.addLayout(button_layout)

        # 상태 바 설정
        # self.status_bar = QStatusBar()
        # self.setStatusBar(self.status_bar)  # QMainWindow 하단에 상태바 부착
        self.status_bar = self.statusBar()
        self.status_bar.showMessage("파일 탐색기 실행 중")  # 초기 메시지

    def get_selected_path(self):
        """
        현재 트리뷰에서 선택된 항목의 전체 경로 반환
        """
        index = self.tree.currentIndex()  # 현재 선택된 QModelIndex 객체
        if not index.isValid():
            return None
        return self.model.filePath(index)

    def get_selected_directory(self):
        """
        현재 트리뷰에서 선택된 항목의 디렉터리 경로를 반환
        - 폴더 선택 시: 해당 폴더 경로 반환
        - 파일 선택 시: 해당 파일이 포함된 상위 폴더 경로 반환
        """
        path = self.get_selected_path()
        if path is None:
            return None
        return path if os.path.isdir(path) else os.path.dirname(path)

    def create_new_folder(self):
        """
        현재 선택된 폴더 안에 새 폴더를 생성하는 함수
        - 중복된 이름이 있을 경우 NewFolder_1, NewFolder_2 등의 형식으로 생성
        """
        base_path = self.get_selected_directory()
        if not base_path:
            QMessageBox.warning(self, "경고", "디렉터리를 먼저 선택하세요.")
            return

        name, ok = QInputDialog.getText(
                        self, "새 폴더 이름", 
                        "폴더 이름을 입력하세요:", 
                        text="NewFolder",
                    )
        if not ok or not name.strip():
            return
        name = name.strip()
        new_path = os.path.join(base_path, name)

        # # 중복된 이름이 존재하면 번호 증가
        # while os.path.exists(new_path):
        #     new_path = os.path.join(base_path, f"{name}_{counter}")
        #     counter += 1
        if os.path.exists(new_path):
            QMessageBox.warning(
                self, "경고", 
                "같은 이름의 폴더가 이미 존재합니다.",
            )
            return

        try:
            os.mkdir(new_path)  # 새 폴더 생성
        except Exception as e:
            QMessageBox.critical(
                self, "오류", 
                f"폴더 생성 실패:\n{e}",
            )
        else:
            # 트리 뷰 강제 갱신
            self.tree.setRootIndex(self.tree.rootIndex())
            parent_index = self.model.index(base_path)
            new_index = self.model.index(new_path)
            self.tree.expand(parent_index)
            self.tree.setCurrentIndex(new_index)
            self.tree.scrollTo(new_index)

            self.status_bar.showMessage(f"폴더 생성됨: {new_path}", 3000)  # 3초간 상태 메시지 표시

    def create_new_file(self):
        """
        현재 선택된 폴더 안에 새 텍스트 파일을 생성
        - 중복된 경우 NewFile_1.txt, NewFile_2.txt 등으로 생성
        """
        base_path = self.get_selected_directory()
        if not base_path:
            QMessageBox.warning(self, "경고", "디렉터리를 먼저 선택하세요.")
            return

        name, ok = QInputDialog.getText(
            self, "새 파일이름",
            "파일 이름을 입력하세요.",
            text="NewFile.txt",
            )
        if not ok or not name.strip():
            return # 취소하거나 빈 이름이면 그냥 반환.
        counter = 1
        name = name.strip()
        new_file_path = os.path.join(base_path, name)

        # 중복된 파일이 있다면 번호를 증가시키며 파일명 수정
        while os.path.exists(new_file_path):
            new_file_path = os.path.join(base_path, f"NewFile_{counter}.txt")
            counter += 1

        try:
            with open(new_file_path, "w", encoding="utf-8") as f:
                pass  # 내용 없는 빈 파일 생성
        except Exception as e:
            QMessageBox.critical(self, "오류", f"파일 생성 실패:\n{e}")
        else:
            parent_index = self.model.index(base_path)
            self.tree.expand(parent_index) # 디렉토리 펼치기.
            self.tree.scrollTo(parent_index) # 자동 스크롤.
            self.status_bar.showMessage(f"파일 생성됨: {new_file_path}", 3000)

    def rename_item(self):
        """
        선택된 item 의 이름 변경.
        """
        path = self.get_selected_path()
        if not path:
            QMessageBox.warning(
                self, "Warning",
                "먼저 item을 선택하세요.",
            )
            return
        new_name, ok = QInputDialog.getText(
            self, "rename",
            "새 이름:",
            text=os.path.basename(path),
        )
        if ok and new_name:
            new_path = os.path.join(
                os.path.dirname(path),
                new_name,
            )
            try:
                os.rename(path, new_path)
            except Exception as e:
                QMessageBox.critical(
                    self, "Critical Error",
                    f"이름 변경 실패:\n{e}"
                )
            else:
                self.status_bar.showMessage(f"이름 변경됨: {new_path}", 3000)

    def delete_item(self):
        """선택된 파일 또는 폴더 삭제"""
        path = self.get_selected_path()
        if not path:
            QMessageBox.warning(self, "경고", "삭제할 항목을 선택하세요.")
            return

        reply = QMessageBox.question(self, "삭제 확인", f"정말 삭제하시겠습니까?\n{path}",
                                     QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            try:
                if os.path.isdir(path):
                    os.rmdir(path)  # 비어있을 경우만 삭제됨
                    # shutil.rmtree(path) # import shutil 필요.
                else:
                    os.remove(path)
            except Exception as e:
                QMessageBox.critical(self, "오류", f"삭제 실패:\n{e}")
            else:
                self.status_bar.showMessage(f"삭제됨: {path}", 3000)

    def update_path_label(self, selected, _):
        """
        선택된 항목이 변경될 때 라벨을 갱신하여 선택 경로를 표시

        - selected: QItemSelection
        - deselected: QItemSelection
        """
        if indexes := selected.indexes():  # 선택된 인덱스가 있을 경우
            path = self.model.filePath(indexes[0])
            self.path_label.setText(f"선택된 경로: {path}")

    def open_file_on_double_click(self, index):
        """
        파일을 더블 클릭했을 때 시스템 기본 프로그램으로 열기
        - 폴더일 경우 아무 작업도 하지 않음
        """
        if not index.isValid():
            return

        file_path = self.model.filePath(index)

        # 파일일 경우에만 열기
        if not self.model.isDir(index) and os.path.exists(file_path):
            QDesktopServices.openUrl(QUrl.fromLocalFile(file_path))  # 시스템 기본 앱으로 열기


# 프로그램의 진입점: 애플리케이션 실행
if __name__ == "__main__":
    app = QApplication(sys.argv)         # QApplication 객체 생성
    wnd = FileExplorerMainWindow()    # 메인 윈도우 인스턴스 생성
    sys.exit(app.exec())                 # 이벤트 루프 실행 및 종료 처리