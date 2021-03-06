# Day 8
# Part 1
with open('8/input8', 'r') as f:
    lines = f.read().split('\n')

acc = 0
idx = 0
performed_lines = []
while True:
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

print(acc)
