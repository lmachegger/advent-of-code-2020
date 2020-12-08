
with open('8/input8', 'r') as f:
    lines = f.read().split('\n')

changed_lines_ids = []

for i in range(len(lines)):
    arg = lines[i].split(' ')[0]
    print(i)
    if (arg == 'jmp' or arg == 'nop') and not i in changed_lines_ids:
        changed_lines_ids.append(i)
        if arg == 'jmp':
            lines[i].replace('jmp', 'nop')
        else:
            lines[i].replace('nop', 'jmp')
