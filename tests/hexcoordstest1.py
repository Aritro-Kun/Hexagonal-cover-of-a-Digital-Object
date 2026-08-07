import math

size = int(input("Enter side of hexagons in grid: "))
circrad = size
inrad = (math.sqrt(3)/2)*(circrad)

#starting with origin as centre of hexagon
x,y=0,0
deg30 = math.pi/6
deg60 = math.pi/3
coords = []
for i in range(6):
    temp = []
    x0 = x + circrad*(math.cos(deg30 + (i*deg60)))
    y0 = y + circrad*(math.sin(deg30 + (i*deg60)))
    temp.append(x0)
    temp.append(y0)
    coords.append(temp)

print(coords)
