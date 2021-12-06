import os
#
os.chdir("/home/cedric/Travail/AlgoInfo/CodesPython/adventofcode/2020/")

with open("input_day16.txt","r") as f:
    instructions = [l.strip() for l in f.readlines()]

##Part 1

fields = [[i.split()[-3], i.split()[-1]] for i in instructions[:20]]

def notinField(field, n):
    a, b = map(int, field[0].split('-'))
    c, d = map(int, field[1].split('-'))
    return not(n in range(a, b+1) or n in range(c, d+1))

def isUnvalid(n):
    return all([notinField(f, n) for f in fields])

# unvalid = []
# for i in instructions[25:]:
#     for value in map(int, i.split(',')):
#         if isUnvalid(value):
#             unvalid.append(value)

# print(sum(unvalid))

##Part 2

valid_tickets = []
for i in instructions[25:]:
    check  = True
    for value in map(int, i.split(',')):
        if isUnvalid(value):
            check = False
    if check:
        valid_tickets.append(i)
