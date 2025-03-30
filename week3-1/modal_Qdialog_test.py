import sys
from PySide6.QtWidgets import (
    QApplication,
    QDialog,
    QDialogButtonBox,
    QVBoxLayout, QLabel,
    QMainWindow,
    QPushButton,
)

class MW(QMainWindow): 
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QDialog Ex.")

        button = QPushButton("Press it for a Dialog")
        button.clicked.connect(self.button_clicked)

        self.setCentralWidget(button) #이 다음에 show가 없으므로 마지막에 꼭 넣어야 함.

    def button_clicked(self, s): #MW의 인스턴스 항목임. self가 들어갔기 때문.
        print("click", s)
        dlg = QDialog(self) #self,부모
        dlg.setWindowTitle("QDialog Title") 
        dlg.exec() #blocking mode로 동작

        # -------------
        # for custom dlg
        # dlg = CustomDlg(self) 
        # if dlg.exec(): # Modal Dialog
        #     print('ok')
        # else:
        #     print("cancel")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MW()
    window.show() #중요
    app.exec()

# https://share.note.sx/files/ys/ysudiqsx9cj25akonmkj.png
