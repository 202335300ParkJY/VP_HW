import matplotlib.pyplot as plt

# 스타일 설정 (Set style)
plt.style.use('ggplot')

# 데이터 준비
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# 그래프 생성 (Create plot)
plt.plot(x, y)

# 그래프 제목 및 레이블 추가 (Add title and axis labels)
plt.title('Styled Line Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# 그래프 출력 (Display plot)
plt.show()