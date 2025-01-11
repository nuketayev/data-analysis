import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = np.arange(-10,11)

plt.figure(figsize=(12, 6))

plt.title('The plot')
plt.plot(x, x**2)
plt.plot(x, -1 * (x**2))
plt.show()

plt.subplot(1,2,1)