import os
os.chdir("/home/cedric/Travail/AlgoInfo/CodesPython/adventofcode/2021/")

## Part 1 & 2


# digits = 12 * [0]
# f = open("input_day3.txt")
#
# length = 0
# binary = f.readline().strip()
# while binary != '':
#     for i in range(len(binary)):
#         digits[i] += int(binary[i])
#     binary = f.readline().strip()
#     length += 1
# f.close()
#
# gamma = ''
# for d in digits:
#     if d < length/2:
#         gamma += '0'
#     else:
#         gamma += '1'
#
# print(int(gamma, 2) * (2**12 -1 - int(gamma, 2)))

## Part 2
with open("input_day3.txt") as f:
    binary_numbers = [b.strip() for b in f.readlines()]

# binary_numbers = ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010']

def most_common_bit(bn_list, pos):
    length = len(bn_list)
    if sum([int(x[pos]) for x in bn_list]) >= length/2:
        return '1'
    else:
        return '0'

pos = 0
mcb = most_common_bit(binary_numbers, pos)
oxygen = [bn for bn in binary_numbers if bn[pos] == mcb]
while len(oxygen) > 1:
    pos += 1
    mcb = most_common_bit(oxygen, pos)
    oxygen = [bn for bn in oxygen if bn[pos] == mcb]

pos = 0
mcb = most_common_bit(binary_numbers, pos)
co2 = [bn for bn in binary_numbers if bn[pos] != mcb]
while len(co2) > 1:
    pos += 1
    mcb = most_common_bit(co2, pos)
    co2 = [bn for bn in co2 if bn[pos] != mcb]

print(int(oxygen[0], 2) * int(co2[0], 2))


