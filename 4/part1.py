# Day 4
# Part 1

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

# list of items that need to be in pass
check_list = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']


# check function
def check_pass(fields):
    for item in check_list:
        if not item in fields:
            return False
    return True


# check every item in data
valid_count = 0
for item in data:
    if check_pass(item):
        valid_count += 1

print('valid passes: ',  valid_count)
