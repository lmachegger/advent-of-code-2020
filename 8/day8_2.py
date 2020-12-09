# Day 8
# Part 2
with open('8/input8', 'r') as f:
    lines_original = f.read().split('\n')

finished = False
changed_lines_ids = [-1]
while not finished:
    lines = lines_original.copy()

    for i in range(len(lines)):
        arg = lines[i].split(' ')[0]

        if (arg == 'jmp' or arg == 'nop'):
            if i in changed_lines_ids:
                continue
            changed_lines_ids.append(i)
            if arg == 'jmp':
                lines[i] = lines[i].replace('jmp', 'nop')
            else:
                lines[i] = lines[i].replace('nop', 'jmp')
            break

    acc = 0
    idx = 0
    performed_lines = []
    while True:
        if idx > len(lines) - 1:
            finished = True
            break

        arg, val = lines[idx].split()

        if idx not in performed_lines:
            performed_lines.append(idx)
        else:
            break

        if arg == 'acc':
            acc += int(val)
            idx += 1
        elif arg == 'jmp':
            idx += int(val)
        elif arg == 'nop':
            idx += 1


print('acc:', acc)
