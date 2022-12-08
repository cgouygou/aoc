import os
os.chdir('/home/cedric/Travail/AlgoInfo/CodesPython/adventofcode/aoc/2022/')


data = open("input_day7.txt").read().splitlines()


class Directory:
    def __init__(self, name, p):
        self.name = name
        self.parent = p
        self.children = []
        self.files = []

    def add_file(self, f):
        self.files.append(f)

    def add_child(self, d):
        self.children.append(d)

    def size(self):
        return sum(self.files) + sum([c.size() for c in self.children])

    def select_child(self, name:str) -> Directory:
        for child in self.children:
            if child.name == name:
                return child


home = Directory('/', None)
current_dir = home

for line in data[1:]:
    if line == '$ cd ..':
        current_dir = current_dir.parent
    elif line[:5] == '$ cd ':
        dir_name = line.split()[-1]
        current_dir = current_dir.select_child(dir_name)
    elif line == '$ ls':
        pass
    elif line[:3] == 'dir':
        current_dir.add_child(Directory(line.split()[-1], current_dir))
    else:
        current_dir.add_file(int(line.split()[0]))


# Part I
small_sizes = []
def find_small_sizes(d):
    s = d.size()
    if s <= 100000:
        small_sizes.append(s)
    for child in d.children:
        find_small_sizes(child)

find_small_sizes(home)
print(sum(small_sizes))

# Part II
unused_space = 70000000 - home.size()
big_enough = []

def find_sizes(d):
    s = d.size()
    if s >= 30000000 - unused_space:
        big_enough.append(s)
    for child in d.children:
        find_sizes(child)

find_sizes(home)
print(min(big_enough))