from collections import Counter

with open("14/input.txt", "r") as f:
    template = f.readline().strip()
    next(f)
    lines = [ x.split("->") for x in f.read().splitlines()]
    
rules = {}

for line in lines:
    rules[line[0].strip()] = line[1].strip()
    

rounds = 10

polymer = template

for i in range(rounds):
    temp = polymer[0]
    for j in range(len(polymer)-1):
        temp += rules[polymer[j:j+2]] + polymer[j+1]
    polymer = temp

t = Counter(polymer)

mostcommon = int(t.most_common()[0:][0][1])
leastcommon = int(t.most_common()[-1:][0][1])

print("Q1 answer ", mostcommon-leastcommon)

pairs = rules.copy()

for key,val in pairs.items():
    pairs[key] = 0

print(rules)
print(pairs)

for j in range(len(template)-1):
    pairs[template[j:j+2]] += 1

rounds = 40    

for i in range(rounds):
    new_pairs = rules.copy()
    for key,val in new_pairs.items():
        new_pairs[key] = 0
    for pair,no in pairs.items():
        if no != 0:
            new_pairs[pair[0] + rules[pair]] += no
            new_pairs[rules[pair] + pair[1]] += no
    pairs = new_pairs.copy()

print(pairs)

lettersfront = {}
lettersback = {}

for key,val in pairs.items():
    if key[0] in lettersfront:
        lettersfront[key[0]] += val
    else:
        lettersfront[key[0]] = val
    if key[1] in lettersback:
        lettersback[key[1]] += val
    else:
        lettersback[key[1]] = val

for key,val in lettersfront.items():
    lettersfront[key] = max(val, lettersback[key])

print(lettersfront,lettersback)

mini = min(lettersfront, key=lettersfront.get)
maxi = max(lettersfront, key=lettersfront.get)

print(lettersfront[maxi] - lettersfront[mini])