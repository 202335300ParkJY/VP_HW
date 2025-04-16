import matplotlib.pyplot as plt
import numpy as np

import matplotlib.font_manager as fm
import platform
import os
# ==============================================================
def set_korean_font():
    system = platform.system()

    if system == 'Darwin':  # macOS
        font_name = 'AppleGothic'
    elif system == 'Windows':
        font_name = 'Malgun Gothic'
    elif system == 'Linux': # linux는 찾아줘야 함 (colab도 linux라서 colab에서도 돌아감)
        # 예: Colab이나 Ubuntu
        # 나눔고딕이 설치된 경우
        font_path = '/usr/share/fonts/truetype/nanum/NanumGothic.ttf'
        if os.path.exists(font_path):
            font_prop = fm.FontProperties(fname=font_path)
            plt.rcParams['font.family'] = font_prop.get_name()
            print(f"Success- font configuration: {font_prop.get_name()}")
            plt.rcParams['axes.unicode_minus'] = False
            return
        else:
            print("There is not avialble font for Korean.")
            return
    else:
        print("Not Available OS.")
        return

    # 공통 설정
    plt.rcParams['font.family'] = font_name
    plt.rcParams['axes.unicode_minus'] = False
    print(f"폰트 설정 완료: {font_name}")

# 사용 예시
set_korean_font()

# 데이터 생성
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Figure와 Axes 객체 생성
fig, ax = plt.subplots()

# 그래프 그리기
ax.plot(
    x, y,
    linestyle='--',        # '--' : dashed line
    linewidth=2.0,         # 선의 굵기
    color='b',             # 'b' : blue
    alpha=0.7,             # 투명도
    marker='o',            # 'o' : 원형 마커
    markersize=6,          # 마커 크기
    markeredgewidth=1.5,   # 마커 외곽선 굵기
    markerfacecolor='red', # 마커 내부 색상
    markeredgecolor='black' # 마커 외곽선 색상
)

# 제목과 축 레이블 설정
ax.set_title('객체 지향 스타일의 그래프')
ax.set_xlabel('X 축')
ax.set_ylabel('Y 축')

# 그리드 추가
ax.grid(True)

# 그래프 표시
plt.show()