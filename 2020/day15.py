##Part 1
#
# def spoken_number(starting_numbers, position):
#     memory = [s for s in reversed(starting_numbers)]
#     for k in range(len(starting_numbers), position + 1):
#         tete, queue = memory[0], memory[1:]
#         if tete not in queue:
#             memory = [0] + memory
#         else:
#             i = queue.index(tete)
#             memory = [k - (len(queue) - i)] + memory
#     return tete
#
# print(spoken_number([19, 20, 14, 0, 9, 1], 2020))
##Part 2

def spoken_number(starting_numbers, position):
    memory = {}
    for k, s in enumerate(starting_numbers[:-1]):
        memory[s] = k

    current = starting_numbers[-1]
    for i in range(k+1, position - 1):
        if current in memory:
            nxt = i - memory[current]
        else:
            nxt = 0
        memory[current] = i
        current = nxt
    return current

print(spoken_number([19, 20, 14, 0, 9, 1], 30000000))
