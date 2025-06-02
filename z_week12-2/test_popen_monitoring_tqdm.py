import subprocess
import os, sys
import re

# ========================================================

def get_pid_from_str(line):
    pattern = r"os\.getpid\(\)\s*=\s*(\d+)" # 그룹을 이용. 모니터링에 필요
    # patthern에서 원래 중간중간에 \\ 해줘야 하지만, r" "(raw string)로 감싸줘서 \ 만 해도 되게 함
    
    r_match = re.search(pattern, line)
    if r_match:
        pid = r_match.group(1)
        return pid
    else:
        return None
    
def extract_tqdm_info(tqdm_line):
    """tqdm 출력에서 진행률과 남은 시간 추출"""
    # 이미 encapsulation 구조임
    # 기본 패턴
    pattern = r'(\d+)%\|.*?\|\s*(\d+)/(\d+)\s*\[(\d{2}:\d{2})<([^,]+),\s*([^\]]+)\]'
    r_match = re.search(pattern, tqdm_line)
    
    if r_match:
        return {
            'percentage': int(r_match.group(1)), # 퍼센트
            'current': int(r_match.group(2)), # 진행된 항목 개수
            'total': int(r_match.group(3)), # 전체 항목 개수
            'elapsed': r_match.group(4), # 경과 시간
            'remaining': r_match.group(5), # 남은 시간
            'speed': r_match.group(6) # 초당 처리 속도
        }
    return None
     
if __name__ == "__main__":

    desired_cwd = os.path.abspath(os.path.dirname(sys.argv[0]))    
    
    os.chdir(desired_cwd)
    print(f"{os.getcwd()}")
    
    process = subprocess.Popen(
        ['python', 'dummy_task_tqdm.py'],
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE,
    
        text = True, # 보통은 True 충분함
        cwd = desired_cwd, 
        encoding = 'utf-8', # encoding과 errors는 같이 다님. 
        errors = 'ignore', # ignore로 해서 에러인 부분은 그냥 지나감.
    )
    
    while True: # 무한 루프
        output = process.stderr.readline()
        
        if output == "" and process.poll() is not None: # 즉 시스템이 죽은거를 뜻함
            break 
        
        if output:
            pid_str = get_pid_from_str(output.strip())
            if pid_str:
                cmd_pid = int(pid_str)
                print(f"{cmd_pid = }, {process.pid = }")
            else:
                status = extract_tqdm_info(output.strip())
                if status: 
                    print(status)
                else:
                    print(f"[{output}]")
    print("done!")