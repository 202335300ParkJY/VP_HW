import sys
import os
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QTreeView, QFileSystemModel, QLabel, QPushButton,
    QMessageBox, QWidget, QVBoxLayout, QHBoxLayout, QInputDialog, QStatusBar
)
from PySide6.QtCore import QDir, QUrl
from PySide6.QtGui import QFont, QDesktopServices

class FileExplorerMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("파일 탐색기 (QMainWindow 기반)")
        self.setGeometry(100, 100, 1000, 700)
        self.setup_ui_elements()
        self.show()

    def setup_ui_elements(self):
        """UI 요소들을 설정하는 메서드"""
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout(central_widget)

        self.setup_file_system_model()
        self.setup_tree_view()
        self.setup_path_label()
        self.setup_buttons(main_layout)

        self.status_bar = self.statusBar()
        self.status_bar.showMessage("파일 탐색기 실행 중")

    def setup_file_system_model(self):
        """파일 시스템 모델 설정"""
        self.model = QFileSystemModel()
        self.model.setRootPath(QDir.rootPath())
        self.model.setFilter(QDir.AllDirs | QDir.NoDotAndDotDot | QDir.Files)
        self.model.setNameFilters(["*.txt", "*.py", "*.md", "*.png", "*.jpg"])
        self.model.setNameFilterDisables(False)

    def setup_tree_view(self):
        """트리뷰 설정"""
        self.tree = QTreeView()
        self.tree.setModel(self.model)
        self.tree.setRootIndex(self.model.index(QDir.homePath()))
        self.tree.setSortingEnabled(True)
        self.tree.setAnimated(True)
        self.tree.setColumnWidth(0, 300)

        self.tree.doubleClicked.connect(self.open_file_on_double_click)
        self.tree.selectionModel().selectionChanged.connect(self.update_path_label)

    def setup_path_label(self):
        """경로 라벨 설정"""
        self.path_label = QLabel("선택된 파일/폴더 경로:")
        self.path_label.setFont(QFont("Arial", 11))

    def setup_buttons(self, layout):
        """버튼과 레이아웃 설정"""
        button_layout = QHBoxLayout()

        self.btn_add_folder = QPushButton("새 폴더 만들기")
        self.btn_add_folder.clicked.connect(self.create_new_folder)
        button_layout.addWidget(self.btn_add_folder)

        self.btn_add_file = QPushButton("빈 파일 만들기")
        self.btn_add_file.clicked.connect(self.create_new_file)
        button_layout.addWidget(self.btn_add_file)

        self.btn_rename = QPushButton("이름 바꾸기")
        self.btn_rename.clicked.connect(self.rename_item)
        button_layout.addWidget(self.btn_rename)

        self.btn_delete = QPushButton("삭제")
        self.btn_delete.clicked.connect(self.delete_item)
        button_layout.addWidget(self.btn_delete)

        layout.addWidget(self.tree)
        layout.addWidget(self.path_label)
        layout.addLayout(button_layout)

    def get_selected_path(self):
        """현재 선택된 파일 또는 폴더의 경로 반환"""
        index = self.tree.currentIndex()
        return self.model.filePath(index) if index.isValid() else None

    def get_selected_directory(self):
        """현재 선택된 폴더의 경로 반환"""
        path = self.get_selected_path()
        return path if os.path.isdir(path) else os.path.dirname(path) if path else None

    def create_new_folder(self):
        """새 폴더 생성"""
        base_path = self.get_selected_directory()
        if not base_path:
            QMessageBox.warning(self, "경고", "디렉터리를 먼저 선택하세요.")
            return

        name, ok = QInputDialog.getText(self, "새 폴더 이름", "폴더 이름을 입력하세요:", text="NewFolder")
        if ok and name.strip():
            new_path = os.path.join(base_path, name.strip())
            if os.path.exists(new_path):
                QMessageBox.warning(self, "경고", "같은 이름의 폴더가 이미 존재합니다.")
                return
            self.create_directory(new_path)

    def create_directory(self, new_path):
        """디렉터리 생성 후 트리 뷰 갱신"""
        try:
            os.mkdir(new_path)
        except Exception as e:
            QMessageBox.critical(self, "오류", f"폴더 생성 실패:\n{e}")
        else:
            self.refresh_tree_view(new_path)
            self.status_bar.showMessage(f"폴더 생성됨: {new_path}", 3000)

    def refresh_tree_view(self, new_path):
        """트리 뷰 갱신"""
        parent_index = self.model.index(os.path.dirname(new_path))
        new_index = self.model.index(new_path)
        self.tree.setRootIndex(self.tree.rootIndex())
        self.tree.expand(parent_index)
        self.tree.setCurrentIndex(new_index)
        self.tree.scrollTo(new_index)

    def create_new_file(self):
        """새 파일 생성"""
        base_path = self.get_selected_directory()
        if not base_path:
            QMessageBox.warning(self, "경고", "디렉터리를 먼저 선택하세요.")
            return

        name, ok = QInputDialog.getText(self, "새 파일 이름", "파일 이름을 입력하세요:", text="NewFile.txt")
        if ok and name.strip():
            new_file_path = self.get_unique_file_path(base_path, name.strip())
            self.create_file(new_file_path)

    def get_unique_file_path(self, base_path, name):
        """중복되지 않는 파일 경로 생성"""
        counter = 1
        new_file_path = os.path.join(base_path, name)
        while os.path.exists(new_file_path):
            new_file_path = os.path.join(base_path, f"NewFile_{counter}.txt")
            counter += 1
        return new_file_path

    def create_file(self, new_file_path):
        """파일 생성 후 트리 뷰 갱신"""
        try:
            with open(new_file_path, "w", encoding="utf-8"):
                pass
        except Exception as e:
            QMessageBox.critical(self, "오류", f"파일 생성 실패:\n{e}")
        else:
            self.refresh_tree_view(new_file_path)
            self.status_bar.showMessage(f"파일 생성됨: {new_file_path}", 3000)

    def rename_item(self):
        """선택된 항목의 이름 변경"""
        path = self.get_selected_path()
        if not path:
            QMessageBox.warning(self, "경고", "먼저 항목을 선택하세요.")
            return

        new_name, ok = QInputDialog.getText(self, "이름 변경", "새 이름:", text=os.path.basename(path))
        if ok and new_name:
            new_path = os.path.join(os.path.dirname(path), new_name)
            self.rename_file_or_folder(path, new_path)

    def rename_file_or_folder(self, path, new_path):
        """파일 또는 폴더 이름 변경"""
        try:
            os.rename(path, new_path)
        except Exception as e:
            QMessageBox.critical(self, "오류", f"이름 변경 실패:\n{e}")
        else:
            self.status_bar.showMessage(f"이름 변경됨: {new_path}", 3000)

    def delete_item(self):
        """선택된 파일 또는 폴더 삭제"""
        path = self.get_selected_path()
        if not path:
            QMessageBox.warning(self, "경고", "삭제할 항목을 선택하세요.")
            return

        reply = QMessageBox.question(self, "삭제 확인", f"정말 삭제하시겠습니까?\n{path}", QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.delete_file_or_folder(path)

    def delete_file_or_folder(self, path):
        """파일 또는 폴더 삭제"""
        try:
            if os.path.isdir(path):
                os.rmdir(path)
            else:
                os.remove(path)
        except Exception as e:
            QMessageBox.critical(self, "오류", f"삭제 실패:\n{e}")
        else:
            self.status_bar.showMessage(f"삭제됨: {path}", 3000)

    def update_path_label(self, selected, _):
        """선택된 경로를 라벨에 갱신"""
        if indexes := selected.indexes():
            path = self.model.filePath(indexes[0])
            self.path_label.setText(f"선택된 경로: {path}")

    def open_file_on_double_click(self, index):
        """파일 더블 클릭 시 파일 열기"""
        file_path = self.model.filePath(index)
        if os.path.isfile(file_path):
            QDesktopServices.openUrl(QUrl.fromLocalFile(file_path))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FileExplorerMainWindow()
    sys.exit(app.exec())
