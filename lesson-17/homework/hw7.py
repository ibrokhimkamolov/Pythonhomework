import numpy as np
import matplotlib.pyplot as plt

products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
sales = [200, 150, 250, 175, 225]
colors = ['red', 'blue', 'green', 'orange', 'purple']

plt.figure()
plt.bar(products, sales, color=colors)
plt.title('Sales Data for Products')
plt.xlabel('Product')
plt.ylabel('Sales')
plt.grid(True, axis='y')
plt.show()