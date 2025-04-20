import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x6 = np.linspace(-5, 5, 100)
y6 = np.linspace(-5, 5, 100)
X6, Y6 = np.meshgrid(x6, y6)
Z6 = np.cos(X6**2 + Y6**2)

surf = ax.plot_surface(X6, Y6, Z6, cmap='viridis')
fig.colorbar(surf)
ax.set_title('3D Surface Plot: f(x, y) = cos(x² + y²)')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('f(x, y)')
plt.show()