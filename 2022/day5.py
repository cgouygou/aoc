import os
os.chdir('/home/cedric/Travail/AlgoInfo/CodesPython/adventofcode/aoc/2022/')


data = open('input_day5.txt').read().splitlines()

piles = [list('QMGCL'), list('RDLCTFHG'), list('VJFNMTWR'), list('JFDVQP'), list('NFMSLBT'),
         list('RNVHCDP'), list('HCT'), list('GSJVZNHP'), list('ZFHG')]


def extract_move(proc:str) -> tuple:
    p = proc.split()
    return tuple(map(int, [p[1], p[3], p[5]]))


## Part I

# for procedure in data:
#     nb_crates, start, end = extract_move(procedure)
#     for k in range(nb_crates):
#         piles[end-1].append(piles[start-1].pop())


## Part II

for procedure in data:
    nb_crates, start, end = extract_move(procedure)
    temp_pile = []
    for k in range(nb_crates):
        temp_pile.append(piles[start-1].pop())
    for k in range(nb_crates):
        piles[end-1].append(temp_pile.pop())



## Common Answer

print(''.join([p[-1] for p in piles]))
