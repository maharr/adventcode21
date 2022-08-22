import re
regex = r"(on|off) x=(-?[0-9]+)\.\.(-?[0-9]+),y=(-?[0-9]+)\.\.(-?[0-9]+),z=(-?[0-9]+)\.\.(-?[0-9]+)"

with open("22/test3.txt", "r") as f:
    commands = [re.findall(regex,y) for y in f.read().splitlines()]

cell = {}

for line in commands:
    print(line)
    if int(line[0][1]) > 50 or int(line[0][2]) < -50 or int(line[0][3]) > 50 or int(line[0][4]) < -50 or int(line[0][5]) > 50 or int(line[0][6]) < -50:
        break
    
    for x in range(int(line[0][1]), int(line[0][2])+1):
        for y in range(int(line[0][3]), int(line[0][4])+1):
            for z in range(int(line[0][5]), int(line[0][6])+1):
                if -50 <= x <= 50 and -50 <= y <= 50 and -50 <= z <= 50:
                    cell[x,y,z] = line[0][0]

cubes_on = []
cubes_off = []

for line in commands:
    x = min(int(line[0][1]),int(line[0][2]))
    x1 = max(int(line[0][1]),int(line[0][2]))
    y = min(int(line[0][3]),int(line[0][4]))
    y1 = max(int(line[0][3]),int(line[0][4]))
    z = min(int(line[0][5]),int(line[0][6]))
    z1 = max(int(line[0][5]),int(line[0][6]))

    vol = (x1 - x) * (y1 - y) * (z1 - z)

    if line[0][0] == "on":
        cubes_on.append([vol,x,x1,y,y1,z,z1])
    else:
        cubes_off.append([-vol,x,x1,y,y1,z,z1])

print(len(cubes_on))
print(len(cubes_off))

counter = 0
for on in cubes_on:
    for off in cubes_off:
        x, x1, y, y1, z, z1 = on[1], on[2], on[3], on[4], on[5], on[6]
        a, a1, b, b1, c, c1 = off[1], off[2], off[3], off[4], off[5], off[6]
        vol = max(min(a1,x1)-max(a,x),0) * max(min(b1,y1)-max(b,y),0) * max(min(c1,z1)-max(c,z),0)
        if vol != 0: counter += 1
        print(counter, vol)

