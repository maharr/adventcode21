with open("3/input.txt", "r") as f:
    input = [ x for x in f.read().splitlines()]

count = [0] * len(input[0])

for i in input:
    for j,k in enumerate(i):
        if k == "1":
            count[j] += 1
        else:
            count[j] -= 1

output = ""
print(count)

for c in count:
    if c > 0:
        output += "1"
    else:
        output += "0"

gamma = int(output,2)
epsilon = gamma ^ ((2 ** len(input[0]))-1)

print("Power is =", gamma * epsilon)

filter =""
oldlist = input
for j in range(len(input[0])):
    newlist = []
    count = 0
    for i in oldlist:
        if i[j] == "0":
            count -= 1
        else:
            count += 1
    if count <0:
        filter += "0"
    else:
        filter += "1"


    newlist = [i for x,i in enumerate(oldlist) if i.startswith(filter)]
    if len(newlist) != 1:
        oldlist = newlist
    else:
        filter = newlist[0]
        break

    


oxygenrate = int(filter,2)  
print("Oxygen rate", oxygenrate)


filter =""
oldlist = input
for j in range(len(input[0])):
    newlist = []
    count = 0
    for i in oldlist:
        if i[j] == "0":
            count -= 1
        else:
            count += 1
    if count >=0:
        filter += "0"
    else:
        filter += "1"


    newlist = [i for x,i in enumerate(oldlist) if i.startswith(filter)]
    if len(newlist) != 1:
        oldlist = newlist
    else:
        filter = newlist[0]
        break


co2rate = int(filter,2)
print("CO2 rate", co2rate)

print("Support rating", co2rate * oxygenrate)
