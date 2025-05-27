import sys, os
from PySide6.QtWidgets import (QApplication, QMainWindow, QToolBar, 
    QLabel, QStatusBar)
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QAction, QIcon

# ==================================================================

class MW(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        self.fpath = os.path.dirname(
            os.path.abspath(__file__)
        )
        self.setFixedSize(600, 600)
        self.setWindowTitle("jy02's StatusBar")
        self.setup_main_wnd()
        self.create_action()
        self.create_tool_bar()
        self.create_menu()
        self.setStatusBar(QStatusBar()) # 최초 호출에서 상태바 추가
        self.show()
        
        def setup_main_wnd(self):
            self.label = QLabel("QStatusBar EX")
            self.label.setAlignment(
                Qt.AlignmentFlag.AlignCenter
            )
            self.setCentralWidget(self.label)
            
        def create_action(self):
            self.open_act = QAction(
                
            )