import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QMessageBox
)


class MW(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QDialog Example')

        # 기본 버튼 (Information dialog)
        button = QPushButton('Press me for a dialog!', self)
        button.clicked.connect(self.button_clicked)
        self.setCentralWidget(button)

        self.show()

    def button_clicked(self, s):
        print("click", s)

        # 기본 정보 대화 상자 표시
        result = QMessageBox.information(
            self,
            'Message',
            'This is an information message.',
            QMessageBox.Ok | QMessageBox.Cancel,
            QMessageBox.Ok
        )

        print('Dialog result:', result)

        # --- Critical MessageBox 예시 ---
        """
        result = QMessageBox.critical(
            self,
            'Critical',
            'This is a critical error message.',
            QMessageBox.Ok,
            QMessageBox.Ok
        )
        print('Dialog result:', result)
        """

        # --- Warning MessageBox 예시 ---
        """
        result = QMessageBox.warning(
            self,
            'Warning',
            'This is a warning message.',
            QMessageBox.Ok | QMessageBox.Cancel,
            QMessageBox.Ok
        )
        print('Dialog result:', result)
        """

        # --- Question MessageBox 예시 ---
        """
        response = QMessageBox.question(
            self,
            'Question Message',
            'Do you like PySide6?',
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.Yes
        )

        if response == QMessageBox.Yes:
            print('User likes PySide6!')
        else:
            print('User does not like PySide6!')

        print('Dialog result:', response)
        """


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = MW()
    app.exec()
