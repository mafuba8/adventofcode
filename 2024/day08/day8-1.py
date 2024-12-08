#!/usr/bin/python3
# Advent of Code 2024 - Day 8, Part 1
# Benedikt Otto
#
import itertools

# input_file = '../examples/example_8.txt'
input_file = '../inputs/input_8.txt'

# Parse input into dict(key=xy, val=char).
area = {}
antennas = {}
with open(input_file) as file:
    for row_num, row in enumerate(file.readlines()):
        for col_num, char in enumerate(row.strip()):
            area.setdefault((row_num, col_num), char)
            if char != '.':
                antennas.setdefault(char, [])
                antennas[char].append((row_num, col_num))


# Find all antinodes of the antennas:
antinode_set = set()
for antenna in antennas:
    for antenna_pair in itertools.combinations(antennas[antenna], 2):
        a1, a2 = antenna_pair

        # We calculate the difference vector between a1 and a2.
        diff_x = a2[0] - a1[0]
        diff_y = a2[1] - a1[1]

        # The two antinodes are at coordinates 'a1 - diff' and 'a1 + 2*diff'.
        antinode_1 = (a1[0] - diff_x, a1[1] - diff_y)
        antinode_2 = (a1[0] + 2 * diff_x, a1[1] + 2 * diff_y)

        # Add the antinodes that are within the area.
        if antinode_1 in area:
            antinode_set.add(antinode_1)
        if antinode_2 in area:
            antinode_set.add(antinode_2)


print(f'Number of unique antinode locations within the map: {len(antinode_set)}')
