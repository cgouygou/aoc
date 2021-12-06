
## Part 1

# timestamp = 1000677
# IDs = [29,41,661,13,17,23,521,37,19]
#
# go = True
#
# while go:
#     timestamp += 1
#     go = all(timestamp % i  for i in IDs)
#
#
# print((timestamp - 1000677) * [i for i in IDs if timestamp % i == 0][0])

## Part 2
from functools import reduce

# Un peu d'arithmétique
def euclideEtendu(a, b):
    r, u, v, rp, up, vp = a, 1, 0, b, 0, 1
    while rp != 0:
        q = r // rp
        r, u, v, rp, up, vp = rp, up, vp, r - q*rp, u - q*up, v - q*vp
    return u, v

def inverse(a, modulo):
    (u, v) = euclideEtendu(a, modulo)
    if u < 0:
        return u + modulo
    return u

x = 0

IDs = [29,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,661,x,x,x,x,x,x,x,x,x,x,x,x,13,17,x,x,x,x,x,x,x,x,23,x,x,x,x,x,x,x,521,x,x,x,x,x,37,x,x,x,x,x,x,x,x,x,x,x,x,19]

modulos = [i for i in IDs if i!=0]
restes = [-r for r, i in enumerate(IDs) if i != 0]
M = reduce(lambda x, y: x * y, modulos)
inverses = [inverse(M // modulos[k], modulos[k]) for k in range(len(modulos))]

timestamp = sum([restes[k] * inverses[k] * M // modulos[k] for k in range(len(modulos))])
print(timestamp % M)


