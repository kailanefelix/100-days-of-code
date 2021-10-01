import numpy as np
import matplotlib.pyplot as plt

# Plotting a two-dimensional function

x = np.linspace(0, 5, 50) # 50 values in the interval [0,5]
y = np.linspace(0, 5, 50)[:, np.newaxis] # 50 values in the interval [0,5] in just one column
z = np.sin(x) ** 10 + np.cos(10 + y * x) * np.cos(x)

plt.imshow(z, origin='lower', extent=[0, 5, 0, 5], cmap='viridis')
plt.colorbar();