import sys

from PySide6.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton)

# ==================================
class MW(QWidget): 

    def __init__(self): 
        super().__init__() 
        self.init_ui() 

    def init_ui(self):
        self.setMaximumSize(340, 120)
        self.setWindowTitle("QLineEdit Example")

        self.setup_main_wnd()
        self.show()

    def setup_main_wnd(self):
        QLabel("Please enter your name below.", self).move(50, 10)
        name_label = QLabel("Name:", self)
        name_label.move(10, 50) 

        self.name_edit = QLineEdit(self)
        self.name_edit.resize(210, 20)
        self.name_edit.move(80, 50)
        self.name_edit.setStyleSheet("background-color: yellow; color: rgb(50,150,250)")
        self.name_edit.setMaxLength(30)
        self.name_edit.setPlaceholderText('Enter your text')

        self.name_edit.returnPressed.connect(self.on_return_pressed)
        self.name_edit.selectionChanged.connect(self.on_selection_changed)
        self.name_edit.textChanged.connect(self.on_text_changed)
        self.name_edit.textEdited.connect(self.on_text_edited)

        clear_button = QPushButton("Clear", self)
        clear_button.move(100, 80)
        clear_button.clicked.connect(self.clearText)

        accept_button = QPushButton("OK", self)
        accept_button.move(200, 80)        
        accept_button.clicked.connect(self.acceptText)

    def clearText(self):
        self.name_edit.clear()

    def acceptText(self):
        print(self.name_edit.text())
        self.close()

    def on_return_pressed(self):
        print('Return Pressed!')
    def on_selection_changed(self):
        print('Selected Text Changed')
    def on_text_changed(self, text):
        print(f'Text Changed : [{text}]')
    def on_text_edited(self, text):
        print(f'Text Edited : [{text}]')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = MW()
    sys.exit(app.exec())

