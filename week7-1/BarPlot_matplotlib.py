import matplotlib.pyplot as plt

# 데이터 준비
categories = ['A', 'B', 'C', 'D', 'E']
values = [5, 7, 3, 8, 4]

# 막대 그래프 생성 (Create bar plot)
plt.bar(categories, values)

# 그래프 제목 추가 (Add title)
plt.title('Simple Bar Plot')

# x축, y축 레이블 추가 (Add x and y axis labels)
plt.xlabel('Categories')
plt.ylabel('Values')

# 그래프 출력 (Display plot)
plt.show()