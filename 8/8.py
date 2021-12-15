with open("8/test.txt", "r") as f:
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
        else: # number 0, 2, 3, 5, 6, 9
            pass

print("Total ", count)



for line in lines:
    seg = ["abcdefg"] * 7
    for i in range(0,10):
        print(seg)
        if len(line[i]) == 2: # number 1
            seg[3] = line[i]
            seg[6] = line[i]
        elif len(line[i]) == 4: # number 4
            pass
        elif len(line[i]) == 3: # number 7
            pass
        elif len(line[i]) == 7: # number 8
            pass
        else: # number 0, 2, 3, 5, 6, 9
            pass

