import numpy as np
import re

with open("5/input.txt", "r") as f:
    lines = f.read().splitlines()

xmax= 0
ymax = 0
for line in lines:
    x1,y1,x2,y2 = [ int(x) for x in re.findall(r'\d+', line)]
    if max(x1,x2)>xmax:
        xmax = max(x1,x2)
    if max(y1,y2)>ymax:
        ymax = max(y1,y2)


points = np.empty((xmax+1,ymax+1))

for line in lines:
    x1,y1,x2,y2 = [ int(x) for x in re.findall(r'\d+', line)]
    xstep = 0
    ystep = 0
    if x1 < x2:
        xstep = 1
    else:
        xstep = -1
    if y1 < y2:
        ystep = 1
    else:
        ystep = -1
    x = range(x1,x2+xstep,xstep)
    y = range(y1,y2+ystep,ystep)
    if x1 == x2:
        for i in y:
            points[x1,i] += 1
    elif y1 == y2:
        for i in x:
            points[i,y1] += 1
    else:
        for j,i in enumerate(x):
            points[i,y[j]] += 1
        


print(np.count_nonzero(points >= 2))
print(points)

        