import os
import networkx as nx
import matplotlib.pyplot as plt

os.chdir('/home/cedric/Travail/AlgoInfo/CodesPython/adventofcode/aoc/2022/')

data = [list(row) for row in open("input_day12.txt").read().splitlines()]

## Part I
G = nx.DiGraph()

# Création des noeuds et lecture source/target
for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j] == 'S':
            source = (i, j)
            data[i][j] = 'a'
        elif data[i][j] == 'E':
            target = (i, j)
            data[i][j] = 'z'
        G.add_node((i, j))

# Création des arcs
for i in range(len(data)):
    for j in range(len(data[0])):
        for d in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            if (i + d[0], j + d[1]) in G.nodes() and (i + d[0], j + d[1]) not in G.neighbors((i, j)):
                if ord(data[i + d[0]][j + d[1]]) - ord(data[i][j]) <= 1:
                    G.add_edge((i, j) , (i + d[0], j + d[1]))

# Et un bon vieux Dijkstra
# sp = nx.shortest_path(G, source, target)
# print(len(sp)-1)
#
# #Affichage du chemin (en capitales)
# for s in sp:
#     data[s[0]][s[1]] = data[s[0]][s[1]].upper()
# for row in data:
#     print(''.join(row))

## Part II
path_lengths = set()
for i in range(len(data)):
    path_lengths.add(len(nx.shortest_path(G, (i, 0), target))-1)