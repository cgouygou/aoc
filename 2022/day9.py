import os
os.chdir('/home/cedric/Travail/AlgoInfo/CodesPython/adventofcode/aoc/2022/')

data = open("input_day9.txt").read().splitlines()

class Knot:
    def __init__(self):
        self.pos = [0, 0]

    def is_touching(self, knot):
        return abs(self.pos[0] - knot.pos[0]) <=1 and abs(self.pos[1] - knot.pos[1]) <=1

    def update(self, previous_knot):
        if not self.is_touching(previous_knot):
            dx = previous_knot.pos[0] - self.pos[0]
            dy = previous_knot.pos[1] - self.pos[1]
            if dy == 0:
                self.pos[0] += dx // 2
            elif dx == 0:
                self.pos[1] += dy // 2
            else:
                self.pos[0] += dx // abs(dx)
                self.pos[1] += dy // abs(dy)

class Rope:
    directions = {'R': (0, 1), 'L': (0, -1), 'U': (-1, 0), 'D': (1, 0)}
    def __init__(self, n):
        self.knots = [Knot() for _ in range(n)]

    def update_head(self, direction):
        self.knots[0].pos[0] += Rope.directions[direction][0]
        self.knots[0].pos[1] += Rope.directions[direction][1]

    def update_tail(self):
        for i in range(1, len(self.knots)):
            self.knots[i].update(self.knots[i-1])

## Part I
# rope = Rope(2)

## Part II
rope = Rope(10)

visited = set()
for move in data:
    direction, steps = move[0], int(move.split()[-1])
    for step in range(steps):
        rope.update_head(direction)
        rope.update_tail()
        visited.add(tuple(rope.knots[-1].pos))


print(len(visited))
