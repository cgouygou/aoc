data = open('input_day2.txt').read().splitlines()

## Part I
# def game(a, b):
#     r1 = ord(a) - ord('A') + 1
#     r2 = ord(b) - ord('X') + 1
#     if r1 == r2:
#         return r1 + 3
#     elif (r2 - r1) % 3 == 1:
#         return r2 + 6
#     else:
#         return r2

## Part II

def game(a, b):
    opponent_choice = ord(a) - ord('A') + 1
    if b == 'Y':
        return opponent_choice + 3
    elif b == 'Z':
        my_choice = (opponent_choice+1) if opponent_choice < 3 else 1
        return my_choice + 6
    else:
        my_choice = (opponent_choice-1) if opponent_choice > 1 else 3
        return my_choice


for a in ('A', 'B', 'C'):
    for b in ('X', 'Y', 'Z'):
        print(game(a, b))


##Commun

score = 0
for g in data:
    score += game(g[0], g[-1])