# Day 3
# Part 1
with open('input3', 'r') as f:
    data = [f.read().split('\n')]

data = data[0]

x_pos = 0
y_pos = 0

x_slope = 3
y_slope = 1
width = len(data[0])

count_of_trees = 0
reached_bottom = False


def move(x, y, x_slope, y_slope):
    reached_bottom = False

    if(x + x_slope > width - 1):
        x = x + x_slope - width  # - 1
    else:
        x = x + x_slope

    if y + y_slope > len(data) - 1:
        reached_bottom = True
        print(count_of_trees)
    else:
        y = y + y_slope

    return x, y, reached_bottom


def count_trees(x_pos, y_pos, c):
    line = data[y_pos]
    if line[x_pos] == '#':
        c = c + 1

    return c


while(not reached_bottom):
    x_pos, y_pos, reached_bottom = move(
        x_pos, y_pos, x_slope, y_slope)

    if(not reached_bottom):
        count_of_trees = count_trees(x_pos, y_pos, count_of_trees)
