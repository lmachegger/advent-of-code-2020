# Day 2
# Part 1
with open('input2', 'r') as f:
    data = f.read().split('\n')


def check_line(count_min, count_max, character, password):
    count = password.count(character)
    return count <= count_max and count >= count_min


result = 0
for line in data:
    l = line.split(' ')
    count_min, count_max = l[0].split('-')
    character = l[1].split(':')[0]
    password = l[2]
    if check_line(int(count_min), int(count_max), character, password):
        result = result+1

print(result)
