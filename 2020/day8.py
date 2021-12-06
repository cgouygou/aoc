with open("input_day8.txt","r") as f:
    instructions = [l.strip() for l in f.readlines()]

##Part 1

# def game(sequence):
#     done = len(sequence) * [0]
#     rank = 0
#     acc = 0
#     while done[rank] == 0:
#         done[rank] = 1
#         instruction, value = sequence[rank].split()[0], int(sequence[rank].split()[1])
#         if instruction == 'nop':
#             rank += 1
#         elif instruction == 'acc':
#             acc += value
#             rank += 1
#         else:
#             rank += value
#     return acc
#
# print(game(instructions))

##Part 2

def game(sequence):
    done = len(sequence) * [0]
    rank = 0
    acc = 0
    while rank < len(sequence) and done[rank] == 0:
        done[rank] = 1
        instruction, value = sequence[rank].split()[0], int(sequence[rank].split()[1])
        if instruction == 'nop':
            rank += 1
        elif instruction == 'acc':
            acc += value
            rank += 1
        else:
            rank += value
    if rank == len(sequence):
        return acc
    else:
        return False

def modify(seq, k):
    instruction, value = seq[k].split()[0], seq[k].split()[1]
    if instruction == 'nop':
        seq[k] = 'jmp ' + value
    else:
        seq[k] = 'nop ' + value

rank = 0
sequence = instructions.copy()
while not game(sequence):
    rank += 1
    while instructions[rank][:3] not in {'nop', 'jmp'}:
        rank += 1
    sequence = instructions.copy()
    modify(sequence, rank)

print(game(sequence))
