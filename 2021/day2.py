import os
os.chdir("/home/cedric/Travail/AlgoInfo/CodesPython/adventofcode/2021/")

## Part 1 & 2
horizontal_position, depth, aim = 0, 0, 0

with open("input_day2.txt") as f:
    for instruction in f.readlines():
        direction, units = instruction.split()
        if direction == 'up':
            aim -= int(units)
        elif direction == 'down':
            aim += int(units)
        else:
            horizontal_position += int(units)
            depth += aim * int(units)

print(horizontal_position, depth, horizontal_position*depth)
    



