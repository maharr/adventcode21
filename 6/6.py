import numpy as np
with open("6/input.txt", "r") as f:
    fish = [ int(x) for x in f.readline().split(",") ]

timer = np.zeros(9,dtype=int)
print(timer)

for f in fish:
    timer[f] += 1

for day in range(256):
    tmp = timer[0]
    for t in range(len(timer)-1):
        timer[t] = timer[t+1]        

    timer[6] += tmp
    timer[8] = tmp
    
print(timer)
print(sum(timer))