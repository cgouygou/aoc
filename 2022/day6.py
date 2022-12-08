data = open("input_day6.txt").read().splitlines()[0]


def find_first_marker(s:str, n:int) -> int:
    for i in range(len(s)):
        if len(set(s[i:i+n])) == n:
            return i + n

assert find_first_marker('bvwbjplbgvbhsrlpgdmjqwftvncz', 4) == 5
assert find_first_marker('nppdvjthqldpwncqszvftbrmjlhg', 4) == 6
assert find_first_marker('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 4) == 10
assert find_first_marker('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 4) == 11
assert find_first_marker('bvwbjplbgvbhsrlpgdmjqwftvncz', 14) == 23
assert find_first_marker('nppdvjthqldpwncqszvftbrmjlhg', 14) == 23
assert find_first_marker('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 14) == 29
assert find_first_marker('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 14) == 26


# Part I
print(find_first_marker(data, 4))

# Part II
print(find_first_marker(data, 14))
