#!/usr/bin/python3
# Advent of Code 2025 - Day 9, Part 2
# Benedikt Otto
#

# INPUT_FILE = '../examples/example_09.txt'
INPUT_FILE = '../inputs/input_09.txt'

# Parse input into a list of coordinates.
red_tiles = []
with open(INPUT_FILE) as file:
    for line in file.readlines():
        coord = line.strip().split(',')
        coord = (int(coord[0]), int(coord[1]))
        red_tiles.append(coord)


# Create list of all border pairs.
border_pairs = []
for k in range(len(red_tiles)):  # This also adds the pair (last,first) to the list.
    b = (red_tiles[k-1], red_tiles[k])
    border_pairs.append(b)

# Create set of all border points.
border_points = set()
for b1, b2 in border_pairs:
    if b1[0] == b2[0]:
        for k in range(min(b1[1], b2[1]), max(b1[1], b2[1]) + 1):
            p = (b1[0], k)
            border_points.add(p)
    elif b1[1] == b2[1]:
        for k in range(min(b1[0], b2[0]), max(b1[0], b2[0]) + 1):
            p = (k, b1[1])
            border_points.add(p)


def rectangle_area(corner_1, corner_2):
    """Calculates the area of the rectangle with the two given opposite corners."""
    x1, y1 = corner_1
    x2, y2 = corner_2
    return (max(x1, x2) - min(x1, x2) + 1) * (max(y1, y2) - min(y1, y2) + 1)


# Make a list of all possible rectangles.
rectangles = []
for coord_1 in red_tiles:
    for coord_2 in red_tiles:
        a = rectangle_area(coord_1, coord_2)
        rectangle = (a, (coord_1, coord_2))
        rectangles.append(rectangle)

# Sort the list by area.
rectangles.sort(key=lambda t: t[0])


def inside_coloured_area(corner_1, corner_2):
    """Checks if a given rectangle is fully within the coloured area."""
    # Ensure that x1 < x2 and y1 < y2.
    x1, x2 = min(corner_1[0], corner_2[0]), max(corner_1[0], corner_2[0])
    y1, y2 = min(corner_1[1], corner_2[1]), max(corner_1[1], corner_2[1])

    # A rectangle can only be within the coloured area if there is no border point
    # inside the rectangle.
    for b in border_points:
        if (x1 < b[0] < x2) and (y1 < b[1] < y2):
            return False
    return True


# Starting with the largest rectangle, check if it is inside the coloured area.
while True:
    a, corners = rectangles.pop()
    c1, c2 = corners
    if inside_coloured_area(c1, c2):
        break

print(f'Smallest rectangle within coloured area: {c1, c2} - Area: {a}')
