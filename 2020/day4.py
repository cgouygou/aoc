with open("input_day4.txt","r") as f:
    batch = [l.strip() for l in f.readlines()]

##Part 1

# def isValid(passport):
#     nb_fields = len(passport.split(':'))
#     return nb_fields == 9 or (nb_fields == 8 and 'cid' not in passport)
#
# line = 0
# nb_valid_passports = 0
#
# while line < len(batch):
#     passport = ''
#     while line < len(batch) and batch[line] != '':
#         passport += batch[line]
#         line += 1
#     if isValid(passport):
#         nb_valid_passports += 1
#     line += 1
#
# print(nb_valid_passports)
##Part 2

def isValid(passport):
    fields = passport.split()
    if not (len(fields) == 8 or (len(fields) == 7 and 'cid' not in passport)):
        return False
    else:
        dic = {f.split(':')[0]:f.split(':')[1]   for f in fields}
        byr = len(dic['byr']) == 4 and int(dic['byr']) >= 1920 and int(dic['byr']) <= 2002
        iyr = len(dic['iyr']) == 4 and int(dic['iyr']) >= 2010 and int(dic['iyr']) <= 2020
        eyr = len(dic['eyr']) == 4 and int(dic['eyr']) >= 2020 and int(dic['eyr']) <= 2030
        hgt = (dic['hgt'][-2:] == 'cm' and int(dic['hgt'][:-2]) in range(150, 194) ) or (dic['hgt'][-2:] == 'in' and int(dic['hgt'][:-2]) in range(59, 77))
        hcl = dic['hcl'][0] == '#' and len(dic['hcl']) == 7 and all([l in '0123456789abcdef#' for l in dic['hcl']])
        ecl = dic['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        pid = len(dic['pid']) == 9
        return all([byr, iyr, eyr, hgt, hcl, ecl, pid])

line = 0
nb_valid_passports = 0

while line < len(batch):
    passport = ''
    while line < len(batch) and batch[line] != '':
        passport += ' ' + batch[line]
        line += 1

    if isValid(passport):
        nb_valid_passports += 1
    line += 1

print(nb_valid_passports)