# 먼저 필요한 라이브러리를 import
import matplotlib.pyplot as plt
import numpy as np

# 대화형(REPL, or interactive) 모드 활성화
plt.ion()

# 데이터 생성
x = np.linspace(0, 10, 100)
y = np.sin(x)

# 그래프 생성
fig, ax = plt.subplots()
line, = ax.plot(x, y, 'b-')
ax.set_title('Interactive Sine Wave')
ax.set_xlabel('x')
ax.set_ylabel('sin(x)')
ax.grid(True)

'''
# 위상 변경해보기
y = np.sin(x + 1)
line.set_ydata(y)
fig.canvas.draw()

# 주파수 변경해보기
y = np.sin(2 * x)
line.set_ydata(y)
fig.canvas.draw()

# 진폭 변경해보기
y = 0.5 * np.sin(x)
line.set_ydata(y)
fig.canvas.draw()

# 직선 그려보기
y = 0.1 * x
line.set_ydata(y)
fig.canvas.draw()

# y축 범위 변경해보기
ax.set_ylim(-2, 2)
fig.canvas.draw()

# 그래프 제목 변경해보기
ax.set_title('Modified in REPL')
fig.canvas.draw()

# 그래프 색상 변경해보기
line.set_color('red')
fig.canvas.draw()

# 선 스타일 변경해보기
line.set_linestyle('--')
fig.canvas.draw()
'''

# 대화형 모드 비활성화
# plt.ioff()
# 그래프 창 유지 (필요한 경우)
plt.show()
