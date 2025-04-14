import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, 
    QVBoxLayout, QMessageBox, 
    )
# =============================================================
class MW(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('QDialog.question Example')
        button = QPushButton("Press me for a dialog!",self)
        button.clicked.connect(self.button_clicked)
        self.setCentralWidget(button)
        self.show()

    def button_clicked(self, s):
        # built-in dialog 테스트를 위한 method.
        print("click", s)
        # 질문 대화 상자 표시
        response = QMessageBox.question(
                      self, 
                      'Question Message', 
                      'Do you like PySide6?',
                      QMessageBox.Yes | QMessageBox.No, 
                      QMessageBox.Yes)

        # 사용자 응답에 따라 행동
        if response == QMessageBox.Yes:
            print('User likes Python!')
        else:
            print('User does not like Python!')

        result = 
        
        # 사용자가 어떤 버튼을 눌렀는지 출력
        print('Dialog result:', result)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = MW()
    app.exec()
