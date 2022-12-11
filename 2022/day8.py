import os
os.chdir('/home/cedric/Travail/AlgoInfo/CodesPython/adventofcode/aoc/2022/')


data = open("input_day8.txt").read().splitlines()

## Part I

# visibles = [[1] * len(data)] + [[1]+ [0] * (len(data)-2) + [1] for _ in range(len(data)-2)] + [[1] * len(data)]
#
# #passage gauche -> droite
# for row in range(1,len(data)-1):
#     h_max = int(data[row][0])
#     for i in range(1,len(data)-1):
#         if int(data[row][i]) > h_max:
#             h_max = int(data[row][i])
#             visibles[row][i] = 1
#
# #passage droite -> gauche
# for row in range(1,len(data)-1):
#     h_max = int(data[row][-1])
#     for i in range(len(data)-1, 0, -1):
#         if int(data[row][i]) > h_max:
#             h_max = int(data[row][i])
#             visibles[row][i] = 1
#
# #passage haut -> bas
# for column in range(1,len(data)-1):
#     h_max = int(data[0][column])
#     for i in range(1,len(data)-1):
#         if int(data[i][column]) > h_max:
#             h_max = int(data[i][column])
#             visibles[i][column] = 1
#
# # #passage bas -> haut
# for column in range(1,len(data)-1):
#     h_max = int(data[-1][column])
#     for i in range(len(data)-1, 0, -1):
#         if int(data[i][column]) > h_max:
#             h_max = int(data[i][column])
#             visibles[i][column] = 1
#
# print(sum([sum(row) for row in visibles]))

## Part II

def get_tree(position:tuple) -> int:
    return int(data[position[0]][position[1]])

def viewing_distance(position:tuple, direction:tuple, hmax:int) -> int:
    next_position = (position[0]+direction[0], position[1]+direction[1])
    if 0 in next_position or len(data) - 1 in next_position or get_tree(next_position) >= hmax:
        return 1
    else:
        return 1 + viewing_distance(next_position, direction, hmax)

def scenic_score(position:tuple):
    directions = [[-1, 0], [0, -1], [0, 1], [1, 0]]
    score = 1
    for d in directions:
        score *= viewing_distance(position, d, get_tree(position))
    return score

scores = [[scenic_score((r, c)) for c in range(1, len(data)-1)] for r in range(1, len(data)-1)]

print(max([max(row) for row in scores]))