import sys

from PySide6.QtWidgets import (
    QApplication, QMainWindow,
    QWidget, QPushButton, QLabel, QVBoxLayout,
    QLineEdit, QInputDialog
)


class MW(QMainWindow):

    def __init__(self):
        super(MW, self).__init__()
        self.init_ui()
        self.show()

    def init_ui(self):
        self.button0 = QPushButton('Test.')
        self.button0.clicked.connect(self.slot00)

        self.ret_label = QLabel()

        layout = QVBoxLayout()
        layout.addWidget(self.button0)
        layout.addWidget(self.ret_label)

        tmp = QWidget()
        tmp.setLayout(layout)

        self.setCentralWidget(tmp)

    def slot00(self):
        print(self.sender())
        sender = self.sender()

        if sender == self.button0:
            # ✅ 기본: 텍스트 입력 다이얼로그
            ret_text, is_ok = QInputDialog.getText(
                self,
                "Input Text",
                "Enter Your Text!",
                QLineEdit.PasswordEchoOnEdit,
                "default text!"
            )
            if is_ok:
                self.ret_label.setText(f'{ret_text}')

            # --- 멀티라인 입력 ---
            """
            ret_text, is_ok = QInputDialog.getMultiLineText(
                self,
                "Input Text",
                "Enter Your Text!",
                "default text!"
            )
            if is_ok:
                self.ret_label.setText(f'{ret_text}')
            """

            # --- 정수 입력 ---
            """
            ret_int, is_ok = QInputDialog.getInt(
                self,
                "Input Integer",
                "Enter Your Int Value!",
                0,      # default
                0, 100, # range
                3       # step
            )
            if is_ok:
                self.ret_label.setText(f'{ret_int}')
            """

            # --- 실수 입력 ---
            """
            ret_double, is_ok = QInputDialog.getDouble(
                self,
                "Input Double",
                "Enter Your Double Value!",
                0.0,        # default
                0.0, 100.0, # range
                4           # precision
            )
            if is_ok:
                self.ret_label.setText(f'{ret_double}')
            """

            # --- 항목 선택 ---
            """
            ret_item, is_ok = QInputDialog.getItem(
                self,
                "Input Item",
                "Select Your Value!",
                ["faith", "hope", "love"],
                0
            )
            if is_ok:
                self.ret_label.setText(f'{ret_item}')
            """


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mw = MW()
    sys.exit(app.exec())
