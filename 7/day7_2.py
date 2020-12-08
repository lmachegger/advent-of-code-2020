# Day 7
# Part 2
import re

with open('7/input7', 'r') as f:
    all_lines = f.read().split('\n')

tree = {}

# build tree
for line in all_lines:
    color_main = re.match(r'(.+?) bags', line).group(1)
    color_children = re.findall(r'(\d+) (.+?) bag', line)

    # only if color_main has children
    if(len(color_children) > 0):
        tree[color_main] = color_children
    else:
        tree[color_main] = [('0', '')]


def count(col):
    if col == '':
        return 1
    return 1 + sum(int(amount) * count(child) for amount, child in tree[col])


# because of INSIDE shiny gold bag (excluding itself)
print(count('shiny gold') - 1)
