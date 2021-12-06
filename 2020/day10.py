import os
from functools import lru_cache


os.chdir("/home/cedric/Travail/AlgoInfo/CodesPython/adventofcode/2020/")

## Part 1
# with open("input_day10.txt","r") as f:
#     adapters = [0] + [int(l.strip()) for l in f.readlines()]
#
# adapters.sort()
# adapters.append(max(adapters) + 3)
#
# differences = [adapters[k+1] - adapters[k] for k in range(len(adapters) - 1)]
# print(differences.count(1) * differences.count(3))

## Part 2

with open("input_day10.txt","r") as f:
    adapters = [int(l.strip()) for l in f.readlines()]

adapters.sort()

@lru_cache()
def arrangements(n, tup):
    if tup == ():
        return 1
    else:
        next_jolts = [l for l in tup[:3] if l - n <= 3]
        return sum([arrangements(l, tup[tup.index(l)+1:]) for l in next_jolts])

print(arrangements(0, tuple(adapters)))

