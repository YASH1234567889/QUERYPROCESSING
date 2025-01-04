
import numpy as np
import matplotlib.pyplot as plt


x = np.random.rand(50)
y = np.random.rand(50)  

plt.scatter(x, y, facecolors='none', edgecolors='blue')

plt.title("Scatter Plot with Empty Circles")
plt.xlabel("X Values")
plt.ylabel("Y Values")

plt.show()
