with open("16/test.txt", "r") as f:
    lines = f.read().splitlines()

for line in lines:
    number = int(line,16)
    packet = str(bin(number))
    print(packet)
    