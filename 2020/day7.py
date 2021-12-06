with open("input_day7.txt","r") as f:
    bag_rules = [l.strip() for l in f.readlines()]

##Part 1

# def inText(string, txt):
#     k = 0
#     while k + len(string) < len(txt):
#         if string == txt[k:k + len(string)]:
#             return True
#         k += 1
#     return False
#
# def extract_children(string):
#     if string == "no other bags.":
#         return []
#     else:
#         return [" ".join(s.split()[1:3]) for s in string.split(',')]
#
# sg = 'shiny gold'
#
# bag_tree = {}
#
# for rule in bag_rules:
#     container, contents = rule.split(' contain ')
#     bag = " ".join(container.split()[:2])
#     bag_tree[bag] = extract_children(contents)
#
# def deep_search(parent, child, dic):
#     if dic[parent] == []:
#         return False
#     elif child in dic[parent]:
#         return True
#     else:
#         return sum([deep_search(c, child, dic) for c in dic[parent]])
#
# nb_bags = 0
# for bag in bag_tree:
#     if deep_search(bag, sg, bag_tree):
#         # print(bag)
#         nb_bags += 1
#
# print(nb_bags)

#
# def contains(bag):
#     bags = []
#     for rule in bag_rules:
#         container, contents = rule.split(' contain ')
#         if inText(bag, contents):
#             bags.append(container)
#     return bags
# #
# lstbags = []
# def nb_bag_types(bag):
#     global lstbags
#     bags = [b for b in contains(bag) if b not in lstbags]
#     lstbags += bags
#     if bags == []:
#         return None
#     else:
#         for b in bags:
#             nb_bag_types(b)


##Part 2

def extract_children(string):
    if string == "no other bags.":
        return 0, []
    else:
        return [[int(s.split()[0]), " ".join(s.split()[1:3])] for s in string.split(',')]

sg = 'shiny gold'

bag_tree = {}

for rule in bag_rules:
    container, contents = rule.split(' contain ')
    bag = " ".join(container.split()[:2])
    bag_tree[bag] = extract_children(contents)

def deep_search(parent, dic):
    if dic[parent][0] == 0:
        return 0
    else:
        return sum([c[0] * (1 + deep_search(c[1], dic)) for c in dic[parent]])

print(deep_search(sg, bag_tree))