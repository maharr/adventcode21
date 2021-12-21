from re import sub


with open("16/test.txt", "r") as f:
    lines = f.read().splitlines()

for line in lines:
    number = int(line,16)
    packet = str(bin(number))
    print(packet)
    version = int(packet[2:5],2)
    id = int(packet[5:8],2)
    message = packet[8:]
    if id == 4:
        sub_packet = ""
        for i in range(len(message)//5):
            start = (i * 5) + 1
            end = (i * 5) + 5
            sub_packet += message[start:end]
        print(int(sub_packet,2))
        
    print(version,id)
    print(sub_packet)


    