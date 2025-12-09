#!/usr/bin/python3
# Advent of Code 2025 - Day 9, Part 1
# Benedikt Otto
#

# INPUT_FILE = '../examples/example_09.txt'
INPUT_FILE = '../inputs/input_09.txt'

# Parse input into a list of coordinates.
red_tiles = []
with open(INPUT_FILE) as file:
    for line in file.readlines():
        coord = line.strip().split(',')
        coord = tuple(map(int, coord))
        red_tiles.append(coord)

def rectangle_area(corner_1, corner_2):
    """Calculates the area of the rectangle with the two given opposite corners."""
    x1, y1 = corner_1
    x2, y2 = corner_2
    return (max(x1, x2) - min(x1, x2) + 1) * (max(y1, y2) - min(y1, y2) + 1)


# Run through all combinations of corners and find the largest area.
largest_area = 0
for coord_1 in red_tiles:
    for coord_2 in red_tiles:
        a = rectangle_area(coord_1, coord_2)
        if a > largest_area:
            largest_area = a

print(f'Largest area: {largest_area}.')
