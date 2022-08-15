with open("25/test1.txt", "r") as f:
    lines = [ list(x) for x in f.read().splitlines()]

print(lines)
for line in lines:
    for i,col in enumerate(line):
        if col == ">" and line[(i+1) % len(line) ] ==".":
            col = "."
            line[(i+1) % len(line)] = ">"
print(lines)
