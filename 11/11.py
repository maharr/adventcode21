import numpy as np

def flash(x,y):
    for dx in range(-1,2):
        for dy in range(-1,2):
            if 0 <= x+dx < xmax and 0 <= y+dy < ymax and not (dy == 0 and dx == 0):
                if numbers[y+dy,x+dx] != 0:
                    numbers[y+dy,x+dx] += 1
                    
                    

with open("input.txt", "r") as f:
    input = [list(x) for x in f.read().splitlines()]

numbers = np.array(input,dtype=int)
ymax,xmax = numbers.shape
flashes = 0
i=0

while np.count_nonzero(numbers == 0) != 100:
    
    for y,row in enumerate(numbers):
        for x,val in enumerate(row):
            numbers[y,x]+=1
                
    while np.count_nonzero(numbers > 9) != 0:
        for y,row in enumerate(numbers):
            for x,val in enumerate(row):
                if val > 9:
                    numbers[y,x]= 0
                    flash(x,y)
    
    if i < 100:
        flashes += np.count_nonzero(numbers == 0)
        
    i += 1
            
        
print("Total number of flashes ",flashes)
print("First coordinated flash", i)
        

