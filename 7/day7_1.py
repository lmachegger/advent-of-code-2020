# Day 7
# Part 1
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
        tree[color_main] = []


# recursive search for gold bags
def find_gold_bag(col):
    if col == 'shiny gold':
        return True
    else:
        return any(find_gold_bag(child) for amount, child in tree[col])


# -1 for the bag that is shiny gold itself
print(sum(find_gold_bag(color) for color in tree.keys()) - 1)
