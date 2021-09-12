import numpy as np
import matplotlib.pyplot as plt




x = np.arange(0,50,1)
plt.plot(x, (np.sin(x)* np.sin(x))/(x+1))
plt.show()