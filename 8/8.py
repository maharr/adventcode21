with open("8/input.txt", "r") as f:
    lines = [x.split() for x in f.readlines()]

count = 0

for line in lines:
    for i in range(11,15):
        if len(line[i]) == 2: # number 1
            count +=1
        elif len(line[i]) == 4: # number 4
            count += 1
        elif len(line[i]) == 3: # number 7
            count += 1
        elif len(line[i]) == 7: # number 8
            count += 1

print("Total ", count)

