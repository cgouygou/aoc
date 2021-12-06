import os
os.chdir("/home/cedric/Travail/AlgoInfo/CodesPython/adventofcode/2020/")

with open("input_day11.txt","r") as f:
    seats = [['.'] + list(l.strip()) + ['.'] for l in f.readlines()]

##Part 1

# height, width = len(seats) + 2, len(seats[0])
#
# seats.insert(0, width * ['.'])
# seats = seats + [width * ['.']]
#
# def nb_occupied(grid):
#     return sum([line.count('#') for line in grid])
#
# def nb_neighbours(l, c, grid):
#     neighbours = [grid[l-1][c-1], grid[l-1][c], grid[l-1][c+1], grid[l][c-1],
#     grid[l][c+1], grid[l+1][c-1], grid[l+1][c], grid[l+1][c+1]]
#     return neighbours.count('#')
#
# def next_round(init_grid):
#     nb_changes = 0
#     h, w = len(init_grid), len(init_grid[0])
#     final_grid = [['.' for _ in range(w)] for _ in range(h)]
#     for l in range(1, len(init_grid) - 1):
#         for c in range(1, len(init_grid[0]) - 1):
#             if init_grid[l][c] == 'L' and nb_neighbours(l, c, init_grid) == 0:
#                 final_grid[l][c] = '#'
#                 nb_changes += 1
#             elif init_grid[l][c] == '#' and nb_neighbours(l, c, init_grid) >= 4:
#                 final_grid[l][c] = 'L'
#                 nb_changes += 1
#             else:
#                 final_grid[l][c] = init_grid[l][c]
#     return final_grid, nb_changes
#
# n = 1
# while n != 0:
#     seats, n = next_round(seats)
#
# print(nb_occupied(seats))

##Part 2

height, width = len(seats) + 2, len(seats[0])

seats.insert(0, width * ['.'])
seats = seats + [width * ['.']]

def nb_occupied(grid):
    return sum([line.count('#') for line in grid])

def visible_seat(l, c, dir, grid):
    seat = '.'
    x, y = l + dir[0], c + dir[1]
    while x in range(height) and y in range(width) and seat == '.':
        seat = grid[x][y]
        x += dir[0]
        y += dir[1]
    return seat

def nb_neighbours(l, c, grid):
    neighbours = [visible_seat(l, c, d, grid) for d in [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]]
    return neighbours.count('#')

def next_round(init_grid):
    nb_changes = 0
    h, w = len(init_grid), len(init_grid[0])
    final_grid = [['.' for _ in range(w)] for _ in range(h)]
    for l in range(1, len(init_grid) - 1):
        for c in range(1, len(init_grid[0]) - 1):
            if init_grid[l][c] == 'L' and nb_neighbours(l, c, init_grid) == 0:
                final_grid[l][c] = '#'
                nb_changes += 1
            elif init_grid[l][c] == '#' and nb_neighbours(l, c, init_grid) >= 5:
                final_grid[l][c] = 'L'
                nb_changes += 1
            else:
                final_grid[l][c] = init_grid[l][c]
    return final_grid, nb_changes

n = 1
while n != 0:
    seats, n = next_round(seats)

print(nb_occupied(seats))
