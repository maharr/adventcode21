from heapq import heappop, heappush
import time

with open("15/input.txt", "r") as f:
    grid = [[int(y) for y in list(x)] for x in f.read().splitlines()]

height, width = len(grid), len(grid[0])
start = time.perf_counter()

for i in 1,5:
    open_nodes = [(0,0,0)]
    closed_nodes = {(0,0)}
    directions = [[1,0], [0,1], [-1,0], [0,-1]]
    while open_nodes:
        current_node = heappop(open_nodes)
        current_distance = current_node[0]
        if current_node[1] == i * height-1 and current_node[2] == i * width-1:
            print(current_distance)
            print(f"Processing time for Q{i}, {time.perf_counter() - start:0.4f} seconds")
            break
        
        for d in directions:
            x = current_node[1] + d[0]
            y = current_node[2] + d[1]
            if 0 <= x < width * i and 0 <= y < height * i  and (x,y) not in closed_nodes:
                dx, rx = divmod(x, width)
                dy, ry = divmod(y, height)
                score = (grid[ry][rx] + dx + dy - 1 ) % 9 +1
                heappush(open_nodes,(score + current_distance, x,y))
                closed_nodes.add((x,y))