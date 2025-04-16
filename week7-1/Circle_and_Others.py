import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Figure와 Axes 생성 (캔버스와 그리는 영역)
fig, ax = plt.subplots(figsize=(6, 6))

# 1. 원 (Circle)
circle = patches.Circle(
    xy=(0.3, 0.7),       # 중심 좌표 (x, y)
    radius=0.1,          # 반지름
    edgecolor='r',       # 외곽선 색
    facecolor='none'     # 내부 색 없음 (투명)
)

# 2. 타원 (Ellipse)
ellipse = patches.Ellipse(
    xy=(0.7, 0.7),       # 중심 좌표
    width=0.3,           # 가로 길이
    height=0.15,         # 세로 길이
    angle=30,            # 회전 각도 (도 단위)
    edgecolor='g',       # 외곽선 색
    facecolor='lightgreen'  # 내부 색
)

# 3. 사각형 (Rectangle)
rectangle = patches.Rectangle(
    xy=(0.1, 0.1),       # 왼쪽 아래 꼭짓점 좌표
    width=0.3,           # 너비
    height=0.2,          # 높이
    edgecolor='b',       # 외곽선 색
    facecolor='lightblue'  # 내부 색
)

# 4. 정육각형 (RegularPolygon)
hexagon = patches.RegularPolygon(
    xy=(0.7, 0.2),       # 중심 좌표
    numVertices=6,       # 꼭짓점 수 (6각형)
    radius=0.1,          # 외접원의 반지름
    edgecolor='m',       # 외곽선 색
    facecolor='lavender'  # 내부 색
)

# 5. 화살표 (FancyArrow)
arrow = patches.FancyArrow(
    x=0.5, y=0.5,         # 시작점 좌표
    dx=0.3, dy=0.0,       # x, y 방향으로의 길이
    width=0.02,           # 화살표 몸통의 두께
    color='orange'        # 전체 색상
)

# 도형들을 Axes에 추가
for shape in [circle, ellipse, rectangle, hexagon, arrow]:
    ax.add_patch(shape)

# 축 설정
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')  # 비율 고정 (원형 유지)
plt.title("여러 Patch 도형 예제")
plt.show()