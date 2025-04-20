import numpy as np
import matplotlib.pyplot as plt

x1 = np.linspace(-10, 10, 400)
y1 = x1**2 - 4*x1 + 4

plt.figure()
plt.plot(x1, y1, color='blue')
plt.title('Plot of f(x) = x² - 4x + 4')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.show()