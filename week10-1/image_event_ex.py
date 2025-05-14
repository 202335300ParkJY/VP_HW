import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QWidget,
)
from matplotlib.figure import Figure
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar

# =========================================================

# MW 클래스는 pyside6의 QMainwindow 상속받아 유저 정의 윈도우 생성
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Event Handling with Matplotlib and PySide6")
        
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.ax = self.figure.add_subplot(111)
        self.ax.plot([1,2,3,4], [1,4,9,16])
        self.toolbar = NavigationToolbar(self.canvas, self)
        
        layout = QVBoxLayout()
        widget = QWidget()
        self.setCentralWidget(widget)
        widget.setLayout(layout)
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        
        self.canvas.setFocusPolicy(Qt.StrongFocus)
        self.canvas.setFocus()
        
        self.canvas.mpl_connect("button_press_event", self.on_press)
        self.canvas.mpl_connect("button_release_event", self.on_release)
        self.canvas.mpl_connect("motion_notify_event", self.on_motion)
        self.canvas.mpl_connect("key_press_event", self.on_key_press)
        self.canvas.mpl_connect("key_release_event", self.on_key_release)
        
    def on_press(self, event):
        print()
        
'''
이 부분 아래부터는 그냥 집 가서 내용 수정하기 . 그림으로 넣어서 확인해보는거? 좌표대신?
'''

