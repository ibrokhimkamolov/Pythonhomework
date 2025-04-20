import numpy as np
import matplotlib.pyplot as plt

time_periods = ['T1', 'T2', 'T3', 'T4']
category_a = np.array([10, 20, 30, 40])
category_b = np.array([15, 25, 35, 20])
category_c = np.array([5, 10, 15, 25])

plt.figure()
plt.bar(time_periods, category_a, label='Category A', color='blue')
plt.bar(time_periods, category_b, bottom=category_a, label='Category B', color='green')
plt.bar(time_periods, category_c, bottom=category_a+category_b, label='Category C', color='red')
plt.title('Stacked Bar Chart by Category Over Time')
plt.xlabel('Time Period')
plt.ylabel('Value')
plt.legend()
plt.grid(True, axis='y')
plt.show()