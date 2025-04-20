import numpy as np
import matplotlib.pyplot as plt

x3 = np.linspace(-5, 5, 400)
x3_log = np.linspace(0, 5, 400)

fig, axs = plt.subplots(2, 2, figsize=(10, 8))
axs[0, 0].plot(x3, x3**3, color='blue')
axs[0, 0].set_title('f(x) = x³')
axs[0, 0].set_xlabel('x')
axs[0, 0].set_ylabel('f(x)')

axs[0, 1].plot(x3, np.sin(x3), color='red')
axs[0, 1].set_title('f(x) = sin(x)')
axs[0, 1].set_xlabel('x')
axs[0, 1].set_ylabel('f(x)')

axs[1, 0].plot(x3, np.exp(x3), color='green')
axs[1, 0].set_title('f(x) = e^x')
axs[1, 0].set_xlabel('x')
axs[1, 0].set_ylabel('f(x)')

axs[1, 1].plot(x3_log, np.log(x3_log + 1), color='purple')
axs[1, 1].set_title('f(x) = log(x+1)')
axs[1, 1].set_xlabel('x')
axs[1, 1].set_ylabel('f(x)')

plt.tight_layout()
plt.show()