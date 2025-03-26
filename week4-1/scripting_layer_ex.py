import matplotlib.pyplot as plt

# 데이터 준비
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# 그래프 생성
plt.plot(x, y)

# 그래프 제목 추가
plt.title('Simple Line Plot')

# x축, y축 레이블 추가
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# 그래프 출력
plt.show()