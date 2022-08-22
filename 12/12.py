from tracemalloc import start


with open("12/test.txt", "r") as f:
    maps = [[y for y in x.split("-")] for x in f.read().splitlines()]

def find_routes(location):
    result = []
    for line in maps:
        if line[0] == location :
            result.append(line[1])
        elif line[1] == location :
            result.append(line[0])
    return result



finished = False
location = start
paths = [['start']]
completed = 0

while not finished:
    newpaths = []

    for path in paths:
        print(path[-1])
        steps = find_routes(path[-1])
        for step in steps:
            if step not in path or step.isupper() :
                
                newpath = path.copy()
                newpath.append(step)
                newpaths.append(newpath.copy())
    
    print(newpath)
                

    break


