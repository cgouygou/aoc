with open("input_day3.txt","r") as f:
    tree_lines = [l.strip() for l in f.readlines()]

##Part 1

# pos = 0
# width = len(tree_lines[0])
# height = len(tree_lines)
#
# nb_trees = 0
#
# for line in tree_lines:
#     if line[pos] == '#':
#         nb_trees += 1
#     pos = (pos + 3) % long
#
# print(nb_trees)

##Part 2

width = len(tree_lines[0])
height = len(tree_lines)

def nb_trees(right, down):
    pos = 0
    n = 0
    line = 0
    while line < height:
        if tree_lines[line][pos] == '#':
            n += 1
        line += down
        pos = (pos + right) % width
    return n

print(nb_trees(3, 1) * nb_trees(1, 1) * nb_trees(5, 1) * nb_trees(7, 1) * nb_trees(1, 2))