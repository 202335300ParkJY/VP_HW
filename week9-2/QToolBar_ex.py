import sys, os

from PySide6.QtWidgets import (
    QApplication, QMainWindow, 
    QToolBar, QMessageBox,
)
from PySide6.QtGui import (
    QAction, QIcon,
)

# ===========================================================

class MW(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup_main_wnd()

    def setup_main_wnd(self):
        # 윈도우 설정
        self.setWindowTitle("Ex0: QToolBar")
        self.setGeometry(300, 300, 300, 200)
        root_dir = os.path.dirname(__file__)
        self.create_actions(root_dir)
        self.create_toolbar()
        self.show()

    def create_actions(self, root_dir):

        icon0_path = os.path.join(root_dir,
                                 'baseline_compress_black_36pt_3x.png')
        icon1_path = os.path.join(root_dir,
                                 'baseline_favorite_black_36pt_1x.png')
        # 툴바에 액션 추가
        self.button_action0 = QAction("action0", self)
        self.button_action0.setStatusTip("This is the first button")
        self.button_action0.setIcon(QIcon(icon0_path))
        self.button_action0.setShortcut('Ctrl+0')
        self.button_action0.triggered.connect(self.onAction0)

        # 또 다른 액션 추가
        self.button_action1 = QAction("action1", self)
        self.button_action1.setStatusTip("This is the second button")
        self.button_action1.setIcon(QIcon(icon1_path))
        self.button_action1.setShortcut('Ctrl+1')
        self.button_action1.triggered.connect(self.onAction1)

    def create_toolbar(self):    
        # 툴바 생성
        self.toolbar = QToolBar("Main Toolbar")
        self.addToolBar(self.toolbar)
        self.toolbar.addAction(self.button_action0)
        self.toolbar.addAction(self.button_action1)


    def onAction0(self):
        QMessageBox.information(self, "Message", "You clicked the first button!")

    def onAction1(self):
        QMessageBox.information(self, "Message", "You clicked the second button!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    wnd = MW()
    sys.exit(app.exec())