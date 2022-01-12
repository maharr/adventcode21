from collections import Counter

with open("test.txt", "r") as f:
    template = f.readline().strip()
    next(f)
    lines = [ x.split("->") for x in f.read().splitlines()]
    
rules = {}

for line in lines:
    rules[line[0].strip()] = line[1].strip()
    

rounds = 10

for i in range(rounds):
    temp = template[0]
    for j in range(len(template)-1):
        # print(template[j],rules[template[j:j+2]],template[j+1])
        temp += rules[template[j:j+2]] + template[j+1]
    template = temp
    print(i)
    
t = Counter(template)

mostcommon = int(t.most_common()[0:][0][1])
leastcommon = int(t.most_common()[-1:][0][1])

print(mostcommon-leastcommon)

    


        
