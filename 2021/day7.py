import os
# os.chdir("/home/cedric/Travail/AlgoInfo/CodesPython/adventofcode/2021/")
os.chdir("/media/cedric/CLECGOUYGOU/Travail/AlgoInfo/CodesPython/aoc/aoc/2021/")

data_str = open("input_day7.txt").read().splitlines()
crabs = list(map(int, data_str[0].split(',')))
# Example
# crabs = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]

## Part 1

# def median(lst):
#     sorted_lst = sorted(lst)
#     l = len(sorted_lst)
#     if l%2 == 1:
#         return sorted_lst[(l+1)//2]
#     else:
#         return (sorted_lst[l//2-1]+sorted_lst[l//2])//2
#
# def cost(lst, pos):
#     return sum([abs(elt - pos) for elt in lst])
#
# print(cost(crabs, median(crabs)))
#

## Part 2

def cost(pos1, pos2):
    distance = abs(pos1 - pos2)
    return distance * (distance + 1) // 2

costs = [sum([cost(crab, pos) for crab in crabs]) for pos in range(max(crabs))]

print(min(costs))