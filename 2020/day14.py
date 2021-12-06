# import os
#
# os.chdir("/home/cedric/Travail/AlgoInfo/CodesPython/adventofcode/2020/")

with open("input_day14.txt","r") as f:
    instructions = [l.strip() for l in f.readlines()]

##Part 1

# def masked_value(v: int, m: str) -> int:
#     mv = ''
#     v_bin = bin(v)[2:]
#     v_bin = (36 - len(v_bin))*['0'] + list(v_bin)
#     for k in range(len(m)):
#         if m[k] == 'X':
#             mv += v_bin[k]
#         else:
#             mv += m[k]
#     return int(mv, 2)
#
# mem = {}
#
# for instruction in instructions:
#     splitted_data = instruction.split(' = ')
#     if splitted_data[0] == 'mask':
#         mask = splitted_data[1]
#     else:
#         value = int(splitted_data[1])
#         rank = int("".join([s for s in splitted_data[0] if s.isnumeric()]))
#         mem[rank] = masked_value(value, mask)
#
# print(sum(mem.values()))

##Part 2

def replace(n: int, b: str, s: str) -> str:
    '''remplace dans la chaine s les X par les bits de b, complété par des 0 sur
    la longueur en binaire de n'''
    r = 0
    replaced = ''
    for c in s:
        if c == 'X':
            replaced += b.zfill(len(bin(n-1)[2:]))[r]
            r += 1
        else:
            replaced += c
    return replaced


def masked_adresses(a: int, m: str) -> int:
    '''applique le filtre dans ma
    puis renvoie la liste de tous les entiers possibles'''
    ma = ''
    a_bin = bin(a)[2:]
    a_bin = (36 - len(a_bin))*['0'] + list(a_bin)
    for k in range(len(m)):
        if m[k] == '0':
            ma += a_bin[k]
        else:
            ma += m[k]
    nx = ma.count('X')
    ma_list = []
    for k in range(2**nx):
        k_bin = bin(k)[2:]
        ma_list.append(int(replace(2**nx, k_bin, ma), 2))
    return ma_list

mem = {}

for instruction in instructions:
    splitted_data = instruction.split(' = ')
    if splitted_data[0] == 'mask':
        mask = splitted_data[1]
    else:
        value = int(splitted_data[1])
        rank = int("".join([s for s in splitted_data[0] if s.isnumeric()]))
        for adresse in masked_adresses(rank, mask):
            mem[adresse] = value

print(sum(mem.values()))