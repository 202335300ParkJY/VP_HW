import sys
import random
from PySide6.QtWidgets import (QMainWindow,QApplication,)
from PySide6.QtCore import QTimer

import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg

matplotlib.use('QtAgg')

# ============================================================

class MyCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, figsize =(5,5), dpi=100):
        self.fig, self.axes = plt.subplots(
            1,2,
            figsize=figsize, 
            dpi=dpi
        )
        super(MyCanvas, self).__init__(self.fig)

class MW(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('ex: dynamic plot')

        self.plt_canvas = MyCanvas(self, (5,10), 100)

        n_data = 10
        interval_ms = 10
        self.x_data0 = list(range(n_data))
        self.x_data1 = list(range(n_data)) 
        self.y_data0 = [0, 20]+[random.randint(0,20) for i in range(n_data-2)]
        self.y_data1 = [0, 20]+[random.randint(0,20) for i in range(n_data-2)]

        self.update_plot0()
        self.old_plot_ref = None
        self.update_plot1()   


        self.setCentralWidget(self.plt_canvas)
        self.show()

        self.timer0 = QTimer()
        self.timer0.setInterval(interval_ms) # milliseconds
        self.timer0.timeout.connect(self.update_plot0)
        self.timer0.start()


        self.timer1 = QTimer()
        self.timer1.setInterval(interval_ms) # milliseconds
        self.timer1.timeout.connect(self.update_plot1)
        self.timer1.start()

    def update_plot0(self):
        self.y_data0 = [ *self.y_data0[1:], random.randint(0,20)]
        self.plt_canvas.axes[0].cla()
        self.plt_canvas.axes[0].plot(self.x_data0, self.y_data0, label='method0')
        self.plt_canvas.axes[0].grid()
        self.plt_canvas.axes[0].legend(loc='upper right')
        self.plt_canvas.draw() # trigger the canvas to update and redraw

    def update_plot1(self):    
        self.y_data1 = [ *self.y_data1[1:], random.randint(0,20)]
        if self.old_plot_ref is not None:
            self.old_plot_ref.set_ydata(self.y_data1)
        else: 
            self.old_plot_ref = self.plt_canvas.axes[1].plot(
                self.x_data1, self.y_data1, 
                label='method1',
            )[0]
            self.plt_canvas.axes[1].grid()
            self.plt_canvas.axes[1].legend(loc='upper right')
        self.plt_canvas.draw()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    wnd = MW()
    sys.exit(app.exec())