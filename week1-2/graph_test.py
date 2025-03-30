import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,3,4])
y = np.array([10,20,25,30])

plt.plot(x, y)

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('simple plot')
plt.show()
