import numpy as np
def calcFuel(start):
    return abs(start[0] - start[1])

def calcFuelTri(start):
    dist = abs(start[0] - start[1])
    return ((dist**2)+dist)/2

with open("7/input.txt", "r") as f:
    numbers = [ int(x) for x in f.readline().split(",") ]

dest = np.median(numbers)

current = sum(map(calcFuel, [(x,dest) for x in numbers]))
print("First fuel usage ", int(current))
current = sum(map(calcFuelTri, [(x,dest) for x in numbers]))

while True:
    low = sum(map(calcFuelTri, [(x,dest-1) for x in numbers]))
    current = sum(map(calcFuelTri, [(x,dest) for x in numbers]))
    high = sum(map(calcFuelTri, [(x,dest+1) for x in numbers]))
    if low > current < high:
        break
    elif low < current:
        dest -= 1
    elif high < current:
        dest += 1

print("Second fuel usage ", int(current))
