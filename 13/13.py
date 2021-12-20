import numpy as np
import re
import colorama
with open("13/input.txt", "r") as f:
    input = [x for x in f.read().splitlines()]

points = np.array([[int(y) for y in x.split(",")] for x in input[:input.index("")]])
input = [x for x in input[input.index("")+1:]]

commands = []

for command in input:
    tmp = re.findall('.+(.)=([0-9]+)', command)
    dir, val = list(tmp[0])
    print(dir,val)
    commands.append([dir,int(val)])

xmax, ymax = points.max(axis=0)
    
grid = np.zeros((ymax+1, xmax+1),dtype=int)

for p in points:
    grid[p[1]][p[0]] = 1


for command in commands:
    if command[0] == "y":
        top, tmp, bottom = np.split(grid, [command[1], command[1]+1], 0)
        bottom = np.flip(bottom,0)
        if len (top) > len (bottom):
            bottom = np.pad(bottom, [(0,len(top) - len(bottom)),(0,0)],mode='constant')
        elif len(top) < len(bottom):
            top = np.pad(top, [(len(bottom) - len(top),0),(0,0)],mode='constant')
        
            
        grid = np.add(top, bottom)
    if command[0] == "x":
        top, tmp, bottom = np.split(grid, [command[1], command[1]+1], 1)
        bottom = np.flip(bottom,1)
        if len (top[0]) > len (bottom[0]):
            bottom = np.pad(bottom, [(0,0),(0,len(top[0]) - len(bottom[0]))],mode='constant')
        elif len(top[0]) < len(bottom[0]):
            top = np.pad(top, [(0,0),(len(bottom[0]) - len(top[0]),0)],mode='constant')
        
            
        grid = np.add(top, bottom)

np.set_printoptions(linewidth=400)
print(grid)

grid[grid > 0] = 9



print(np.count_nonzero(grid))

def color_sign(x):
    c = colorama.Fore.GREEN if x > 0 else colorama.Fore.RED
    return f'{c}{x}'

np.set_printoptions(formatter={'int': color_sign})

print(grid)