# Day 4
# Part 2
import re

with open('4/input4', 'r') as f:
    all_lines = f.read().split('\n\n')

passports = []
for line in all_lines:
    passports.append(line.replace('\n', ' ').split(' '))


def check_byr(s):
    return 1920 <= int(s) <= 2002


def check_iyr(s):
    return 2010 <= int(s) <= 2020


def check_eyr(s):
    return 2020 <= int(s) <= 2030


def check_hgt(s):
    height = re.match(r'^(\d{1,})(cm|in)$', s)
    if height:
        if height[2] == 'cm' and 150 <= int(height[1]) <= 193:
            return True
        elif height[2] == 'in' and 59 <= int(height[1]) <= 76:
            return True
    return False


def check_hcl(s):
    return re.match(r'#[a-f0-9]{6}', s)


def check_ecl(s):
    ecls = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    return s in ecls


def check_pid(s):
    return len(s) == 9 and re.match(r'[0-9]{9}', s)


check_list = {'byr': check_byr,
              'iyr': check_iyr,
              'eyr': check_eyr,
              'hgt': check_hgt,
              'hcl': check_hcl,
              'ecl': check_ecl,
              'pid': check_pid}

counter = 0
for pp in passports:
    d = dict(i.split(':') for i in pp)
    if all(vals in d for vals in check_list):
        all_checks_correct = True
        for item in check_list:
            func = check_list[item]
            if not func(d[item]):
                all_checks_correct = False
        if all_checks_correct:
            counter += 1

print(counter)
