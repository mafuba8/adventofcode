#!/usr/bin/python3
# Advent of Code 2022 - Day 8, Part 2
# Benedikt Otto

# input_file = '../examples/example_8.txt'
input_file = '../inputs/input_8.txt'

# Parse input into dict {(x, y): tree_height}
forest = {}
forest_height = 0
forest_width = 0
with open(input_file) as file:
    for row_num, row in enumerate(file.readlines()):
        for col_num, c in enumerate(row.strip()):
            forest.setdefault((row_num, col_num), int(c))
        forest_width = col_num + 1
    forest_height = row_num + 1


def scenic_score(base_tree):
    """Returns the scenic score of a given tree (tuple)."""
    x, y = base_tree
    total_score = 1

    # UP / DOWN
    v = y
    score = 0
    for u in reversed(range(0, x)):
        tree = (u, v)
        score += 1
        if forest[tree] >= forest[(x, y)]:
            break
    total_score *= score

    score = 0
    for u in range(x+1, forest_height):
        tree = (u, v)
        score += 1
        if forest[tree] >= forest[(x, y)]:
            break
    total_score *= score

    # LEFT/RIGHT
    u = x
    score = 0
    for v in reversed(range(0, y)):
        tree = (u, v)
        score += 1
        range(y + 1, forest_width)
        if forest[tree] >= forest[(x, y)]:
            break
    total_score *= score

    score = 0
    for v in range(y+1, forest_width):
        tree = (u, v)
        score += 1
        if forest[tree] >= forest[(x, y)]:
            break
    total_score *= score
    return total_score


# Determine the scenic score of all trees and find a tree with maximum score.
max_score = 0
max_tree = (0, 0)
for x in range(forest_height):
    for y in range(forest_width):
        tree = (x, y)
        score = scenic_score(tree)
        print(f'Tree: {tree} - Score: {score}')
        if score > max_score:
            max_tree = tree
            max_score = score

print(f'A tree with a maximum scenic score is {max_tree} with a score of {max_score}.')
