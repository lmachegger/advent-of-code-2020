# Day 1
# Part 1
with open("1/input1", "r") as f:
    data = [int(line) for line in f.read().split('\n')]

for i in range(len(data)):
    for j in range(i, len(data)):
        if i == j:
            continue
        if data[i] + data[j] == 2020:
            print(data[i] * data[j])
