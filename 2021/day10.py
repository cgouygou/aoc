import os
os.chdir("/media/cedric/CLECGOUYGOU/Travail/AlgoInfo/CodesPython/adventofcode/aoc/2021/")

data_str = open("input_day10.txt").read().splitlines()

open_chr = '([{<'
close_chr = ')]}>'

## Part 1
# def score(line):
#     opened = []
#     for character in line:
#         if character in open_chr:
#             opened.append(character)
#         else:
#             last_opened = opened.pop()
#             if open_chr.index(last_opened) != close_chr.index(character):
#                 return [3, 57, 1197, 25137][close_chr.index(character)]
#     return 0

# answer = sum([score(l) for l in data_str])

## Part 2

def score(line):
    opened = []
    for character in line:
        if character in open_chr:
            opened.append(character)
        else:
            last_opened = opened.pop()
            if open_chr.index(last_opened) != close_chr.index(character):
                return 0
    s = 0
    for character in "".join(reversed([close_chr[open_chr.index(op)] for op in opened])):
        s = 5*s + (close_chr.index(character)+1)
    return s

scores = sorted([score(l) for l in data_str if score(l) != 0])
print(scores[len(scores)//2])



