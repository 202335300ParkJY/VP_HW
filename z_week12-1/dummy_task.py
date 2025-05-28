import os, sys

from time import sleep

# 참고로 flush란 용어는 버퍼를 비우는 것임.
def flush_and_wait():
    sys.stdout.flush() # 이 둘은 flush로 stdout과 stderr를 비움
    sys.stderr.flush() #  ''
    sleep(1)
    
if __name__ == "__main__":
    
    sys.stdout.write(f"{os.getpid() = }\n") # write와 read로 stdout 읽고 씀
    
    for i in range(5):
        sys.stdout.write(f"task process's stdout: {i}\n")
        sleep(0.1)
    sys.stderr.write(f"total progress: 10%\n")
    flush_and_wait()
    
    for i in range(5, 10):
        sys.stdout.write(f"task process's stdout: {i}\n")
        sleep(0.2)
    sys.stderr.write(f"total progress: 30%\n")
    flush_and_wait()
    
