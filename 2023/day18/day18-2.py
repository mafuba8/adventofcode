#!/usr/bin/python3
# Advent of Code 2023 - Day 18, Part 2
# Benedikt Otto

# Open puzzle file and parse into list of tuples.
dig_plan = []
#with open('example_18.txt') as file:
with open('input_18.txt') as file:
    lines = file.readlines()
    for line in lines:
        li = line.strip().split(' ')
        color = li[2].replace('(', '').replace(')', '')

        hex_str = color[1:6]
        length = int(hex_str, 16)

        match color[6]:
            case '0':
                direction = 'R'
            case '1':
                direction = 'D'
            case '2':
                direction = 'L'
            case '3':
                direction = 'U'

        dig_plan.append((direction, length))


# List of all points on the boundary.
boundary = set()
pointer = (0, 0)
for instruction in dig_plan:
    (direction, length) = instruction
    match direction:
        case 'U':
            step = (-1, 0)
        case 'D':
            step = (1, 0)
        case 'L':
            step = (0, -1)
        case 'R':
            step = (0, 1)
        case _:
            step = (0, 0)
    for k in range(length):
        pointer = (pointer[0] + step[0], pointer[1] + step[1])
        boundary.add(pointer)


# List of edges of the polygon.
edges = []
pointer = (0, 0)
for instruction in dig_plan:
    (direction, length) = instruction
    match direction:
        case 'U':
            pointer = (pointer[0] - length, pointer[1])
        case 'D':
            pointer = (pointer[0] + length, pointer[1])
        case 'L':
            pointer = (pointer[0], pointer[1] - length)
        case 'R':
            pointer = (pointer[0], pointer[1] + length)
    edges.append(pointer)


def det(a, b, c, d):
    """2x2 determinant of the matrix
    (a b)
    (c d) ."""
    return a * d - b * c


# Determine the area of the polygon given by the edges using the shoelace formula.
print(edges)
a = 0
prev_edge = edges[-1]
for edge in edges:
    a += det(prev_edge[0], edge[0], prev_edge[1], edge[1])
    prev_edge = edge

area = abs(a)/2
print(f'The area of the polygon is {area}')

# Use Pick's theorem to determine the number of interior points.
num_boundary = len(boundary)
num_interior = area - num_boundary/2 + 1

print(f'Number of interior/boundary points: {num_interior}/{num_boundary}')
print(f'Total number of points: {int(num_boundary + num_interior)}')
