import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(1,1,1) # make a blank plotting area
# fig, ax = plt.subplots()  # ax를 포함하고 있는 fig를 반환. 위의 두 line을 한번에 처리.

print('fig.axes:', fig.axes)   # fig.axes는 list임. (Figure는 복수 개의 Axes를 가질 수 있음)
print('ax.figure:', ax.figure) # ax 는 Axes의 instance임.
print('ax.xaxis:', ax.xaxis)
print('ax.yaxis:', ax.yaxis)
print('ax.xaxis.axes:', ax.xaxis.axes)
print('ax.yaxis.axes:', ax.yaxis.axes)
print('ax.xaxis.figure:', ax.xaxis.figure)
print('ax.yaxis.figure:', ax.yaxis.figure)
