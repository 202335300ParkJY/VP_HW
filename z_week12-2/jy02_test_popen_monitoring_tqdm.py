import subprocess
import os
import sys
import re

# =======================================================

class TaskMonitor:
    def __init__(self, script_name):
        self.script_name = script_name
        self.process = None
        self.current_pid = None

    def get_pid_from_str(self, line):
        """PID를 추출하는 함수"""
        pattern = r"os\.getpid\(\)\s*=\s*(\d+)"
        r_match = re.search(pattern, line)
        if r_match:
            self.current_pid = r_match.group(1)
            return self.current_pid
        return None

    def extract_tqdm_info(self, tqdm_line):
        """tqdm 진행 상태 정보를 추출하는 함수"""
        pattern = r'(\d+)%\|.*?\|\s*(\d+)/(\d+)\s*\[(\d{2}:\d{2})<([^,]+),\s*([^\]]+)\]'
        r_match = re.search(pattern, tqdm_line)
        if r_match:
            return {
                'percentage': int(r_match.group(1)),  # 퍼센트
                'current': int(r_match.group(2)),  # 진행된 항목 개수
                'total': int(r_match.group(3)),  # 전체 항목 개수
                'elapsed': r_match.group(4),  # 경과 시간
                'remaining': r_match.group(5),  # 남은 시간
                'speed': r_match.group(6),  # 초당 처리 속도
            }
        return None

    def start_process(self):
        """외부 스크립트를 실행하고, 그 결과를 모니터링하는 메서드"""
        desired_cwd = os.path.abspath(os.path.dirname(sys.argv[0]))
        os.chdir(desired_cwd)
        print(f"Current working directory: {os.getcwd()}")
        
        self.process = subprocess.Popen(
            ['python', self.script_name],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            cwd=desired_cwd,
            encoding='utf-8',
            errors='ignore'
        )

    def monitor_process(self):
        """실행 중인 프로세스를 모니터링하고, PID와 진행 상태를 출력하는 메서드"""
        while True:
            output = self.process.stderr.readline()
            if output == "" and self.process.poll() is not None:
                break

            if output:
                pid_str = self.get_pid_from_str(output.strip())
                if pid_str:
                    print(f"Process PID: {pid_str}")
                else:
                    status = self.extract_tqdm_info(output.strip())
                    if status:
                        print(status)
                    else:
                        print(f"[{output}]")
                        
# ===============================================================

if __name__ == "__main__":
    # TaskMonitor 클래스를 인스턴스화 하고, 프로세스 모니터링 시작
    monitor = TaskMonitor('dummy_task_tqdm.py')
    monitor.start_process()
    monitor.monitor_process()
