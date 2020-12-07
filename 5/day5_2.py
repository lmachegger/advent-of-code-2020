# Day 5
# Part 2
with open('input5', 'r') as f:
    all_lines = [f.read().split('\n')][0]

results = []

for line in all_lines:
    binary = line.replace('F', '0').replace(
        'B', '1').replace('L', '0').replace('R', '1')
    row, seat = binary[:7], binary[7:]
    results.append(int(row, 2) * 8 + int(seat, 2))

results.sort()
idx = results[0]
for result in results:
    if result != idx:
        print(idx)
        break
    idx += 1
