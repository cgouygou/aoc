with open("input_day6.txt","r") as f:
    answers = [l.strip() for l in f.readlines()]

##Part 1
# line = 0
# sum_answers = 0
#
# while line < len(answers):
#     ans = ''
#     while line < len(answers) and answers[line] != '':
#         ans += answers[line]
#         line += 1
#     sum_answers += len(set(ans))
#     line += 1
#
# print(sum_answers)

##Part 2

def set_intersection(lst):
    i = set(lst[0])
    for item in lst:
        i = i.intersection(set(item))
    return i

line = 0
sum_answers = 0

while line < len(answers):
    ans = []
    while line < len(answers) and answers[line] != '':
        ans.append(answers[line])
        line += 1

    sum_answers += len(set_intersection(ans))
    line += 1

print(sum_answers)