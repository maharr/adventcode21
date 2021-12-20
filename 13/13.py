import numpy as np
import re
with open("13/input.txt", "r") as f:
    input = [x for x in f.read().splitlines()]


points = np.array([[int(y) for y in x.split(",")] for x in input[:input.index("")]])
input = [x for x in input[input.index("")+1:]]


commands = []

for command in input:
    tmp = re.findall('.+(.)=([0-9]+)', command)
    commands.append(list(tmp[0]))

print(commands)

xmax, ymax = points.max(axis=0)
    
grid = np.zeros((ymax+1, xmax+1),dtype=int)

for p in points:
    grid[p[1]][p[0]] = 1

print(grid)


top, tmp, bottom = np.split(grid, [int(commands[0][1]),int(commands[0][1])+1],0)

print(top.shape)
print(tmp)
print(bottom.shape)

bottom_flip = np.flip(bottom,0)
print(bottom_flip)

print(np.count_nonzero(np.add(top, bottom_flip)))