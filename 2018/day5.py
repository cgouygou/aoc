import time


data = open('/home/cedric/Travail/AlgoInfo/CodesPython/adventofcode/aoc/2018/input_day5.txt').read()[:-1]

def is_opposite(s:str, t:str) -> bool:
    '''
    renvoie un booléen qui détermine si les deux caractères sont les mêmes,
    avec une casse (minuscule, majuscule) différente.
    '''
    return abs(ord(s) - ord(t)) == 32


def remove_first_pair(string:str) -> tuple:
    '''
    simplifie la première paire de caractères opposés dans la chaîne de caractère
    et renvoie un tuple composé de la chaîne simplifiée et d'un booléen indiquant
    si une simplification a eu lieu
    '''
    for i in range(len(string)-1):
        if is_opposite(string[i], string[i+1]):
            return string[:i] + string[i+2:], True
    return string, False

example = 'dabAcCaCBAcCcaDA'

# start_time = time.time()
# remove = True
# while remove:
#     data, remove = remove_first_pair(data)
# print(len(data))
# end_time = time.time()
#
# print(end_time - start_time)

# 23.895 s

start_time = time.time()

pile = []

for i in range(len(data)):
    if pile == [] or not is_opposite(pile[-1], data[i]):
        pile.append(data[i])
    else:
        pile.pop()

print(len(pile))
end_time = time.time()

print(end_time - start_time)

# 0.021 s
