#!/usr/bin/python3
# Advent of Code 2021 - Day 5, Part 2
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

        vent = (x1, x2, y1, y2)
        vent_list.append(vent)


# Dictionary with key=(x, y), val=num(vents).
vent_spots = {}

def record_vent(coord):
    global vent_spots
    if coord in vent_spots:
        vent_spots[coord] += 1
    else:
        vent_spots.setdefault(coord, 1)


for vent in vent_list:
    x1, x2, y1, y2 = vent
    # Horizontal vents.
    if x1 == x2:
        if y1 > y2:
            y1, y2 = y2, y1  # ensure that always y1 <= y2.
        for y in range(y1, y2 + 1):
            record_vent((x1, y))

    # Vertical vents.
    elif y1 == y2:
        if x1 > x2:
            x1, x2 = x2, x1  # ensure that always x1 <= x2.
        for x in range(x1, x2 + 1):
            record_vent((x, y1))

    # Diagonal vents.
    else:
        # Direction of diagonal step.
        sx = 1
        if x1 > x2:
            sx = -1
        sy = 1
        if y1 > y2:
            sy = -1
        step = (sx, sy)

        # Add step vector and record the vent.
        c = (x1, y1)
        record_vent(c)
        n = abs(x2 - x1)  # number of points on diagonal.
        for k in range(n):
            c = (c[0] + step[0], c[1] + step[1])
            record_vent(c)


# Get number of vent spots with at least two vents.
danger_spots = [c for c in vent_spots if vent_spots[c] > 1]
print(f'Danger spots: {danger_spots}')
print(f'Number of danger spots: {len(danger_spots)}')
