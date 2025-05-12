#!/usr/bin/python3
# Advent of Code 2021 - Day 5, Part 1
# Benedikt Otto
#
import re

# input_file = '../examples/example_5.txt'
input_file = '../inputs/input_5.txt'

# Parse input into list of vents.
vent_list = []
regex = re.compile(r'^(\d+),(\d+)\s->\s(\d+),(\d+)$')
with open(input_file) as file:
    for line in file.readlines():
        search = regex.search(line)
        x1, y1 = int(search.group(1)), int(search.group(2))
        x2, y2 = int(search.group(3)), int(search.group(4))

        # Ensure that always x1 <= x2 and y1 <= y2.
        if x1 > x2:
            x1, x2 = x2, x1
        if y1 > y2:
            y1, y2 = y2, y1

        # Only horizontal or vertical lines.
        if x1 == x2 or y1 == y2:
            vent = (x1, x2, y1, y2)
            vent_list.append(vent)


# Dictionary with key=(x, y), val=num(vents).
vent_spots = {}
for vent in vent_list:
    x1, x2, y1, y2 = vent
    # Horizontal vents.
    if x1 == x2:
        for y in range(y1, y2 + 1):
            c = (x1, y)
            if c in vent_spots:
                vent_spots[c] += 1
            else:
                vent_spots.setdefault(c, 1)
    # Vertical vents.
    elif y1 == y2:
        for x in range(x1, x2 + 1):
            c = (x, y1)
            if c in vent_spots:
                vent_spots[c] += 1
            else:
                vent_spots.setdefault(c, 1)


# Get number of vent spots with at least two vents.
danger_spots = [c for c in vent_spots if vent_spots[c] > 1]
print(f'Danger spots: {danger_spots}')
print(f'Number of danger spots: {len(danger_spots)}')
