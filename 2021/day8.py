import os
os.chdir("/home/cedric/Travail/AlgoInfo/CodesPython/adventofcode/aoc/2021/")

data_str = open("input_day8.txt").read().splitlines()
# Example
# data_str = ['acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf']

## Part 1
# nb_segments = []
# for line in data_str:
#     output_values = line.split('|')[1].split()
#     for value in output_values:
#         nb_segments.append(len(value))
# 
# ones = nb_segments.count(2)
# fours = nb_segments.count(4)
# sevens = nb_segments.count(3)
# eights = nb_segments.count(7)
# 
# print(ones+fours+sevens+eights)

## Part 2
def analysis(single_patterns_list):
    digits = dict()
    digits[8] = set(single_patterns_list[-1])
    digits[1] = set(single_patterns_list[0])
    digits[7] = set(single_patterns_list[1])
    digits[4] = set(single_patterns_list[2])
    for pattern in [sp for sp in single_patterns_list if len(sp) == 6]:
        if not digits[1].issubset(set(pattern)):
            digits[6] = set(pattern)
        elif digits[4].issubset(set(pattern)):
            digits[9] = set(pattern)
        else:
            digits[0] = set(pattern)
    for pattern in [sp for sp in single_patterns_list if len(sp) == 5]:
        if digits[1].issubset(set(pattern)):
            digits[3] = set(pattern)
        elif set(pattern).issubset(digits[6]):
            digits[5] = set(pattern)
        else:
            digits[2] = set(pattern)
    return digits
    
def decode(number, digit_dict):
    for digit, value in digit_dict.items():
        if set(number) == value:
            return digit
answer = 0
for line in data_str:
    single_patterns, output_values = sorted(line.split('|')[0].split(), key=len), line.split('|')[1].split()
    a = analysis(single_patterns)
    answer += int("".join([str(decode(value, a)) for value in output_values]))

print(answer)