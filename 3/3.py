with open("3/test.txt", "r") as f:
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


