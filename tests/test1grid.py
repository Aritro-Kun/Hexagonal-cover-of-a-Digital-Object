import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

fig,ax = plt.subplots()
for i in range(50):
    if i%2==0:
        x_offset=0
    else:
        x_offset=0.87
    for j in range(50):
        x=j*1.74+x_offset
        y=-i*1.5
        x1=np.array([[-50+x,49.5+y], [-49.13+x,50+y], [-48.26+x,49.5+y], [-48.26+x,48.5+y], [-49.13+x,48+y], [-50+x,48.5+y]])
        p1 = Polygon(x1, facecolor = 'r',alpha=0.1, edgecolor='k')
        ax.add_patch(p1)
ax.set_xlim([-10,10])
ax.set_ylim([-10,10])
plt.show()
