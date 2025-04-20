import numpy as np
import matplotlib.pyplot as plt

x2 = np.linspace(0, 2 * np.pi, 400)
plt.figure()
plt.plot(x2, np.sin(x2), 'r--o', label='sin(x)')
plt.plot(x2, np.cos(x2), 'g-x', label='cos(x)')
plt.title('Sine and Cosine Functions')
plt.xlabel('x')
plt.ylabel('Value')
plt.legend()
plt.grid(True)
plt.show()