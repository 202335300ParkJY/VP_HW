import subprocess
import sys, os
from PySide6.QtCore import QTimer

from PySide6.QtCore import (
    QObject, QRunnable, QThreadPool,
    Signal, Slot
)

from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QTextEdit, QLabel, QPushButton,
    QVBoxLayout
)

# ======================== SubProcessWorker ========================
class SubProcessWorkerSignals(QObject):
    recv_line_signal = Signal(str)
    finished_signal = Signal()


class SubProcessWorker(QRunnable):
    def __init__(self, cmd, cwd=""):
        super().__init__()
        self.cmd = cmd if isinstance(cmd, list) else cmd.split()
        self.cwd = cwd
        self.signals = SubProcessWorkerSignals()

    @Slot()
    def run(self):
        try:
            process = subprocess.Popen(
                self.cmd,
                cwd=self.cwd,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                shell=False,
                text=True,
                encoding="utf-8"  #'cp949'도 가능. 오타를 내서 ct949로 했을 때에는 unknown encoding 문자 뜸.
            )

            for line in process.stdout:
                self.signals.recv_line_signal.emit(line.strip())

            process.stdout.close()
            process.wait()

        except Exception as e:
            self.signals.recv_line_signal.emit(f"Error: {e}")
        finally:
            self.signals.finished_signal.emit()

class MW(QMainWindow):
    def __init__(self):
        super().__init__()

        self.cwd = os.path.abspath(os.path.dirname(sys.argv[0]))
        os.chdir(self.cwd)

        self.cnt = 0
        self.threadpool = QThreadPool()

        self.init_ui()

        # 타이머 설정 (1초마다 카운트 증가)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.inc_cnt_slot)  # 타이머가 1초마다 inc_cnt_slot을 호출
        self.timer.start(1000)  # 1000ms (1초)마다 호출

    def init_ui(self):
        self.setWindowTitle("Ex: QRunnable and subprocess")
        self.lm = QVBoxLayout()

        self.setup_main_wnd()
        self.show()

    def setup_main_wnd(self):
        self.txt = QTextEdit()
        self.lm.addWidget(self.txt)

        btn_exec_thread = QPushButton("Run external cmd as QRunnable")
        btn_exec_thread.clicked.connect(self.start_cmd)
        self.lm.addWidget(btn_exec_thread)

        btn_exec_main = QPushButton("Run external cmd as MainThread")
        btn_exec_main.clicked.connect(self.start_cmd_as_main_thread)
        self.lm.addWidget(btn_exec_main)

        btn_cls = QPushButton("Clear text edit")
        btn_cls.clicked.connect(self.cls_slot)
        self.lm.addWidget(btn_cls)

        # 카운터 초기화 버튼
        btn_reset = QPushButton("Reset Counter")
        btn_reset.clicked.connect(self.reset_cnt_slot)
        self.lm.addWidget(btn_reset)

        self.label = QLabel(f"cnt = {self.cnt}")
        self.lm.addWidget(self.label)

        btn_cnt = QPushButton("Increment cnt")
        btn_cnt.clicked.connect(self.inc_cnt_slot)
        self.lm.addWidget(btn_cnt)

        container = QWidget()
        container.setLayout(self.lm)
        self.setCentralWidget(container)

    def inc_cnt_slot(self):
        self.cnt += 1  # 카운터 증가
        self.label.setText(f"cnt = {self.cnt}")  # QLabel 업데이트
        self.txt.append(f"Counter incremented: {self.cnt}")  # QTextEdit에 메시지 추가

    def reset_cnt_slot(self):
        self.cnt = 0  # 카운터 리셋
        self.label.setText(f"cnt = {self.cnt}")  # QLabel 업데이트
        self.txt.append("Counter reset to 0")  # QTextEdit에 리셋 메시지 추가

    def start_cmd(self):
        self.runner = SubProcessWorker(
            ["python", "dummy_task.py"],
            self.cwd
        )
        self.runner.signals.recv_line_signal.connect(self.result_slot)
        self.runner.signals.finished_signal.connect(lambda: self.result_slot("[Task finished]"))
        self.threadpool.start(self.runner)

    def start_cmd_as_main_thread(self):
        try:
            output = subprocess.getoutput("python dummy_task.py")
            self.result_slot(output)
        except Exception as e:
            self.result_slot(f"[Error] {e}")

    def result_slot(self, s):
        self.txt.append(s)

    def cls_slot(self):
        self.txt.clear()

# ======================== Entry ========================
if __name__ == "__main__":
    app = QApplication(sys.argv)
    wnd = MW()
    sys.exit(app.exec())
