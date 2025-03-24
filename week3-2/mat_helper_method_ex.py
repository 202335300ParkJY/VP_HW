import matplotlib.pyplot as plt
import numpy as np

# 데이터 준비
x = np.linspace(0, 50, 100)  # x축 범위를 50으로 확장
y = np.sin(x)

# Figure와 Axes 생성
fig, ax = plt.subplots()

# 1. ax.annotate (Annotate)
ax.annotate('Peak', xy=(25, np.sin(25)), xytext=(30, 0.8),
            arrowprops=dict(facecolor='black', arrowstyle='->'),
            fontsize=12)

# 2. ax.bar (Rectangle)
ax.bar([10, 20, 30, 40], [5, 6, 7, 8], color='skyblue', label="Bar Chart")

# 3. ax.errorbar (Line2D and Rectangle)
ax.errorbar(x, y, yerr=0.1, fmt='o', color='red', label="Error bars")

# 4. ax.fill (Polygon)
ax.fill(x, np.abs(y), color='lightgreen', alpha=0.5, label="Filled Area")

# 5. ax.hist (Rectangle)
data = np.random.randn(1000) * 5 + 20  # 데이터 범위를 넓히기 위해 조정
ax.hist(data, bins=30, color='orange', alpha=0.7, label="Histogram")

# 6. ax.imshow (AxesImage)
image = np.random.rand(10, 10)
ax.imshow(image, cmap='hot', interpolation='nearest', extent=[0, 50, -1, 1], alpha=0.6, label="Image")

# 7. ax.legend (Legend)
ax.legend(loc='upper left')

# 8. ax.plot (Line2D)
ax.plot(x, y, label='Sine wave', color='b', linestyle='-', linewidth=2)

# 9. ax.scatter (PathCollection)
ax.scatter(np.random.rand(50) * 50, np.random.rand(50) * 10, color='purple', label="Scatter plot")

# 10. ax.text (Text)
ax.text(25, 0.5, "This is a text annotation", fontsize=12, color='green')

# x축 범위 설정 (0에서 50까지)
ax.set_xlim(0, 50)

# 그래프 표시
plt.show()
