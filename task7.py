import numpy as np
import matplotlib.pyplot as plt




x = np.arange(1, 9)             #По x
y=np.array([5,4,2,7,0,3,3,4])   #По у   
fig, ax = plt.subplots()
ax.bar(x, y)


fig.set_figwidth(8)             #  ширина и
fig.set_figheight(8)            #  высота "Figure"
fig.set_facecolor('floralwhite')


plt.show()