import numpy as np
from numpy.core.fromnumeric import repeat
def calcFuel(start):
    return abs(start[0] - start[1])

from numpy.lib.function_base import median
with open("7/input.txt", "r") as f:
    numbers = [ int(x) for x in f.readline().split(",") ]

dest = np.median(numbers)

current = sum(map(calcFuel, [(x,dest) for x in numbers]))

while True:
    low = sum(map(calcFuel, [(x,dest-1) for x in numbers]))
    high = sum(map(calcFuel, [(x,dest+1) for x in numbers]))
    if low > current < high:
        print(int(current))
        break
    elif low < current:
        dest += 1
    elif high < current:
        dest -= 1
