# libraries
import matplotlib.pyplot as plt
import numpy as np
x = np.random.rand(20)
y = np.random.rand(20)
z = np.random.rand(20)
plt.scatter(x, y, s=z * 1000, alpha=0.5)
plt.show()
