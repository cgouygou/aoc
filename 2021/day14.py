import os
import time
os.chdir("/home/cedric/Travail/AlgoInfo/CodesPython/adventofcode/aoc/2021/")

data_str = open("input_day14.txt").read().splitlines()

## Parsing data
template = data_str[0]
insertion_rules = dict()
for i in range(2, len(data_str)):
    insertion_rules[data_str[i].split(' -> ')[0]] = data_str[i].split(' -> ')[1]

## Part 1
# def insertion(chain, rules):
#     new_chain = ''
#     for i in range(len(chain) - 1):
#         new_chain += chain[i] + rules[chain[i:i+2]]
#     return new_chain + chain[-1]
#
# steps = 10
# for step in range(steps):
#     template = insertion(template, insertion_rules)
#
# frequencies = {element: template.count(element) for element in set(template)}
# print( max(frequencies.values()) - min(frequencies.values()))

## Part 2
template = data_str[0]

pairs = {template[i:i+2]:template.count(template[i:i+2]) for i in range(len(template) - 1)}

elements = {e:(template).count(e) for e in set(insertion_rules.values())}

steps = 40

for _ in range(steps):
    new_pairs = dict()
    for p in pairs:
        to_insert = insertion_rules[p]
        elements[to_insert] += pairs[p]
        for np in [p[0]+to_insert, to_insert+p[1]]:
            if np in new_pairs:
                new_pairs[np] += pairs[p]
            else:
                new_pairs[np] = pairs[p]
    pairs = dict(new_pairs) #on remplace et on recommence...

print(max(elements.values()) - min(elements.values()))
