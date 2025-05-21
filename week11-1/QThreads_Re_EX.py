from PySide6.QtCore import QThread, Signal
from PySide6.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QProgressBar
import time
import sys

# ====================================================================

class WorkerThread(QThread):
    update_signal = Signal(int)  # 진행 상태를 정수로 업데이트하기 위한 신호 정의

    def __init__(self, id):
        super().__init__()
        self.id = id

    def run(self):
        for i in range(101):
            time.sleep(0.1)  # 작업을 모방하기 위한 시간 지연
            self.update_signal.emit(i)  # 진행 상태 업데이트
        self.update_signal.emit(100)  # 작업 완료 시 100%로 설정

class MonitorThread(QThread):
    all_done = Signal()  # 모든 스레드가 완료되었을 때 발생하는 신호

    def __init__(self, threads):
        super().__init__()
        self.threads = threads

    def run(self):
        for thread in self.threads:
            thread.wait()  # 모든 스레드가 완료될 때까지 대기
        self.all_done.emit()  # 모든 스레드 완료 신호 발생

class MW(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.show()

    def init_ui(self):
        self.layout = QVBoxLayout(self)

        self.status_label = QLabel("Click 'Start All Threads' to run the threads", self)
        self.layout.addWidget(self.status_label)

        self.start_all_button = QPushButton("Start All Threads", self)
        self.start_all_button.clicked.connect(self.start_all_threads)
        self.layout.addWidget(self.start_all_button)

        self.progressBars = []
        self.threads = []
        self.buttons = []

        for i in range(3):
            label = QLabel(f"Thread {i+1} Example", self)
            progressBar = QProgressBar(self)
            progressBar.setMaximum(100)
            button = QPushButton(f"Start Thread {i+1}", self)
            button.clicked.connect(self.make_start_thread(i))

            self.layout.addWidget(label)
            self.layout.addWidget(progressBar)
            self.layout.addWidget(button)

            worker = WorkerThread(i)
            worker.update_signal.connect(progressBar.setValue)

            self.progressBars.append(progressBar)
            self.threads.append(worker)
            self.buttons.append(button)

        self.monitor_thread = MonitorThread(self.threads)
        self.monitor_thread.all_done.connect(self.update_status_label)

    def make_start_thread(self, index):
        def start_thread():
            if not self.threads[index].isRunning():  # 스레드가 실행 중이 아니면 시작
                self.threads[index].start()
        return start_thread

    def start_all_threads(self):
        for thread in self.threads:
            if not thread.isRunning():
                thread.start()
        self.monitor_thread.start()  # 모니터 스레드 시작

    def update_status_label(self):
        self.status_label.setText("All threads completed!")  # 레이블 업데이트

if __name__ == "__main__":
    app = QApplication(sys.argv)
    wnd = MW()
    sys.exit(app.exec())
