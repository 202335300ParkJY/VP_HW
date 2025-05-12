import sys
from PySide6.QtWidgets import (QMainWindow, QApplication)
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg

matplotlib.use('QtAgg')

# =================================================================

class MyCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, figsize=(5, 5), dpi=100):
        self.fig, self.axes = plt.subplots(
            1, 2,
            figsize=figsize,
            dpi=dpi
        )
        # Ensure the figure canvas is initialized with the figure object.
        super(MyCanvas, self).__init__(self.fig)

class MW(QMainWindow):

    def __init__(self):
        super().__init__()

        # Create canvas object
        plt_canvas = MyCanvas(self, (10, 5), 100)  # Adjust the size as needed

        # Plotting on the first axes (left side)
        plt_canvas.axes[0].plot([0, 1, 2, 3, 4], [10, 13, 20, 30, 15], label='Line')
        plt_canvas.axes[0].set_title('Line Plot')  # Optional title for clarity

        # Plotting on the second axes (right side)
        plt_canvas.axes[1].scatter([0, 1, 2, 3, 4], [10, 13, 20, 30, 15], label='Scatter')
        plt_canvas.axes[1].set_title('Scatter Plot')  # Optional title for clarity

        # Set grid and legends
        for ax in plt_canvas.axes:
            ax.grid(True)
            ax.legend()

        # Set central widget to be the canvas
        self.setCentralWidget(plt_canvas)

        # Window settings
        self.setWindowTitle("Matplotlib in PySide6")
        self.setGeometry(100, 100, 800, 600)  # Adjust window size as needed
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    wnd = MW()
    sys.exit(app.exec())
