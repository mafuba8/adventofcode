#!/usr/bin/python3
# Advent of Code 2023 - Day 11, Part 2
# Benedikt Otto
import re
import itertools

# Open puzzle file.
#with open('example_11.txt') as file:
with open('input_11.txt') as file:
    lines = file.readlines()

# Parse lines, remember rows without a galaxy and columns with one.
empty_rows = set()
nonempty_cols = set()
re_nogalaxy = re.compile(r'#')
for row_num, row in enumerate(lines):
    a = row.strip()
    # Remember the row_num of empty rows.
    if not re_nogalaxy.search(a):
        empty_rows.add(row_num)
    # Remember columns with a galaxy.
    for col_num, char in enumerate(a):
        if char == '#':
            nonempty_cols.add(col_num)

# Get set of columns without a galaxy.
empty_cols = []
for k in range(len(lines[0]) - 1):  # accounting for the newline at the end.
    if k not in nonempty_cols:
        empty_cols.append(k)

# Get the list of tuples of all galaxies
galaxy_list = []
for row_num, row in enumerate(lines):
    row = row.strip()
    for col_num, char in enumerate(row):
        if char == '#':
            galaxy_list.append((row_num, col_num))


def count_empty_rows(start, end):
    """Count empty rows between row <start> and row <end>, not inclusive."""
    count = 0
    ma = max(start, end)
    mi = min(start, end)
    for k in range(mi + 1, ma):
        if k in empty_rows:
            count += 1
    return count


def count_empty_cols(start, end):
    """Count empty columns between column <start> and column <end>, not inclusive."""
    count = 0
    ma = max(start, end)
    mi = min(start, end)
    for k in range(mi + 1, ma):
        if k in empty_cols:
            count += 1
    return count


# Number of additional empty rows and columns to add between galaxies.
# Note: the text says 'x times MORE', so for 100x more we need 99 additional lines.
EXPANSION = 1000000 - 1

# Count the total distance of all pairs of galaxies.
total_distance = 0
num = 0
for pair in itertools.combinations(galaxy_list, 2):
    galaxy_1, galaxy_2 = pair

    # Normal distance plus <expansion> many additional steps for each empty row.
    empty_row_count = count_empty_rows(galaxy_1[0], galaxy_2[0])
    empty_col_count = count_empty_cols(galaxy_1[1], galaxy_2[1])
    distance_row = abs(galaxy_1[0] - galaxy_2[0]) + EXPANSION * empty_row_count
    distance_col = abs(galaxy_1[1] - galaxy_2[1]) + EXPANSION * empty_col_count
    distance = distance_row + distance_col

    total_distance += distance
    num += 1

print(f'Total distance of {num} galaxies: {total_distance}')
