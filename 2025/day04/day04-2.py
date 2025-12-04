#!/usr/bin/python3
# Advent of Code 2025 - Day 4, Part 2
# Benedikt Otto
#

# INPUT_FILE = '../examples/example_04.txt'
INPUT_FILE = '../inputs/input_04.txt'

# Parse input into a dict.
input_shelf = {}
with open(INPUT_FILE) as file:
    for row_num, line in enumerate(file.readlines()):
        for col_num, char in enumerate(line.strip()):
            input_shelf[(row_num, col_num)] = char


def count_neigh_paper(xy_coord, shelf_dict):
    """Returns the number of paper rolls in the eight adjacent tiles of xy_coord."""
    x, y = xy_coord
    count = 0
    for neigh in [(x-1, y-1), (x-1, y), (x-1, y+1), (x, y-1), (x, y+1), (x+1, y-1), (x+1, y), (x+1, y+1)]:
        if neigh in shelf_dict and shelf_dict[neigh] == '@':
            count += 1
    return count


# In each step, remove all accessible paper rolls and count them.
shelf = input_shelf
count_removed = 0
paper_removed = True
while paper_removed:
    new_shelf = {}
    paper_removed = False

    for xy in shelf:
        if shelf[xy] == '@' and count_neigh_paper(xy, shelf) < 4:
            new_shelf[xy] = '.'
            paper_removed = True
            count_removed += 1
        else:
            new_shelf[xy] = shelf[xy]

    shelf = new_shelf

print(f'A total of {count_removed} paper rolls can be removed by forklifts.')
