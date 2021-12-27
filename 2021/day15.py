import os
import time
from dijkstra import *
os.chdir("/home/cedric/Travail/AlgoInfo/CodesPython/adventofcode/aoc/2021/")

data_str = [list(map(int, list(line))) for line in open("input_day15.txt").read().splitlines()]


## Part 1 (heuristique sud + est only)

def lowest_total_risk(tab):
    height, width = len(tab), len(tab[0])

    T = [width * [0] for _ in range(height)]

    for i in range(height):
        for j in range(width):
            if i+j > 0:
                if i == 0:
                    T[i][j] = T[i][j-1] + tab[i][j]
                elif j == 0:
                    T[i][j] = T[i-1][j] + tab[i][j]
                else:
                    T[i][j] = min(T[i][j-1] + tab[i][j], T[i-1][j] + tab[i][j])

    return T[-1][-1]

# print(lowest_total_risk(data_str))

## Part 2

def cycle(value, n):
    if value + n > 9:
        return value + n - 9
    else:
        return value +n

def shift(tab, i, j):
    return [[cycle(v, i+j) for v in line] for line in tab]

def concat_tabs(tab, i):
    tab_line = shift(tab, i, 0)
    for j in range(1, 5):
        for k in range(len(tab)):
            tab_line[k] += shift(tab, i, j)[k]
    return tab_line

def create_map(tab):
    full = []
    for i in range(5):
        full += concat_tabs(tab, i)
    return full

def voisins(s):
    lst = []
    i, j = s
    if i > 0:
        lst.append([full_map[i-1][j], (i-1, j)])
    if i < len(full_map)-1:
        lst.append([full_map[i+1][j], (i+1, j)])
    if j > 0:
        lst.append([full_map[i][j-1], (i, j-1)])
    if j < len(full_map[0])-1:
        lst.append([full_map[i][j+1], (i, j+1)])
    return lst
t0 = time.time()
full_map = create_map(data_str)
t1 = time.time()
d, p = dijkstra((0,0), (499, 499), voisins)
t2 = time.time()
print(d)
print(t2-t1, t1-t0)
