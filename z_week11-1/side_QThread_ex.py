from PySide6.QtCore import QThread, Signal
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, 
        QVBoxLayout, QWidget, )
import time, sys, os

# =========================================================================

class WorkerThread(QThread):
    update_signal = Signal(str)  # 신호 정의
    def run(self):
        for i in range(5):
            time.sleep(1)  # 작업을 모방하기 위한 시간 지연
            self.update_signal.emit(f"Working {i+1}")  # 진행 상태 업데이트
        self.update_signal.emit("Task completed!")  # 작업 완료 메시지

class MW(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.show()

    def init_ui(self):
        # 레이아웃과 위젯 설정
        self.label = QLabel("Thread Example", self)
        self.button = QPushButton("Start Thread", self)
        self.button.clicked.connect(self.start_thread)

        layout = QVBoxLayout(self)
        layout.addWidget(self.label)
        layout.addWidget(self.button)

        self.worker = WorkerThread()
        self.worker.update_signal.connect(self.update_label)

    def start_thread(self):
        if not self.worker.isRunning():  # 스레드가 실행 중이 아니면 시작
            self.worker.start()

    def update_label(self, message):
        self.label.setText(message)  # 레이블 업데이트

if __name__ == "__main__":
    app = QApplication(sys.argv)
    wnd = MW()
    sys.exit(app.exec())
