#!/usr/bin/python3
# Advent of Code 2025 - Day 12, Part 1
# Benedikt Otto
#

# INPUT_FILE = '../examples/example_12.txt'
INPUT_FILE = '../inputs/input_12.txt'


# Parse input.
shapes = []
regions = []
with open(INPUT_FILE) as file:
    shape_part = False
    shape_row = 0
    shape = {}
    for line in file.readlines():
        if line == '\n':
            shapes.append(shape)
            shape = {}
        elif line[1] == ':':
            shape_row = 0
        elif '#' in line or '.' in line:
            for col_num, char in enumerate(line.strip()):
                shape[(shape_row, col_num)] = char
            shape_row += 1
        else:  # List of regions.
            raw_region_size, raw_region_counts = line.strip().split(': ')
            r_size = tuple(int(s) for s in raw_region_size.split('x'))
            r_counts = list(int(s) for s in raw_region_counts.split(' '))
            regions.append((r_size, r_counts))


# As it turns out, the input is so generously crafted that you don't have to bother with
# any arrangements at all. Checking whether there are enough spots in each region or not is enough.
valid_regions = 0
for region_size, region_counts in regions:
    free_spaces = region_size[0] * region_size[1]
    print(region_size, region_counts)
    for shape_idx, shape_count in enumerate(region_counts):
        shape_occupied_tiles = len([xy for xy in s if s[xy] == '#'])
        free_spaces -= shape_count * shape_occupied_tiles
    if free_spaces >= 0:
        valid_regions += 1

print(f'Number of valid regions: {valid_regions}')
