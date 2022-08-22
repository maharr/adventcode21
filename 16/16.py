from re import sub

with open("16/test.txt", "r") as f:
    lines = f.read().splitlines()

for line in lines:
    number = int(line,16)
    packet = format(number, f'#0{(len(line)*4)+2}b')
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
    else:
        if message[0:1] == "0":
            length = int(message[1:16],2)
            print("Length ", length)
            sub_packet += message[16:]
            print("Sub Packet ", sub_packet)
            # 15 bits
        else:
            num_packets = message[1:12]
            print("Num Packets ", num_packets)
            sub_packet += message[12:]
            print("Sub Packet", sub_packet)
            #11 bits

        
    print(version,id)
    print(sub_packet)


    