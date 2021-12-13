import os
os.chdir("/home/cedric/Travail/AlgoInfo/CodesPython/adventofcode/aoc/2021/")

data_str = open("input_day12.txt").read().splitlines()

## Construction du graphe

caves = dict()

for edge in data_str:
    vertexes = edge.split('-')
    for i in range(2):
        if vertexes[i] in caves:
            caves[vertexes[i]].append(vertexes[1-i])
        else:
            caves[vertexes[i]] = [vertexes[1-i]]

def is_lower(vertex):
    return vertex[0].lower() == vertex[0]

## Part 1

# paths = []
#
# def find_path(graph, path, seen):
#     if path[-1] == 'end':
#         paths.append(path)
#     else:
#         for neighbour in graph[path[-1]]:
#             if neighbour not in seen:
#                 if is_lower(neighbour):
#                     find_path(graph, path + [neighbour], seen + [neighbour])
#                 else:
#                     find_path(graph, path + [neighbour], seen)
#
# find_path(caves, ['start'], ['start'])

## Part 2

paths = []

def find_path(graph, path, seen, joker):
    if path[-1] == 'end':
        if path not in paths:
            paths.append(path)
    else:
        for neighbour in graph[path[-1]]:
            if neighbour not in seen:
                if is_lower(neighbour):
                    if neighbour == joker:
                        find_path(graph, path + [neighbour], seen, '')
                    else:
                        find_path(graph, path + [neighbour], seen + [neighbour], joker)
                else:
                    find_path(graph, path + [neighbour], seen, joker)

for c in caves:
    if is_lower(c):
        find_path(caves, ['start'], ['start'], c)


