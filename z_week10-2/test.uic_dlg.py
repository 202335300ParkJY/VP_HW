import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, 
)
from PyQt6 import uic

#forms = uic.loadUiType(    'simple_dlg.ui',)
from simple_dlg import Ui_Dialog

#print(forms[0].__name__, forms[1].__name__)

#class MW (forms[1], forms[0]):
class MW (QWidget, Ui_Dialog):

    def __init__(self):
        super().__init__()
        self.cnt = 0
        self.setupUi(self)
        self.init_ui()
        self.show()

    def init_ui(self):
        self.pushButton.clicked.connect(self.clk_slot)

    def clk_slot(self):
        self.cnt += 1
        self.label.setText(f"{self.cnt} clicked!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    wnd = MW()
    sys.exit(app.exec())