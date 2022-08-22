import time

with open("12/input.txt", "r") as f:
    maps = [[y for y in x.split("-")] for x in f.read().splitlines()]

def find_routes(location):
    result = []
    for line in maps:
        if line[0] == location :
            result.append(line[1])
        elif line[1] == location :
            result.append(line[0])
    return result

start = time.perf_counter()
finished = False
paths = [['start']]
completed = 0

while not finished:
    if not paths:
        break 
    current_path = paths.pop()
    steps = find_routes(current_path[-1])
    for step in steps:
        if step not in current_path or step.isupper() :
            if step != 'end':
                newpath = current_path.copy()
                newpath.append(step)
                paths.append(newpath.copy())
            else:
                completed += 1

print(completed, " total routes")
print(f"Processing time for part 1, {time.perf_counter() - start:0.4f} seconds")


finished = False
paths = [['start']]
completed2 = 0

def check_visit(next, path):
    if step.isupper():
        return True
    lower_path = [x for x in path if x.islower()]
    if len(lower_path) <= len(set(lower_path)) + 1 and step != "start":
        return True
    return False

while not finished:
    if not paths:
        break 
    current_path = paths.pop()
    steps = find_routes(current_path[-1])
    for step in steps:
        if check_visit(step, current_path) :
            if step != 'end':
                newpath = current_path.copy()
                newpath.append(step)
                paths.append(newpath.copy())
            else:
                completed2 += 1
    

print(completed2, " total routes")
print(f"Processing time for part 2, {time.perf_counter() - start:0.4f} seconds")


