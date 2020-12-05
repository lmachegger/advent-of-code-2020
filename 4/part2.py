# Day 4
# Part 2

# read in all lines
f = open('input1', 'r')
all_lines = [f.read().split('\n')][0]

# create array of data
data = []
chunk = ''
for line in all_lines:
    if not ':' in line:
        data.append(chunk)
        chunk = ''
    else:
        chunk = chunk + ' ' + line

# add last item
data.append(chunk)

# define class passport


class Passport:
    check_list = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

    def __init__(self, data):
        items = {}
        for item in data.split(' '):
            if ':' in item:
                items[item.split(':')[0]] = item.split(':')[1]

        self.data = items

    def is_valid(self):
        for key in self.check_list:
            if not key in self.data:
                return False

            if key == 'byr':
                try:
                    year = int(self.data[key])
                    if year < 1920 or year > 2002:
                        return False
                except ValueError:
                    return False

            elif key == 'iyr':
                try:
                    year = int(self.data[key])
                    if year < 2010 or year > 2020:
                        return False
                except ValueError:
                    return False

            elif key == 'eyr':
                try:
                    year = int(self.data[key])
                    if year < 2020 or year > 2030:
                        return False
                except ValueError:
                    return False

            elif key == 'hgt':
                val = self.data[key]
                if not 'in' in val and not 'cm' in val:
                    return False
                try:
                    height = int(val[:-2])
                    x = val[-2:]
                    if x == 'in':
                        if height < 59 or height > 76:
                            return False
                    if x == 'cm':
                        if height < 150 or height > 193:
                            return False
                except ValueError:
                    return False

            elif key == 'hcl':
                color = self.data[key]
                allowed_values = ['0', '1', '2', '3', '4', '5', '6', '7',
                                  '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
                if color[0] != '#' or len(color) != 7:
                    return False
                for i in range(1, len(color)):
                    if not color[i] in allowed_values:
                        return False

            elif key == 'ecl':
                allowed_values = ['amb', 'blu',
                                  'brn', 'gry', 'grn', 'hzl', 'oth']
                if not self.data[key] in allowed_values:
                    return False

            elif key == 'pid':
                pid = self.data[key]
                if len(pid) != 9:
                    return False
                if not pid.isdigit():
                    return False

        return True


# check every item in data
valid_count = 0
for item in data:
    p = Passport(item)
    if p.is_valid():
        valid_count += 1


print('valid passes: ',  valid_count)
