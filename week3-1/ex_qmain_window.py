# ex_qmain_window.py
# Import necessary modules
import sys

PYSIDE = True
PYQT = False

try:
    import PySide6.QtCore
    from PySide6.QtWidgets import (QApplication, 
                                   QWidget, QMainWindow, 
                                   QLabel, QVBoxLayout,
                                   )
    from PySide6.QtGui import QIcon

except Exception as e:
    print(e)
    PYSIDE = False

if not PYSIDE :
    PYQT = True
    try:
        import PyQt6.QtCore
        from PyQt6.QtWidgets import (QApplication, 
                                    QWidget, QMainWindow, 
                                    QLabel, QVBoxLayout,
                                    )
        from PyQt6.QtGui import QIcon
    except Exception as e:
        print(e)
        PYQT = False

class MW(QMainWindow):
    def __init__(self):
        """ Constructor for MW Class """
        super().__init__()
        self.initialize_ui()

    def initialize_ui(self):
        import os
        img_path = os.path.dirname(os.path.abspath(__file__))
        """set up the application."""
        self.setMinimumSize(400, 500) #width, height
        self.setWindowTitle("Title of Main Window")
        self.setWindowIcon(QIcon(img_path))
        self.setup_main_wnd()
        self.show() # Display the window on the screen
        # self.showFullScreen()
        # self.showNormal()

    def setup_main_wnd(self):
        """set up the main window."""

        # 1번과정. 여기선 QLabel 인스턴스 2개를 생성.
        label0 = QLabel("test0")
        label1 = QLabel("test1")
        # 2번 과정. Layout Manager 생성.
        vbox = QVBoxLayout()
        # 3번 과정. 1번 과정에서 만든 Widget인스터스들을 LayoutManger에 추가.
        vbox.addWidget(label0)
        vbox.addWidget(label1)
        # 4번 과정. Container 인스턴스 생성.
        container = QWidget()
        # 5번 과정. Container 인스턴스의 Layout Manager를 설정.
        container.setLayout(vbox)
        # 6번 과정. Main Window 인스턴스에 Central Widget으로 Container 인스턴스 설정.
        self.setCentralWidget(container)

# Run the program
if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = MW()
    sys.exit(app.exec())
