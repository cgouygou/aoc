import os
os.chdir("/home/cedric/Travail/AlgoInfo/CodesPython/adventofcode/aoc/2021/")

data_str = open("input_day13.txt").read().splitlines()

## Parsing
dots = [1311*['.'] for _ in range(895)]
maxx, maxy = 0, 0
i = 0
while data_str[i] != '':
    x, y = tuple(map(int, data_str[i].split(',')))
    dots[y][x] = '#'
    i += 1

fold_instructions = []
for k in range(i+1, len(data_str)):
    line = data_str[k].split('=')
    fold_instructions.append((line[0][-1], int(line[1])))

## Folding functions
def overlap(pos1, pos2):
    if '#' in [pos1, pos2]:
        return '#'
    else:
        return  '.'

def fold(paper, axis):
    new_paper = []
    if axis == 'x':
        for line in paper:
            new_paper.append([overlap(line[i], line[-(i+1)]) for i in range(len(line)//2)])
    else:
        for i in range(len(paper)//2):
            new_paper.append([overlap(paper[i][j], paper[-(i+1)][j]) for j in range(len(paper[0]))])
    return new_paper


## Part 1
# dots = fold(dots, fold_instructions[0][0])
# print(sum([l.count('#') for l in dots]))

## Part 2

for instruction in fold_instructions:
    dots = fold(dots, instruction[0])

for line in dots:
    print("".join(line))