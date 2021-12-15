import os
os.chdir("/home/cedric/Travail/AlgoInfo/CodesPython/adventofcode/aoc/2021/")

data_str = open("input_day6.txt").read().splitlines()
fishes = list(map(int, data_str[0].split(',')))
# Example
# fishes = [3, 4, 3, 1, 2]

nb_days = 256

## Part 1

# for day in range(nb_days):
#     new_fish = 0
#     for i in range(len(fishes)):
#         if fishes[i] == 0:
#             fishes[i] = 6
#             new_fish += 1
#         else:
#             fishes[i] -= 1
#     fishes += new_fish * [8]
#

## Part 2

# def create(timer, days):
#     new = max(0, (days-timer)//7 + 1*((days-timer)%7>0))
#     # print(new)
#     c = new
#     for k in range(new):
#         c += create(8, days-(timer+k*7))
#     return c
#
# for fish in [3,4,3,1,2]:
#     print(create(fish, 18))
#
# print(sum([create(fish, 256) for fish in [3,4,3,1,2]]))

timer = {k: 0 for k in range(9)}

for f in fishes:
    timer[f] += 1

for _ in range(nb_days):
    temp = timer[0]
    for k in range(8):
        timer[k] = timer[k+1]
    timer[6] += temp
    timer[8] = temp
    # print(timer)

print(sum(timer.values()))