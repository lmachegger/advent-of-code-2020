# Day 3
# Part 2
f = open('input1', 'r')

data = [f.read().split('\n')]
data = data[0]

x_slopes = [1, 3, 5, 7, 1]
y_slopes = [1, 1, 1, 1, 2]
width = len(data[0])

counts_of_trees = []


def move(x, y, x_slope, y_slope):
    reached_bottom = False

    if(x + x_slope > width - 1):
        x = x + x_slope - width  # - 1
    else:
        x = x + x_slope

    if y + y_slope > len(data) - 1:
        reached_bottom = True
        counts_of_trees.append(count_of_trees)
    else:
        y = y + y_slope

    return x, y, reached_bottom


def count_trees(x_pos, y_pos, c):
    line = data[y_pos]
    if line[x_pos] == '#':
        c = c + 1

    return c


for x_slope, y_slope in zip(x_slopes, y_slopes):
    reached_bottom = False
    count_of_trees = 0
    x_pos = 0
    y_pos = 0

    while(not reached_bottom):
        x_pos, y_pos, reached_bottom = move(
            x_pos, y_pos, x_slope, y_slope)

        if(not reached_bottom):
            count_of_trees = count_trees(x_pos, y_pos, count_of_trees)

print('tree-counts: ', counts_of_trees)
result = counts_of_trees[0]
for i in range(1, len(counts_of_trees)):
    result = result * counts_of_trees[i]

print('result: ', result)
