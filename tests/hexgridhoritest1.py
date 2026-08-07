import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import math

size = int(input("Enter side of hexagons in grid: "))
xplotlimn = int(input("negative x-axis limit: "))
xplotlimp = int(input("positive x-axis limit: "))
yplotlimn = int(input("negative y-axis limit: "))
yplotlimp = int(input("positive y-axis limit: "))
circrad = size
inrad = (math.sqrt(3)/2)*(circrad)

#starting with left most possible point along y=0 as centre of first hexagon
x,y=xplotlimn+inrad+5,0
deg30 = math.pi/6
deg60 = math.pi/3
fig, plane = plt.subplots()
plane.set_xlim([xplotlimn, xplotlimp])
plane.set_ylim([yplotlimn, yplotlimp])
while(x<=xplotlimp-inrad):
    coords = []
    for i in range(6):
        temp = []
        x0 = x + circrad*(math.cos(deg30 + (i*deg60)))
        y0 = y + circrad*(math.sin(deg30 + (i*deg60)))
        temp.append(x0)
        temp.append(y0)
        coords.append(temp)
    hexa = Polygon(coords, edgecolor='0', facecolor='1')
    plane.add_patch(hexa)
    x+=(2*inrad)

plt.show()
