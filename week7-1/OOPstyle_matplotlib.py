import matplotlib.pyplot as plt

'''
figure와 axes 객체 생성
'''
# Figure 객체 생성
fig = plt.figure()  # 전체 그림을 위한 Figure 객체를 생성함

# Axes 객체 추가
ax = fig.add_subplot(1, 1, 1)  # 1행 1열의 그리드에 첫 번째 Axes를 추가함

# ===============================================================

'''
plotting 데이터
ax 객체로 데이터를 plot 가능. plot()는 line graph 그릴 때 사용
'''
# 데이터 생성
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 40]

# 데이터를 플롯
ax.plot(x, y)  # Axes 객체의 plot() 메소드를 사용하여 데이터를 플롯함

# 그래프 표시
plt.show()  # 전체 Figure를 화면에 표시함

# ===========================================================

fig, ax = plt.subplots()  # Figure와 Axes 객체를 동시에 생성함

# 데이터 생성
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 40]

# 데이터를 플롯
ax.plot(x, y)  # 데이터를 플롯

# 그래프 표시
plt.show()  # 전체 Figure를 화면에 표시함

'''
집에서 일부 내용 추가(깃허브에서 자체적으로)
'''