import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Figure와 Axes 생성
fig, ax = plt.subplots()

# Rectangle 객체 생성 (x, y, width, height)
# 여기서 (x, y)는 사각형의 왼쪽 하단 좌표
rect = patches.Rectangle((0, 0), 1, 1, linewidth=0, edgecolor='r', facecolor='lightblue')

# Rectangle 객체를 Axes에 추가
ax.add_patch(rect)

# Axes의 설정
ax.set_xlim(0, 2)
ax.set_ylim(0, 2)

plt.show()