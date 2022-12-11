import os
os.chdir('/home/cedric/Travail/AlgoInfo/CodesPython/adventofcode/aoc/2022/')

data = open("input_day10.txt").read().splitlines()

## Part I
X = 1
cycles = []

for instruction in data:
    cycles.append(X)
    if instruction != 'noop':
        cycles.append(X)
        X += int(instruction.split()[-1])

# print(sum([(k+1) * cycles[k] for k in range(len(cycles)) if k%40 == 19]))

## Part II
crt = ''
for X in cycles:
    if abs(X - len(crt)%40) <= 1:
        crt += '#'
    else:
        crt += '.'

for line in range(6):
    print(crt[40*line:40*(line+1)])