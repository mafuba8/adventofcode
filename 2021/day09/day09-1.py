#!/usr/bin/python3
# Advent of Code 2021 - Day 9, Part 1
# Benedikt Otto
#

# input_file = '../examples/example_9.txt'
input_file = '../inputs/input_9.txt'

# Parse input into dict(key=xy, val=char).
height_map = {}
with open(input_file) as file:
    for row_num, row in enumerate(file.readlines()):
        for col_num, char in enumerate(row.strip()):
            coord = (row_num, col_num)
            height_map.setdefault(coord, int(char))


def is_low_point(coord):
    x, y = coord
    base_val = height_map[coord]

    for c in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
        if c in height_map and base_val >= height_map[c]:
            return False
    return True


# Run through all points and count the low points.
low_point_count = 0
risk_level_sum = 0
for coord in height_map:
    if is_low_point(coord):
        low_point_count += 1
        risk_level = height_map[coord] + 1
        risk_level_sum += risk_level
        print(f'Low point at {coord} (risk level: {risk_level})')

print(f'Number of low points: {low_point_count}.')
print(f'Sum of risk levels: {risk_level_sum}')
