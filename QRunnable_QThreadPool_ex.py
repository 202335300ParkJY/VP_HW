from PySide6.QtCore import QRunnable, QThreadPool, Signal, Slot
from PySide6.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget
import time
import sys

# ==============================================================

class Task(QRunnable):
    def __init__(self, num, update_signal):
        super().__init__()
        self.num = num
        self.update_signal = update_signal

    def run(self):
        for i in range(101):
            time.sleep(0.1)  # 작업을 모방하기 위한 시간 지연
            self.update_signal.emit(f"Thread {self.num}: {i}% completed", self.num)  # 진행 상태 업데이트
        self.update_signal.emit(f"Thread {self.num}: Task completed!", self.num)  # 작업 완료 메시지

class MainWindow(QWidget):
    update_signal = Signal(str, int)  # 메시지와 스레드 번호를 전달하는 신호

    def __init__(self):
        super().__init__()
        self.init_ui()
        self.show()

    def init_ui(self):
        self.layout = QVBoxLayout(self)

        self.labels = [QLabel(f"Thread {i+1}: Waiting to start...", self) for i in range(3)]
        for label in self.labels:
            self.layout.addWidget(label)

        self.start_button = QPushButton("Start All Tasks", self)
        self.start_button.clicked.connect(self.start_tasks)
        self.layout.addWidget(self.start_button)

        self.pool = QThreadPool.globalInstance()

    @Slot()
    def start_tasks(self):
        for i in range(3):
            task = Task(i, self.update_signal)
            self.pool.start(task)
        self.update_signal.connect(self.update_label)

    @Slot(str, int)
    def update_label(self, message, idx):
        self.labels[idx].setText(message)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()