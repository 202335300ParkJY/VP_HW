from re import L
import subprocess
import sys, os

from PySide6.QtCore import(
    QObject,
    QRunnable, QThreadPool,
    Signal, Slot,
)

from PySide6.QtWidgets import(
    QApplication,
    QMainWindow, QWidget,
    QTextEdit, QLabel,
    QPushButton, QVBoxLayout, 
)

# QRunnable 은 직접 Signal객체를 attribute로 가지지 못함.
# 때문에 QObject를 상속받은 클래스를 만들고, 여기에 class attribute로 Signal객체를 만들 것.
# 정의 위치로는 class attributer이나, PySide6의 메타 클래스가 이들을 
# instance 별 Signal객체로 만들어줌.
# 반드시 class attribute로 할당해야 제대로 동작함. 
class SubProcessWorkerSignals(QObject):
    
    recv_line_signal = Signal(str)
    finished_signal = Signal()
    
import re
# https://dsaint31.tistory.com/548 참고
class SubProcessWorker(QRunnable):
    
    def __init__(self, cmd, cwd=""):
        super().__init__()
        
        self.signals = SubProcessWorkerSignals()
        
        self.cmd = cmd
        self.cwd = cwd
        
    @Slot()
    def run(self):
        process = subprocess.Popen(
            ['python', 'dummy_executable.py'],
            stdout = subprocess.PIPE,
            stderr = subprocess.STDOUT,
    
            text = True,
            cwd = self.cwd,
            encoding = 'utf-8',
            errors = 'ignore',
        )
        while True:
            output = process.stdout.readline()
            
            if output == "" and process.poll() is not None:
                break
            
            pid_str = self.get_pid_from_str(output.strip())
            if pid_str:
                self.cmd_pid = int(pid_str)
            
            self.signals.recv_line_signal.emit(output.strip())
        
        # output = subprocess.getoutput(self.cmd)
        # self.signals.result_signal.emit(output)
        self.signals.finished_signal.emit()
        
    def get_pid_from_str(self, line):
        pattern = r"os\.getpid\(\)\s*=\s*(\d+)" # \ 그룹을 이용. s는 문자열임. + 기호는 하나 이상의 수
        r_match = re.search(pattern, line)
        if r_match:
            pid = r_match.group(1)
            return pid
        else:
            return None
        
class MW(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.cwd = os.path.abspath(os.path.dirname(sys.argv[0]))
        os.chdir(self.cwd)
        
        self.cnt = 0
        self.threadpool = QThreadPool()
        
        self.init_ui()
        
    def init_ui(self):
        self.setWindowTitle("Ex: QRunnable and subprocess")
        self.setup_main_wnd()
        self.show()
        
    def setup_main_wnd(self):
        lm = QVBoxLayout()
        
        # subprocess의 stdout의 결과를 보여주는 QTextEdit
        self.txt = QTextEdit()
        lm.addWidget(self.txt)
        
        # QRunnable을 통해 별도의 Thread에서 동작시킴.
        btn_exec = QPushButton("run external cmd as QRunnable")
        btn_exec.clicked.connect(self.start_cmd)
        lm.addWidget(btn_exec)
        
        # MainThread에서 동작시킴.
        btn_exec = QPushButton("run external cmd as MainThread")
        btn_exec.clicked.connect(self.start_cmd_as_main_thread)
        lm.addWidget(btn_exec)
        
        # QTextEdit 객체의 문자열을 초기화.
        btn_cls = QPushButton("clear text edit")
        btn_cls.clicked.connect(self.cls_slot)
        lm.addWidget(btn_cls)
        
        # subprocess 실행 중 MainThread의 동작을 확인하기 위한
        # cnt 확인용 QLabel
        self.label = QLabel(f"cnt = {self.cnt}")
        lm.addWidget(self.label)
        
        # subprocess 실행 중 MainThread의 동작을 확인하기 위한
        # cnt 증가용 QPushButton
        btn_cnt = QPushButton("increment cnt")
        btn_cnt.clicked.connect(self.inc_cnt_slot)
        lm.addWidget(btn_cnt)
        
        container = QWidget()
        container.setLayout(lm)
        self.setCentralWidget(container)
        
    def start_cmd(self):
        # subprocess 의 blocking 실행을 별도의 Thread로 수행.
        self.runner = SubProcessWorker("python dummy_executable.py", self.cwd)
        # Thread가 subprocess의 실행이 종료되면 Signal and Slot을 통해
        # main thread 에 전달.
        self.runner.signals.recv_line_signal.connect(self.resv_line_slot)
        self.threadpool.start(self.runner)
    
    def start_cmd_as_main_thread(self):
        output = subprocess.getoutput("python dummy_executable.py")
        self.result_slot(output)
        
    def resv_line_slot(self, s):
        self.txt.append(f"{self.runner.cmd_pid}: {s}")
    
    def result_slot(self, s):
        self.txt.append(s)
    
    def cls_slot(self):
        self.txt.clear()
    
    def inc_cnt_slot(self):
        self.cnt += 1
        self.label.setText(f"cnt = {self.cnt}")
        
                
if __name__ == "__main__":
    app = QApplication(sys.argv)
    wnd = MW()
    sys.exit(app.exec())
    
    