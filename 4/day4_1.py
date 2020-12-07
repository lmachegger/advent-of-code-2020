# Day 4
# Part 1

with open('input4', 'r') as f:
    all_lines = f.read().split('\n\n')

passports = []
for line in all_lines:
    passports.append(line.replace('\n', ' ').split(' '))

check_list = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

counter = 0
for pp in passports:
    d = dict(i.split(':') for i in pp)
    if all(vals in d for vals in check_list):
        counter += 1

print(counter)
print(len(passports))
