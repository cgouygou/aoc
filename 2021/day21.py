import os
os.chdir("/home/cedric/Travail/AlgoInfo/CodesPython/adventofcode/aoc/2021/")

# Player 1 starting position: 6
# Player 2 starting position: 4

scores = [0, 0]
positions = [4, 8]
dice = list(range(1, 101))
i_dice = 0
steps = 0

while max(scores) < 1000:
# for _ in range(4):
    steps += 1
    for player in range(2):
        roll = dice[i_dice] + dice[i_dice+1] + dice[i_dice+2]
        dice += 3
        positions[player] = (positions[player] + roll) % 10
        if positions[player] == 0:
            positions[player] = 10
        scores[player] += positions[player]
    # print(positions, scores, dice)


