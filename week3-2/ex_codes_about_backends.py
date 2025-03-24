import matplotlib.pyplot as plt
import matplotlib

# 사용 가능한 모든 백엔드 목록 확인
print(matplotlib.rcsetup.all_backends)

#현재 사용 중인 백엔드 목록
print({f'----------------'})
print(matplotlib.get_backend())

#matplotlib의 경로 확인하는 코드
print({f'----------------'})
print(matplotlib.matplotlib_fname())

