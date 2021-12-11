import os
from math import inf
os.chdir("/home/cedric/Travail/AlgoInfo/CodesPython/adventofcode/aoc/2021/")

data_str = open("input_day11.txt").read().splitlines()

## Construction du tableau octo
width = len(data_str[0])
octo = [(width+2) * [0]]
for line in data_str:
    octo.append([0]+list(map(int, list(line)))+[0])
octo.append((width+2) * [0])


## Procédures dégueulasses avec plein de variables globales affreuses

flashes = 0

def first_increase():
    for i in range(1, 1+width):
        for j in range(1, 1+width):
            if octo[i][j] == -inf:
                octo[i][j] = 0
            octo[i][j] += 1

def flash(i, j):
    global flashes
    flashes += 1
    octo[i][j] = -inf
    octo[i-1][j-1] += 1
    octo[i-1][j] += 1
    octo[i-1][j+1] += 1
    octo[i][j-1] += 1
    octo[i][j+1] += 1
    octo[i+1][j-1] += 1
    octo[i+1][j] += 1
    octo[i+1][j+1] += 1

def is_flash():
    for i in range(1, 1+width):
        for j in range(1, 1+width):
            if octo[i][j] > 9:
                return i, j
    return False

def step():
    first_increase()
    while is_flash():
        i, j = is_flash()
        flash(i, j)

## Part 1
# for _ in range(100):
#     step()
#
# print(flashes)

## Part 2

def is_sync():
    flashing = 0
    for line in octo:
        flashing += line.count(-inf)
    return flashing == width ** 2

steps = 0
while not is_sync():
    step()
    steps += 1

print(steps)