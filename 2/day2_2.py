# Day 2
# Part 2
with open('input2', 'r') as f:
    data = f.read().split('\n')


def check_line(pos_1, pos_2, character, password):
    count = 0
    if(password[pos_1 - 1] == character):
        count = count + 1
    if(password[pos_2 - 1] == character):
        count = count + 1

    return count == 1


result = 0
for line in data:
    l = line.split(' ')
    pos_1, pos_2 = l[0].split('-')
    character = l[1].split(':')[0]
    password = l[2]
    if check_line(int(pos_1), int(pos_2), character, password):
        result = result+1

print(result)
