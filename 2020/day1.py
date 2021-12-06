with open("input_day1.txt","r") as f:
    numbers = [int(l) for l in f.readlines()]


def find_sum2(N, lst):
    for item in lst:
        if N - item in lst:
            return item
    return None

def find_sum3(N, lst):
    for item in lst:
        a = find_sum2(N - item, lst)
        if a != None:
            return item, a, N - (item + a)


##Part 1
# a = find_sum2(2020, numbers)
# print(a, 2020 - a, a*(2020-a))

##Part 2
sol = find_sum3(2020, numbers)

print(sol, sol[0] * sol[1] * sol[2])