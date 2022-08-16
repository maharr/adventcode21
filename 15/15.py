with open("15/input.txt", "r") as f:
    grid = [[int(y) for y in list(x)] for x in f.read().splitlines()]

for line in grid:
    print(*line)

height = len(grid)
width = len(grid[0])    

print(height,width)

open_nodes = [[0,[0,0]]]
closed_nodes = set()
directions = [[1,0], [0,1], [-1,0], [0,-1]]



while True:
    if not(open_nodes):
        break

    current_node = open_nodes.pop(0)
    current_distance = current_node[0]
    if current_node[1] == [height-1,width-1]:
        print(current_distance)
        break
    
    closed_nodes.add((current_node[1][0],current_node[1][1]))
    #print("cur ", current_node)

    for d in directions:
        x = current_node[1][0] + d[0]
        y = current_node[1][1] + d[1]
        if 0 <= x < width and 0 <= y < height and (x,y) not in closed_nodes:
            #print(grid[y][x],x,y)
            open_nodes.append([grid[y][x] + current_distance, [x,y]])
    open_nodes = sorted(open_nodes)
    if current_distance == 40:
        pass
        #print("open ", open_nodes)
        #print("close ",closed_nodes)
    
        #print(current_distance)

#print(open_nodes)
#print(closed_nodes)


