import numpy as np

def checkadjacent(x,y,num):
    val = num[y,x]
    ymax,xmax = num.shape
    surround = []
    if x > 0:
        surround.append(num[y,x-1])
    if x < xmax-1:
        surround.append(num[y,x+1])
    if y > 0:
        surround.append(num[y-1,x])
    if y < ymax-1:
        surround.append(num[y+1,x])
    
    if val < min(surround):
        return x,y,int(val) + 1
    else:
        return x,y,0

def findbasin(x,y,num):
    val = int(num[y,x])
    ymax,xmax = num.shape
    if x > 0:
        if 9 > int(num[y,x-1]) > val:
            basinpoints.append((x-1,y))
            findbasin(x-1,y,num)
    if x < xmax-1:
        if 9 > int(num[y,x+1]) > val:
            basinpoints.append((x+1,y))
            findbasin(x+1,y,num)
    if y > 0:
        if 9 > int(num[y-1,x]) > val:
            basinpoints.append((x,y-1))
            findbasin(x,y-1,num)
    if y < ymax-1:
        if 9 > int(num[y+1,x]) > val:
            basinpoints.append((x,y+1))
            findbasin(x,y+1,num)
    

with open("9/input.txt", "r") as f:
    input = [list(x) for x in f.read().splitlines()]

numbers = np.array(input)

total = 0
basins  = []
basinpoints = []
basinsize = []

for i,line in enumerate(numbers):
    for j,col in enumerate(line):
        a,b,c = checkadjacent(j,i,numbers)
        if c > 0:
            total += c
            basins.append([a,b])

print("Total risk level ", total)

for basin in basins:
    findbasin(basin[0],basin[1],numbers)
    
    basinsize.append(len(list(set(basinpoints)))+1)
    basinpoints = []

b = np.array(basinsize)

a = np.argpartition(b, -3) [-3:]
print(np.prod(b[a]))

