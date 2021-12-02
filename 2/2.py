with open("2/input.txt", "r") as f:
    input = [ x.split() for x in f.read().splitlines()]


depth = 0
position = 0
aim = 0

for i in input:
    if i[0] == "forward":
        position += int(i[1])
    elif i[0] == "up":
        depth -= int(i[1])
    else:
        depth += int(i[1])

print("Depth is", depth * position)

depth = 0
position = 0
aim = 0

for i in input:
    if i[0] == "forward":
        position += int(i[1])
        depth += aim * int(i[1])
    elif i[0] == "up":
        aim -= int(i[1])
    else:
        aim += int(i[1])


print("Depth is", depth * position)