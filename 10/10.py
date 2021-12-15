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


for line in lines:
    stack = []
    for char in line:
        if char in opens:
            stack.append(char)
        elif char == pairs[stack[-1]]:
            stack.pop()
        else:
            print("Error, expected ", pairs[stack[-1]], " but instead found ", char)
            if char == ")":
                points += 3
            elif char == "]":
                points += 57
            elif char == "}":
                points += 1197
            elif char == ">":
                points += 25137
            break

print("Total points ", points)