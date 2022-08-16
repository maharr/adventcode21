from heapq import heappop, heappush

with open("15/input.txt", "r") as f:
    grid = [[int(y) for y in list(x)] for x in f.read().splitlines()]

height, width = len(grid), len(grid[0])

open_nodes = [(0,0,0)]
closed_nodes = {(0,0)}
directions = [[1,0], [0,1], [-1,0], [0,-1]]

while open_nodes:
    #print(len(open_nodes), len(closed_nodes))
    current_node = heappop(open_nodes)
    current_distance = current_node[0]
    if current_node[1] == height-1 and current_node[2] == width-1:
        print(current_distance)
        break
    
    
    #print("cur ", current_node)

    for d in directions:
        x = current_node[1] + d[0]
        y = current_node[2] + d[1]
        if 0 <= x < width and 0 <= y < height and (x,y) not in closed_nodes:
            #print(grid[y][x],x,y)
            heappush(open_nodes,(grid[y][x] + current_distance, x,y))
            closed_nodes.add((current_node[1],current_node[2]))

