import re
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
        else: # number 0, 2, 3, 5, 6, 9
            pass

print("Total ", count)

def convertbin(commands):
    sum = 0
    vals = sorted(list(commands))
    for v in vals:
        if v == 'a':
            sum += 1
        elif v == 'b':
            sum += 2
        elif v == 'c':
            sum += 4
        elif v == 'd':
            sum += 8
        elif v == 'e':
            sum += 16
        elif v == 'f':
            sum += 32
        elif v == 'g':
            sum += 64
    return sum

def convertoutput(command, seg):
    sums = 0
    vals = sorted(list(command))
    for v in vals:
        sum = 0
        if v == 'a':
            sum += 1
        elif v == 'b':
            sum += 2
        elif v == 'c':
            sum += 4
        elif v == 'd':
            sum += 8
        elif v == 'e':
            sum += 16
        elif v == 'f':
            sum += 32
        elif v == 'g':
            sum += 64
        for i,s in enumerate(seg):
            if sum == s:
                sums += 2**i


    return sums

total = 0
for line in lines:
    seg = [0] * 7

    # find top seg
    for i in range(0,10):
        if len(line[i]) == 2: # number 1
            seg[2] = convertbin(line[i])
            seg[5] = convertbin(line[i])
    for i in range(0,10):
        if len(line[i]) == 3: # number 7
            seg[0] = convertbin(line[i]) ^ seg[2]
    for i in range(0,10):    
        if len(line[i]) == 4: # number 4
            seg[1] = convertbin(line[i]) ^ seg[2]
            seg[3] = convertbin(line[i]) ^ seg[2]
    seg[4] = (seg[0] | seg[1] | seg[2]) ^ 127
    seg[6] = (seg[0] | seg[1] | seg[2]) ^ 127

    tmp = []
    for i in range(0,10): 
        if len(line[i]) == 5: # 2,3 or 5
            tmp.append(convertbin(line[i]))
    
    tmp1 = (tmp[0] & tmp[1] & tmp[2]) - seg[0]

    seg[3] = seg[3] & tmp1
    seg[6] = seg[6] & tmp1
    seg[1] = seg[1] ^ seg[3]
    seg[4] = seg[4] ^ seg[6]

    tmp = []
    for i in range(0,10): 
        if len(line[i]) == 6: # 0,6 or 9
            tmp.append(convertbin(line[i]))
    
    tmp1 = (tmp[0] & tmp[1] & tmp[2]) + seg[3] + seg[4]
    seg[2] = tmp1 ^ 127
    seg[5] = seg[5] ^ seg[2]

    output = 0
    for i in range(11,15):
        tmp = convertoutput(line[i],seg)
        output = output*10
        if tmp == 119:
            output += 0
        elif tmp == 36:
            output += 1
        elif tmp == 93:
            output += 2
        elif tmp == 109:
            output += 3
        elif tmp == 46:
            output += 4
        elif tmp == 107:
            output += 5
        elif tmp == 123:
            output += 6
        elif tmp == 37:
            output += 7
        elif tmp == 127:
            output += 8
        elif tmp == 111:
            output += 9
    
    total += output

print("Total Values ", total)
    
    
            

