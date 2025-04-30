import numpy as np
import matplotlib.pyplot as plt

# 샘플 데이터 생성: 0에서 100 사이의 1000개 랜덤 값
x = np.random.normal(loc=50, scale=15, size=1000)

# 히스토그램 그리기
plt.hist(
    x, 
    bins=30,  # 구간 개수
    range=(0, 100),  # 데이터 범위 지정
    density=True,  # 확률 밀도 함수로 정규화
    cumulative=False,  # 누적 히스토그램
    histtype='bar',  # 막대 형태
    align='mid',  # 막대 정렬 방식
    orientation='vertical',  # 수직 방향
    rwidth=0.9,  # 막대 너비
    log=False,  # 로그 스케일 사용 안 함
    color='blue',  # 색상 지정
    label='Sample Data',  # 레이블 지정
    stacked=False  # 쌓인 히스토그램 아님
)

# 레이블과 타이틀 추가
plt.xlabel('Value')
plt.ylabel('Density')
plt.title('Histogram Example')

# 범례 추가
plt.legend()

# 그래프 출력
plt.show()
