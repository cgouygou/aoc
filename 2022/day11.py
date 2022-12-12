import os
os.chdir('/home/cedric/Travail/AlgoInfo/CodesPython/adventofcode/aoc/2022/')

monkey_items = [[66, 59, 64, 51],
                [67, 61],
                [86, 93, 80, 70, 71, 81, 56],
                [94],
                [71, 92, 64],
                [58, 81, 92, 75, 56],
                [82, 98, 77, 94, 86, 81],
                [54, 95, 70, 93, 88, 93, 63, 50]]

monkey_views = 8 * [0]

operations = [lambda x: x*3,
              lambda x: x*19,
              lambda x: x+2,
              lambda x: x**2,
              lambda x: x+8,
              lambda x: x+6,
              lambda x: x+7,
              lambda x: x+4]

tests = [lambda n: 1 if n%2 == 0 else 4,
         lambda n: 3 if n%7 == 0 else 5,
         lambda n: 4 if n%11 == 0 else 0,
         lambda n: 7 if n%19 == 0 else 6,
         lambda n: 5 if n%3 == 0 else 1,
         lambda n: 3 if n%5 == 0 else 6,
         lambda n: 7 if n%17 == 0 else 2,
         lambda n: 2 if n%13 == 0 else 0]


## Part I
# for round in range(20):
#     for m in range(len(monkey_items)):
#         while monkey_items[m] != []:
#             monkey_views[m] += 1
#             worry_level = operations[m](monkey_items[m].pop(0)) // 3
#             next_monkey = tests[m](worry_level)
#             monkey_items[next_monkey].append(worry_level)

## Part II

modulo = 2 * 3 * 5 * 7 * 11 * 13 * 17 * 19

for round in range(10000):
    for m in range(len(monkey_items)):
        while monkey_items[m] != []:
            monkey_views[m] += 1
            worry_level = operations[m](monkey_items[m].pop(0)) % modulo
            next_monkey = tests[m](worry_level)
            monkey_items[next_monkey].append(worry_level)


## Common
monkey_views.sort(reverse=True)
print(monkey_views[0]*monkey_views[1])