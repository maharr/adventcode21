import os
print(os.getcwd())
with open("1/input.txt", "r") as f:
    input = [int(x) for x in f.read().splitlines()]

count = 0

for i in range(len(input)-1):
    if input[i] < input[i+1]:
        count += 1

print(count)

count2 = 0

for i in range(len(input)-1):
    if sum(input[i:i+3]) < sum(input[i+1:i+4]):
        count2 += 1
print(count2)