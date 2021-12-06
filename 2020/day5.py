with open('input_day5.txt', 'r') as f:
    boardingpasses = [l.strip() for l in f.readlines()]

def seatID(bp):
    row, column = '', ''
    for k in range(7):
        row += '1' * (bp[k] == 'B') + '0' * (bp[k] == 'F')
    for k in range(3):
        column += '1' * (bp[7 + k] == 'R') + '0' * (bp[7 + k] == 'L')
    return int(row, 2)*8 + int(column, 2)

##Part 1
# print(max([seatID(bp) for bp in boardingpasses]))

##Page 2

bpIDs = [seatID(bp) for bp in boardingpasses]
bpIDs.sort()

seat = bpIDs[0]
while seat in bpIDs:
    seat += 1
print(seat)