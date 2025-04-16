import matplotlib.pyplot as plt
import matplotlib.patches as patches

# 원의 중심 좌표와 반지름 설정
c_pnt = (0.5, 0.5)
r = 0.4

# Figure와 Axes 생성
fig, ax = plt.subplots(figsize=(5,5))

# 원 생성
circle = patches.Circle(
    c_pnt, 
    r, 
    edgecolor='r', 
    facecolor='none',
    )

# 원을 Axes에 추가
ax.add_patch(circle)

# 축 범위 설정
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

# 그래프 표시
plt.show()