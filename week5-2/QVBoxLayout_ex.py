import sys

from PySide6.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout, QSizePolicy, QLineEdit, QPushButton)
from PySide6.QtCore import Qt

class MW (QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Ex: QVBoxLayout and QSizePolicy")
        self.setup_main_wnd()
        self.show()

    def setup_main_wnd(self):
        lm = QVBoxLayout()

        self.label0 = QLabel('Enter text!')
        lm.addWidget(self.label0)

        lm.addSpacing(10) # fixed spacing

        self.label1 = QLabel('--------')
        lm.addWidget(self.label1)

        lm.addSpacing(20) # fixed spacing

        self.line_edit = QLineEdit()
        # —————————————————————————————————-
        # sizePolicy attribute를 변경한 효과를 보기 위해선
        # 다음 주석을 해제해볼 것 (lm.addStrech 등을 반드시 주석처리할 것.)
        # self.line_edit.setSizePolicy(
        #     QSizePolicy.Policy.Preferred, 
        #     QSizePolicy.Policy.Preferred)

        # ———————————————————————————————-
        # 아래는 Expanding으로 sizePolicy를 설정한 경우임.
        # 역시 lm.addStrech를 주석처리해야 한다.
        # self.line_edit.setSizePolicy(
        #     QSizePolicy.Policy.Expanding, 
        #     QSizePolicy.Policy.Expanding)
        lm.addWidget(self.line_edit)

        # sizePolicy 효과를 보기 위해서는 아래 라인 주석처리 필요.
        lm.addStretch(1)

        self.label2 = QLabel('--------')
        lm.addWidget(self.label2)

        # sizePolicy 효과를 보기 위해서는 아래 라인 주석처리 필요.
        lm.addStretch(2)

        self.push_button = QPushButton("Check")
        # 아래는 Expanding으로 sizePolicy를 설정한 경우임.
        # 역시 lm.addStrech를 주석처리해야 한다.
        # self.push_button.setSizePolicy(
        #     QSizePolicy.Policy.Expanding, 
        #     QSizePolicy.Policy.Expanding)
        lm.addWidget(self.push_button)
        self.print_qsize()
        self.setLayout(lm)

    def print_qsize(self):

        print('==============================')
        print("label0's ideal size (=sizeHint)     :",self.label0.sizeHint())
        print("label1's ideal size (=sizeHint)     :",self.label1.sizeHint())
        print("label2's ideal size (=sizeHint)     :",self.label2.sizeHint())
        print("line_edit's ideal size (=sizeHint)  :",self.line_edit.sizeHint())
        print("push_button's ideal size (=sizeHint):",self.push_button.sizeHint())
        print('==============================')
        print("label0's size      :",self.label0.size()     ,"/",self.label0     .sizePolicy().verticalPolicy(),"/",self.label0     .sizePolicy().horizontalPolicy())
        print("label1's size      :",self.label1.size()     ,"/",self.label1     .sizePolicy().verticalPolicy(),"/",self.label1     .sizePolicy().horizontalPolicy())
        print("label2's size      :",self.label2.size()     ,"/",self.label2     .sizePolicy().verticalPolicy(),"/",self.label2     .sizePolicy().horizontalPolicy())
        print("line_edit's size   :",self.line_edit.size()  ,"/",self.line_edit  .sizePolicy().verticalPolicy(),"/",self.line_edit  .sizePolicy().horizontalPolicy())
        print("push_button's size :",self.push_button.size(),"/",self.push_button.sizePolicy().verticalPolicy(),"/",self.push_button.sizePolicy().horizontalPolicy())

    # resize event handler    
    def resizeEvent(self,event): # overriding함.
        super().resizeEvent(event)
        self.print_qsize()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_wnd = MW()
    sys.exit(app.exec())
