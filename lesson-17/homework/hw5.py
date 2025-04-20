import numpy as np
import matplotlib.pyplot as plt

data5 = np.random.normal(0, 1, 1000)

plt.figure()
plt.hist(data5, bins=30, alpha=0.7, color='blue', edgecolor='black')
plt.title('Histogram of Normally Distributed Data')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()