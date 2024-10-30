#!/usr/bin/python3
# Advent of Code 2022 - Day 8, Part 1
# Benedikt Otto

# input_file = '../examples/example_8.txt'
input_file = '../inputs/input_8.txt'

# Parse input into dict.
forest = {}
forest_height = 0
forest_width = 0
with open(input_file) as file:
    for row_num, row in enumerate(file.readlines()):
        for col_num, c in enumerate(row.strip()):
            forest.setdefault((row_num, col_num), int(c))
        forest_width = col_num + 1
    forest_height = row_num + 1

# Trees that are visible from left or right.
vis_left = []
vis_right = []
for x in range(0, forest_height):
    # Start at side and compare tree size with current level.
    tree_level = -1
    for y in range(0, forest_width):
        tree = (x, y)
        if forest[tree] > tree_level:
            vis_left.append(tree)
            tree_level = forest[tree]

    tree_level = -1
    for y in reversed(range(0, forest_width)):
        tree = (x, y)
        if forest[tree] > tree_level:
            vis_right.append(tree)
            tree_level = forest[tree]

# Trees that are visible from top or bottom.
vis_top = []
vis_bot = []
for y in range(0, forest_width):
    # Start at side and compare tree size with current level.
    tree_level = -1
    for x in range(0, forest_height):
        tree = (x, y)
        if forest[tree] > tree_level:
            vis_top.append(tree)
            tree_level = forest[tree]

    tree_level = -1
    for x in reversed(range(0, forest_height)):
        tree = (x, y)
        if forest[tree] > tree_level:
            vis_bot.append(tree)
            tree_level = forest[tree]


# Trees that are visible from any direction.
visible_trees = set(vis_left + vis_right + vis_top + vis_bot)
print(f'Number of trees that are visible: {len(visible_trees)}')
