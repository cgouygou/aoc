data = open('input_day3.txt').read().splitlines()

example = ['vJrwpWtwJgWrhcsFMMfFFhFp', 'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
           'PmmdzqPrVvPwwTWBwg', 'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
           'ttgJtRGJQctTZtZT', 'CrZsJsPPZsGzwwsLwLmpwMDw']

## Part I (version NSI)
def priority(ruckpack:str) -> int:
    l = len(ruckpack)
    first, second = ruckpack[:l//2], ruckpack[l//2:]
    item = set(first).intersection(set(second)).pop()
    if ord(item) <= 90:
        return ord(item) - ord('A') + 27
    else:
        return ord(item) - ord('a') + 1

# answer = sum([priority(r) for r in data])

## Part II
def badge(ruck_list:list) -> int:
    f, s, t = ruck_list
#     b = set(f).intersection(set(s)).intersection(set(t)).pop()
    b = (set(f) & set(s) & set(t)).pop()
    if ord(b) <= 90:
        return ord(b) - ord('A') + 27
    else:
        return ord(b) - ord('a') + 1
    
answer = sum([badge(data[i:i+3]) for i in range(0, len(data), 3)])