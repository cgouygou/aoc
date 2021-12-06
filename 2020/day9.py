with open("input_day9.txt","r") as f:
    numbers = [int(l.strip()) for l in f.readlines()]

##Part 1

# def isValid(k, lst):
#     n = lst[k]
#     preamble = lst[k-25:k]
#     for p in preamble:
#         if lst[rank] - p in preamble:
#             return True
#     return False
#
# go = True
# rank = 24
#
# while go:
#     rank += 1
#     go = isValid(rank, numbers)
#
# print(numbers[rank])

##Part 2

invalid = 69316178

def contiguous_sum(k, n, lst):
    s = lst[k]
    rank = k
    while s < n:
        rank += 1
        s += lst[rank]
    return s == n, k, rank

rank = 0
stop = False
while not stop:
    stop, rank_min, rank_max = contiguous_sum(rank, invalid, numbers)
    rank += 1
print(min(numbers[rank_min:rank_max+1]) + max((numbers[rank_min:rank_max+1])))