import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.collections import PatchCollection
import numpy as np

# Figure와 Axes 생성
fig, ax = plt.subplots(figsize=(6, 6))

patches_list = []  # Circle 객체들을 담을 리스트

# 난수 고정 (재현성 확보)
np.random.seed(0)

# 원 20개 생성
for _ in range(20):
    center = np.random.rand(2)        # 중심 좌표: (x, y), [0.0 ~ 1.0)
    radius = np.random.rand() * 0.05 + 0.02  # 반지름: 0.02 ~ 0.07
    circle = patches.Circle(
        center,   # 중심 좌표
        radius    # 반지름
    )
    patches_list.append(circle)  # 리스트에 추가

# PatchCollection 생성
collection = PatchCollection(
    patches_list,          # 도형 객체들 리스트
    edgecolor='black',     # 외곽선 색상
    facecolor='skyblue',   # 내부 색상
    alpha=0.7              # 투명도
)

# 컬렉션을 Axes에 추가
ax.add_collection(collection)

# 축 설정
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')
plt.title("PatchCollection을 이용한 원 배열")
plt.show()