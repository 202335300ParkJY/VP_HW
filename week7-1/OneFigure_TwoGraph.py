import matplotlib.pyplot as plt

# 데이터 준비
x = [1, 2, 3, 4, 5]
y1 = [1, 4, 9, 16, 25]
y2 = [1, 2, 3, 4, 5]

# Figure와 Subplot 생성 (Create figure and subplots)
plt.figure()

# 첫 번째 subplot
plt.subplot(2, 1, 1)  # (행, 열, 위치)
plt.plot(x, y1, 'r')  # 'r'은 red 색상을 의미
plt.title('First Plot')

# 두 번째 subplot
plt.subplot(2, 1, 2)
plt.plot(x, y2, 'b')  # 'b'는 blue 색상을 의미
plt.title('Second Plot')

# 레이아웃 조정 및 그래프 출력 (Adjust layout and display plot)
plt.tight_layout()
plt.show()