import numpy as np
import matplotlib.pyplot as plt

x4 = np.random.uniform(0, 10, 100)
y4 = np.random.uniform(0, 10, 100)
colors = np.random.rand(100)
markers = ['o', 's', '^', 'd']

plt.figure()
for i in range(4):
    idx = np.arange(i, 100, 4)
    plt.scatter(x4[idx], y4[idx], color=np.random.rand(3,), marker=markers[i], label=f'Group {i+1}')
plt.title('Scatter Plot of Random Points')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.show()