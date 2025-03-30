import matplotlib.pyplot as plt

# 데이터 준비
x = [1,2,3,4,5]
y = [1,2,3,4,5]

# Figure & Axes 객체 생성
fig, ax = plt.subplots()

# 그래프 생성
line, = ax.plot(x, y, 'r-') # 'r-'는 red solid line 의미

# 그래프 제목 추가
ax.set_title('simple line plot')

# X,y 축 레이블 추가
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')

# 그래프 출력
plt.show()

# https://share.note.sx/files/pn/pntl6ki8n3osn2cb1jbg.png
