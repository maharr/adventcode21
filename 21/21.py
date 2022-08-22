with open("21/input.txt", "r") as f:
    lines = f.read().splitlines()

p1 = [int(lines[0][-1]),0]
p2 = [int(lines[1][-1]),0]
playing = "p1"
die = 1

print(p1,p2)

play = True

while play:
    move = ((die-1%100 + (die)%100 + (die+1)%100) % 10) + 3
    if playing == "p1":
        p1[0] = ((p1[0] + move - 1) % 10) +1
        p1[1] += p1[0]
        if p1[1] >= 1000:
            play = False
        playing = "p2"
    else:
        p2[0] = ((p2[0] + move - 1) % 10) +1
        p2[1] += p2[0]
        if p2[1] >= 1000:
            play = False
        playing = "p1"
    
    die += 3

print(min(p1[1],p2[1])* (die-1))