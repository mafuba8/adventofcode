#!/usr/bin/python3
# Advent of Code 2025 - Day 4, Part 1
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


# Count the number of paper rolls that can be accessed.
accessible_count = 0
for xy in input_shelf:
    if input_shelf[xy] == '@' and count_neigh_paper(xy, input_shelf) < 4:
        accessible_count += 1

print(f'A total of {accessible_count} rolls of paper can be accessed by a forklift.')
