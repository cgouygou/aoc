import os
os.chdir("/home/cedric/Travail/AlgoInfo/CodesPython/adventofcode/2021/")

data_str = open("input_day6.txt").read().splitlines()
fishes = list(map(int, data_str[0].split(',')))

## Part 1 

nb_days = 80

for day in range(nb_days):
    new_fish = 0
    for i in range(len(fishes)):
        if fishes[i] == 0:
            fishes[i] = 6
            new_fish += 1
        else:
            fishes[i] -= 1
    fishes += new_fish * [8]


    