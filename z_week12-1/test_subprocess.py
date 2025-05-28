import subprocess
import os, sys

cmd = ["python", "dummy_task.py"]

if __name__ == "__main__": # 이렇게 해주는 이유가 윈도우는 spawn 사용하기 때문
    
    cwd = os.path.abspath(
         os.path.dirname(
             sys.argv[0]
             )
         )
    # 위 __file__ 대신 sys.argv[0]으로 (우회)
    
    os.chdir(cwd)
    print(f"> {cwd = }")
    
    full_cmd = " ".join(cmd) # " "을 구분문자로 함     
    
    # output_str = subprocess.getoutput(full_cmd)
    output = subprocess.check_output(
        cmd,
        # text = True, # False면 바이츠 어레이로 보냄
    )
    print(type(output))
    output_str = output.decode("cp949")
    
    print(f"> {output_str.strip()}")

# stdout은 task들을, stderr는 total progress를