import matplotlib.pyplot as plt

# 데이터 준비
x = [1, 2, 3, 4, 5]
y1 = [1, 4, 9, 16, 25]
y2 = [1, 2, 3, 4, 5]

# 그래프 생성 (Create plots)
plt.plot(x, y1, label='y = x^2')
plt.plot(x, y2, label='y = x')

# 범례 추가 (Add legend)
plt.legend()

# 그래프 제목 및 레이블 추가 (Add title and axis labels)
plt.title('Line Plot with Legend')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# 그래프 출력 (Display plot)
plt.show()