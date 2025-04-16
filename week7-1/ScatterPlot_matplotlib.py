import matplotlib.pyplot as plt

# 데이터 준비
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# 산점도 생성 (Create scatter plot)
plt.scatter(x, y)

# 그래프 제목 추가 (Add title)
plt.title('Simple Scatter Plot')

# x축, y축 레이블 추가 (Add x and y axis labels)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# 그래프 출력 (Display plot)
plt.show()