with open("10/input.txt", "r") as f:
    lines = f.read().splitlines()

opens = "{[(<"
pairs = {
    "(": ")",
    "{": "}",
    "[": "]",
    "<": ">"
}
points = 0
completed = []

for line in lines:
    stack = []
    complete = 0
    corrupted = False
    for char in line:
        if char in opens:
            stack.append(char)
        elif char == pairs[stack[-1]]:
            stack.pop()
        else:
            print("Error, expected ", pairs[stack[-1]], " but instead found ", char)
            corrupted = True
            if char == ")":
                points += 3
            elif char == "]":
                points += 57
            elif char == "}":
                points += 1197
            elif char == ">":
                points += 25137
            break
    if not corrupted:
        for i in range(len(stack),0, -1):
            val = stack.pop()
            complete *= 5
            if val == "(":
                complete += 1
            elif val == "[":
                complete += 2
            elif val == "{":
                complete += 3
            elif val == "<":
                complete += 4
        completed.append(complete)

print("Total points ", points)
print("Total completion points ", sorted(completed)[len(completed)//2])