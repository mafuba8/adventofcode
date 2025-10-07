#!/usr/bin/python3
# Advent of Code 2020 - Day 3, Part 1
# Benedikt Otto
#

# input_file = '../examples/example_3.txt'
input_file = '../inputs/input_3.txt'

# Parse input into a dict of chars.
map_dict = {}
with open(input_file) as file:
    for row, line in enumerate(file.readlines()):
        for col, char in enumerate(line.strip()):
            map_dict[(row, col)] = char

# Get maximum width.
max_x = max(pos[0] for pos in map_dict)
max_y = max(pos[1] for pos in map_dict)

tree_count = 0
pos_x, pos_y = 0, 0
while pos_x < max_x:
    # Move toboggan, accounting for wrapping along y coordinate.
    pos_x = pos_x + 1
    pos_y = (pos_y + 3) % (max_y + 1)

    # Check if we hit a tree.
    tile = map_dict[(pos_x, pos_y)]
    if tile == '#':
        tree_count += 1

print(f'With a trajectory of (1, 3), we hit {tree_count} trees.')
