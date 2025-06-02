import os, sys

from time import sleep
import tqdm

# ==================================================================

if __name__ == "__main__":
    
    sys.stdout.write(f"{os.getpid() = }\n") # write와 read로 stdout 읽고 씀
    for i in tqdm.tqdm(range(100)):
        # print(idx, end="\r") # 이 부분은 별로 추천하지 않은 방법임을 알아두기
        sleep(0.1)
        
        
        
        
        