import os
import numpy as np

os.chdir("/home/cedric/Travail/AlgoInfo/CodesPython/adventofcode/2020/")

with open("input_day12.txt","r") as f:
    actions = [l.strip() for l in f.readlines()]

##Part 1

# directions = [[1, 0], [0, -1], [-1, 0], [0, 1]]
# card_points = ['E', 'S', 'W', 'N']
# position = [0, 0]
# current_direction = 0
#
# for action in actions:
#     a = action[0]
#     value = int(action[1:])
#     if a in card_points:
#         position[0] += value * directions[card_points.index(a)][0]
#         position[1] += value * directions[card_points.index(a)][1]
#     elif a == 'L':
#         current_direction = (current_direction - value//90) % 4
#     elif a == 'R':
#         current_direction = (current_direction + value//90) % 4
#     else:
#         position[0] += value * directions[current_direction][0]
#         position[1] += value * directions[current_direction][1]
#
# print(abs(position[0]) +abs(position[1]))

##Part 2

directions = [[1, 0], [0, -1], [-1, 0], [0, 1]]
card_points = ['E', 'S', 'W', 'N']
position = np.mat([[0], [0]])
waypoint = np.mat([[10], [1]])

def rotate(wp, val, sens):
    rot = np.mat([[0, -1], [1, 0]])
    if sens == 'R':
        rot = - rot
    for i in range(val//90):
        wp = rot * wp
    return wp

for action in actions:
    a = action[0]
    value = int(action[1:])
    if a in card_points:
        waypoint[0] += value * directions[card_points.index(a)][0]
        waypoint[1] += value * directions[card_points.index(a)][1]
    elif a == 'F':
        position = position + value * waypoint
    else:
        waypoint = rotate(waypoint, value, a)

print(abs(position[0]) +abs(position[1]))
