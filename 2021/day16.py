import os
os.chdir("/media/cedric/CLECGOUYGOU/Travail/AlgoInfo/CodesPython/adventofcode/aoc/2021/")

data_str = open("input_day16.txt").read().splitlines()

bits = "".join([bin(int(hexa, 16))[2:] for hexa in data_str[0]])

p = '110100101111111000101000'
p = '00111000000000000110111101000101001010010001001000000000'
p = '11101110000000001101010000001100100000100011000001100000'
def scan(packet):
    version = int(packet[:3], 2)
    typeID = int(packet[3:6], 2)
    groups = []
    if typeID == 4:
        k = 0
        while packet[6+5*k] != '0':
            groups.append(packet[6+5*k+1:6+5*k+5])
            k += 1
        groups.append(packet[6+5*k+1:6+5*k+5])
        zeros = 4 - (6+5*(k+1))%4
        next_start = 6+5*(k+1) + zeros
    else:
        length_type_ID = packet[6]
        if length_type_ID == '0':
            length_subpackets = int(packet[7:22])
            zeros = 4 - (22+length_subpackets)%4
            next_start = 22+length_subpackets + zeros
            groups = ['1']
        else:
            nb_subpackets = int(packet[7:18], 2)
            for k in range(nb_subpackets):
                groups.append(int(packet[18+11*k:18+11*(k+1)], 2))
            zeros = 4 - (18 + 11*nb_subpackets)%4
            next_start = 18 + 11*nb_subpackets + zeros

    return version,  groups, packet[next_start:]