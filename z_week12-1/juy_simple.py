import subprocess
import sys, os

from PySide6.QtCore import (
    QObject, QRunnable, QThreadPool, Signal, Slot
)
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QTextEdit, QLabel, QPushButton,
    QVBoxLayout
)

# =============================================
class SubProcessSignals(QObject):
    recv_line_signal = Signal(str)


class SubProcessWorker(QRunnable):
    def __init__(self, cmd: str, cwd: str):
        super().__init__()
        self.cmd = cmd
        self.cwd = cwd
        self.cmd_pid = None
        self.signals = SubProcessSignals()

    @Slot()
    def run(self):
        process = subprocess.Popen(
            self.cmd,
            cwd=self.cwd,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True
        )
        self.cmd_pid = process.pid
        for line in process.stdout:
            self.signals.recv_line_signal.emit(line.strip())
        process.stdout.close()
        process.wait()


# =============================================
class MW(QMainWindow):
    def __init__(self):
        super().__init__()
        self.cwd = os.path.abspath(os.path.dirname(sys.argv[0]))
        self.cnt = 0
        self.threadpool = QThreadPool()
        self.cmd = ["python dummy_task.py"]
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Ex: QRunnable and subprocess")

        self.txt = QTextEdit()
        self.label = QLabel(f"cnt = {self.cnt}")

        layout = QVBoxLayout()
        layout.addWidget(self.txt)
        layout.addWidget(self._make_button("Run command in QRunnable", self.start_cmd))
        layout.addWidget(self._make_button("Run command in MainThread", self.start_cmd_as_main_thread))
        layout.addWidget(self._make_button("Clear text edit", self.cls_slot))
        layout.addWidget(self.label)
        layout.addWidget(self._make_button("Increment cnt", self.inc_cnt_slot))

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        self.show()

    def _make_button(self, text, slot_func):
        btn = QPushButton(text)
        btn.clicked.connect(slot_func)
        return btn

    def start_cmd(self):
        self.runner = SubProcessWorker(self.cmd[0], self.cwd)
        self.runner.signals.recv_line_signal.connect(self.resv_line_slot)
        self.threadpool.start(self.runner)

    def start_cmd_as_main_thread(self):
        output = subprocess.getoutput(self.cmd[0])
        self.result_slot(output)

    def resv_line_slot(self, s):
        self.txt.append(f"{self.runner.cmd_pid}: {s}")

    def result_slot(self, s):
        self.txt.append(s)

    def cls_slot(self):
        self.txt.clear()

    def inc_cnt_slot(self):
        self.cnt += 1
        self.label.setText(f"{self.cnt = }")


# =============================================
if __name__ == "__main__":
    app = QApplication(sys.argv)
    wnd = MW()
    sys.exit(app.exec())
