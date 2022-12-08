import os
os.chdir('/home/cedric/Travail/AlgoInfo/CodesPython/adventofcode/aoc/2022/')


data = open('input_day4.txt').read().splitlines()

# data = ['2-4,6-8', '2-3,4-5', '5-7,7-9', '2-8,3-7', '6-6,4-6', '2-6,4-8']

## Part I & II

full_contain, overlap = 0, 0

for assignment in data:
    first, second = assignment.split(',')
    a, b = map(int, first.split('-'))
    c, d = map(int, second.split('-'))

    # Part I
    if (a >= c and b <= d) or (c >= a and d <= b):
        full_contain +=1

    # Part II
    if not (c > b or a > d):
        overlap += 1

print(full_contain, overlap)


