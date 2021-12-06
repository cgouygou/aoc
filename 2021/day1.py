import os
os.chdir("/home/cedric/Travail/AlgoInfo/CodesPython/adventofcode/2021/")

## Part 1
with open("input_day1_1.txt") as f:
    measurements = [int(m) for m in f.readlines()]

data_str = open('input1.txt').read().splitlines()
# increases = 0
# for i in range(1, len(measurements)):
#     if measurements[i] > measurements[i-1]:
#         increases += 1
# 
# print(increases)

## Part 2

increases = 0

windows = [measurements[i-1] + measurements[i] + measurements[i+1] for i in range(1, len(measurements) - 1)]
for i in range(1, len(windows)):
    if windows[i] > windows[i-1]:
        increases += 1

print(increases)
