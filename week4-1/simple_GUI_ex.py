# juy02_labels.py
# -------------------------------------------------
import sys, os
import traceback

DS_DEBUG = False

try:
    from PySide6.QtWidgets import QApplication, QWidget, QLabel
    from PySide6.QtGui import QFont,QPixmap
    from PySide6.QtCore import Qt
except Exception as e:
    if DS_DEBUG:
        traceback.print_exc()
    print("Can't import PySide6 modules!")


try:
    from PyQt6.QtWidgets import QApplication, QWidget, QLabel
    from PyQt6.QtGui import QFont,QPixmap
    from PyQt6.QtCore import Qt
except Exception as e:
    if DS_DEBUG:
        traceback.print_exc()
    print("Can't import PyQt6 modules!")

# -------------------------------------------------
class MW(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setGeometry(300,300,350,300)
        self.setFixedSize(350,300)
        self.setWindowTitle('QLabel Example')
        self.setup_main_wnd()
        self.show()

    def setup_main_wnd(self):
        # hello_label = QLabel('Hello, World and Qt!',self) # 아래 두라인과 동일한 수행.
        hello_label = QLabel(self)
        hello_label.setText('Hello, World and Qt!! juy02 ')
        hello_label.setFont(QFont('Arial',15))
        
        # hello_label.setAlignment(Qt.AlignmentFlag.AlignCenter) 
        # hello_label.setStyleSheet("background-color: yellow")
        hello_label.move(10,10)

        path_py_file = os.path.realpath(__file__)
        path_py_file = os.path.dirname(path_py_file)
        img_fstr = os.path.join(path_py_file,'earth_planet_map-1324554.jpg!d')
        try:
            with open(img_fstr):
                world_label = QLabel(self)
                pixmap = QPixmap(img_fstr)
                pixmap = pixmap.scaled(300,300, Qt.AspectRatioMode.KeepAspectRatio)
                # KeepAspectRatio는 가로세로 비율을 유지하면서 크기 조절 가능
                world_label.setPixmap(pixmap)
                world_label.move(25,40)
        except FileNotFoundError as err:
            print(f'Image not found.\nError: {err}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = MW()
    sys.exit(app.exec())
