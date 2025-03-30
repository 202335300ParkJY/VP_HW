import sys
from PySide6.QtWidgets import (
    QApplication,
    QDialog,
    QDialogButtonBox,
    QVBoxLayout, QLabel,
    QMainWindow,
    QPushButton,
)

class CustomDlg(QDialog): 
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle('Hello, QDialog')

        buttons = QDialogButtonBox.Ok | QDialogButtonBox.Cancel #파이프, 바티컬 바 존재
        # 이를 통해 한 명령어의 출력을 다른 명령어의 입력으로 전달.
        # buttons에 해당하는 button 객체
        self.button_box = QDialogButtonBox(buttons) 

        # QDialog의 메서드를 slot으로
        self.button_box.accepted.connect(self.accept) 
        # QDialog의 메서드를 slot으로
        self.button_box.rejected.connect(self.reject)    

        self.layout = QVBoxLayout()
        message = QLabel('Is something ok?')
        self.layout.addWidget(message)
        # QDialogButtonBox 객체 추가.
        self.layout.addWidget(self.button_box) 
        self.setLayout(self.layout)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CustomDlg()
    window.show()
    app.exec()

# https://share.note.sx/files/ee/eezjicpj4aiowcermpn7.png
