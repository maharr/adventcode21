boards = []
with open("4/test.txt", "r") as f:
    calls = [ int(x) for x in f.readline().split(",") ]
    lines = f.read().splitlines()


print(calls)

for i in range(len(lines)/6):
    print(lines[i])





print(lines)