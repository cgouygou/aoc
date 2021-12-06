with open("input_day2.txt","r") as f:
    passwords = [l for l in f.readlines()]


##Part 1
# def isCorrect(pwd):
#     policy, pwd = pwd.split(':')
#     occurences, char = policy.split()
#     occ_min, occ_max = map(int, occurences.split('-'))
#
#     nb_char = pwd.count(char)
#     return nb_char >= occ_min and nb_char <= occ_max


##Part 2

def isCorrect(pwd):
    policy, pwd = pwd.split(':')
    positions, char = policy.split()
    pos1, pos2 = map(int, positions.split('-'))
    return [pwd[pos1], pwd[pos2]].count(char) == 1


sol = sum([isCorrect(p) for p in passwords])
print(sol)
