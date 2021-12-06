import os
os.chdir("/home/cedric/Travail/AlgoInfo/CodesPython/adventofcode/2021/")

## Part 1 (& 2)
data_str = open("input_day5.txt").read().splitlines()

points = [1000 * [0] for _ in range(1000)]

for line in data_str:
    point1, point2 = line.split(' -> ')
    x1, y1 = tuple(map(int, point1.split(',')))
    x2, y2 = tuple(map(int, point2.split(',')))
    
    if x1 == x2:
        for y in range(min(y1, y2), max(y1, y2) + 1):
            points[x1][y] += 1
        
    elif y1 == y2:
        for x in range(min(x1, x2), max(x1, x2) + 1):
            points[x][y1] += 1

# begin Part 2
    else:
        if x1 > x2:
            x1, y1, x2, y2 = x2, y2, x1, y1
        inc = (y2-y1) // abs(y2-y1)
        for x in range(x1, x2+1):
            points[x][y1] += 1
            y1 += inc
# end Part 2

answer = 0
for i in range(1000):
    for j in range(1000):
        if points[i][j] >= 2:
            answer += 1

print(answer)

    