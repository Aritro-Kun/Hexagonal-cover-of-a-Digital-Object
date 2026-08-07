import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

y = np.array([[-.87,.5], [0,1], [.87,.5], [.87,-.5], [0,-1], [-.87,-.5]])

p = Polygon(y, facecolor = 'r',alpha=0.5, edgecolor='k')

fig,ax = plt.subplots()

ax.add_patch(p)
ax.set_xlim([-3,3])
ax.set_ylim([-3,3])
plt.show()
