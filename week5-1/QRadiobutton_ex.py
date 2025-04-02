import sys

from PySide6.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout, QRadioButton, QButtonGroup)
from PySide6.QtCore import Qt

# ========================================
class MW (QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Ex: QRadioButton")
        self.setup_main_wnd()
        self.show()

    def setup_main_wnd(self):

        self.rb01 = QRadioButton('1. faith')
        self.rb02 = QRadioButton('2. hope')
        self.rb03 = QRadioButton('3. love')
        self.dp_label = QLabel("")


        # -------------------
        # layout manager setting
        lm = QVBoxLayout()        
        lm.addWidget(QLabel('What is most important?'))
        lm.addWidget(self.rb01)
        lm.addWidget(self.rb02)
        lm.addWidget(self.rb03) 
        lm.addWidget(self.dp_label)

        self.setLayout(lm)

        # -------------------
        # QButtonGroup setting
        self.bg = QButtonGroup(self)        
        self.bg.addButton(self.rb01)
        self.bg.addButton(self.rb02)
        self.bg.addButton(self.rb03)

        self.bg.buttonClicked.connect(self.ck_click) # 어떤 버튼이 눌렸는지 체크처리

    def ck_click(self, button):
        # click 이 이루어진 button의 text 얻기.        
        tmp = button.text()         
        self.dp_label.setText(tmp)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_wnd = MW()
    sys.exit(app.exec())
