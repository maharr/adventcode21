with open("25/input.txt", "r") as f:
    lines = [ list(x) for x in f.read().splitlines()]

#for row in lines:
#    print(*row, sep="\t")

#print(len(lines[0]))

counter = 0

while True:
    counter += 1
    change = False
    new_grid = [["." for x in range(len(lines[0]))] for y in range(len(lines))]

    for i,line in enumerate(lines):
        for j,col in enumerate(line):
            next_col = (j+1) % len(line)

            if col == ">":
                if line[next_col] == ".":
                    new_grid[i][next_col] = ">"
                else:
                    new_grid[i][j] = ">"
            
            if col == "v":
                new_grid[i][j] = "v"

    if lines == new_grid:
        change = True

    lines = new_grid.copy()

    new_grid = [["." for x in range(len(lines[0]))] for y in range(len(lines))]

    for i,line in enumerate(lines):
        for j,col in enumerate(line):
            next_row = (i+1) % len(lines)

            if col == 'v':
                if lines[next_row][j] == ".":
                    new_grid[next_row][j] = "v"
                else:
                    new_grid[i][j] = "v"
            
            if col == ">":
                new_grid[i][j] = ">"

    if lines == new_grid:
        if change:
            change = True
        else:
            change = False

    lines = new_grid.copy()


    #for row in new_grid:
        #print(*row, sep="\t")

    if change:
        break
    

    #input("Press enter for next iteration " + str(counter))

print(counter)
