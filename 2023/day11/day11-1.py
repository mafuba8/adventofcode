#!/usr/bin/python3
# Advent of Code 2023 - Day 11, Part 1
# Benedikt Otto
import re
import itertools

# Open puzzle file.
#with open('example_11.txt') as file:
with open('../inputs/input_11.txt') as file:
    lines = file.readlines()

# Parse lines, double empty rows and remember columns without galaxy.
nonempty_cols = set()
lines2 = []
re_nogalaxy = re.compile(r'#')
for line in lines:
    a = line.strip()
    # Repeat lines without galaxy '#' once.
    if not re_nogalaxy.search(a):
        lines2.append(a)
    # Remember nonempty columns.
    for col, char in enumerate(line):
        if char == '#':
            nonempty_cols.add(col)
    lines2.append(a)

# Double empty columns
image_list = []
for line in lines2:
    a = ""
    for k in range(len(line)):
        if k in nonempty_cols:
            a += line[k]
        else:
            a += line[k] + '.'
    image_list.append(a)

# Get the list of tuples of all galaxies
galaxy_list = []
for row_num, row in enumerate(image_list):
    for col_num, char in enumerate(row):
        if char == '#':
            galaxy_list.append((row_num, col_num))

# Count the total distance of all pairs of galaxies.
total_distance = 0
num = 0
for pair in itertools.combinations(galaxy_list, 2):
    galaxy_1, galaxy_2 = pair

    # Distance between two galaxies is just the combined absolute difference of their coordinates.
    distance_row = abs(galaxy_1[0] - galaxy_2[0])
    distance_col = abs(galaxy_1[1] - galaxy_2[1])
    distance = distance_row + distance_col

    total_distance += distance
    num += 1

print(f'Total distance of {num} galaxies: {total_distance}')
