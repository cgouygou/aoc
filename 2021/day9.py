import os
os.chdir("/media/cedric/CLECGOUYGOU/Travail/AlgoInfo/CodesPython/adventofcode/aoc/2021/")

data_str = open("input_day9.txt").read().splitlines()

## Construction du tableau heightmap
width = len(data_str[0])
heightmap = [(width+2) * [9]]
for line in data_str:
    heightmap.append([9]+list(map(int, list(line)))+[9])
heightmap.append((width+2) * [9])


## Part 1
# answer = 0
# for i in range(1, 1+width):
#     for j in range(1, 1+width):
#         neighbours = [heightmap[i-1][j], heightmap[i+1][j], heightmap[i][j-1], heightmap[i][j+1]]
#         if heightmap[i][j] < min(neighbours):
#             answer += 1 + heightmap[i][j]
#
# print(answer)


## Part 2

#Construction du graphe
graph = {(i, j): [] for i in range(1, 1+width) for j in range(1, 1+width) if heightmap[i][j] != 9}

for g in graph:
    i, j = g
    if heightmap[i-1][j] != 9:
        graph[g].append ((i-1, j))
    if heightmap[i+1][j] != 9:
        graph[g].append ((i+1, j))
    if heightmap[i][j-1] != 9:
        graph[g].append ((i, j-1))
    if heightmap[i][j+1] != 9:
        graph[g].append ((i, j+1))

# Recherche des composantes connexes
seen = []
not_seen = list(graph.keys())
components = dict()

def cc_vertex(G, v, i):
    seen.append(v)
    not_seen.remove(v)
    if i in components:
        components[i].append(v)
    else:
        components[i] = [v]
    for neighbour in G[v]:
        if neighbour not in seen:
            cc_vertex(G, neighbour, i)

def cc(G):
    i = 0
    while len(seen) != len(G):
        vertex = not_seen[0]
        cc_vertex(G, vertex, i)
        i += 1

cc(graph)

# Tailles des composantes connexes par parcours
sizes = sorted([len(value) for value in components.values()], reverse=True)

print(sizes[0]*sizes[1]*sizes[2])