# Day 1
# Part 1
f = open("input", "r")
data = [int(line) for line in f.read().split('\n')]

for i in range(len(data)):
    for j in range(i, len(data)):
        for k in range(j, len(data)):
            if i == j or i == k or j == k:
                continue
            if data[i] + data[j] + data[k] == 2020:
                print(data[i] * data[j] * data[k])
