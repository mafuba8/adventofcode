#!/usr/bin/python3
# Advent of Code 2024 - Day 8, Part 2
# Benedikt Otto
#
import itertools

# input_file = '../examples/example_8.txt'
input_file = '../inputs/input_8.txt'

# Parse input into dicts.
area = {}  # dict(key=xy, val=char)
antennas = {}  # dict(key=frequency, val=list(antennas with this freq.))
with open(input_file) as file:
    for row_num, row in enumerate(file.readlines()):
        for col_num, char in enumerate(row.strip()):
            area.setdefault((row_num, col_num), char)
            if char != '.':
                # Add this antenna to the list of antennas with the same frequency (character).
                antennas.setdefault(char, [])
                antennas[char].append((row_num, col_num))


# Find all antinodes created by all antenna pairs of the same frequency.
antinode_set = set()
for antenna in antennas:
    for antenna_pair in itertools.combinations(antennas[antenna], 2):
        a1, a2 = antenna_pair

        # We calculate the difference vector between a1 and a2.
        diff_x = a2[0] - a1[0]
        diff_y = a2[1] - a1[1]

        # Check all antinodes reached by adding k-multiples of the diff vector.
        k = 0
        within_area = True
        while within_area:
            antinode1 = (a1[0] + k * diff_x, a1[1] + k * diff_y)
            antinode2 = (a1[0] - k * diff_x, a1[1] - k * diff_y)

            # Check additional antinodes along the diagonal defined by diff until both
            # potential antinodes are outside the area.
            within_area = False
            if antinode1 in area:
                antinode_set.add(antinode1)
                within_area = True

            if antinode2 in area:
                antinode_set.add(antinode2)
                within_area = True

            k += 1


print(f'Number of unique antinode locations within the map: {len(antinode_set)}')
