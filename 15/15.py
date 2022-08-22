from heapq import heappop, heappush

with open("15/input.txt", "r") as f:
    grid = [[int(y) for y in list(x)] for x in f.read().splitlines()]

height, width = len(grid), len(grid[0])



width5 , height5 = width*5, height*5


for i in 1,5:
    open_nodes = [(0,0,0)]
    closed_nodes = {(0,0)}
    directions = [[1,0], [0,1], [-1,0], [0,-1]]
    while open_nodes:
        #print(len(open_nodes), len(closed_nodes))
        current_node = heappop(open_nodes)
        current_distance = current_node[0]
        if current_node[1] == i * height-1 and current_node[2] == i * width-1:
            print(current_distance)
            break
        
        
        #print("cur ", current_node)

        for d in directions:
            x = current_node[1] + d[0]
            y = current_node[2] + d[1]
            if 0 <= x < width * i and 0 <= y < height * i  and (x,y) not in closed_nodes:
                #print(grid[y][x],x,y)
                dx, rx = divmod(x, width)
                dy, ry = divmod(y, height)
                
                score = (grid[ry][rx] + dx + dy - 1 ) % 9 +1
                heappush(open_nodes,(score + current_distance, x,y))
                closed_nodes.add((x,y))

