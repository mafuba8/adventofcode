#!/usr/bin/python3
# Advent of Code 2023 - Day 18, Part 1
# Benedikt Otto

# Open puzzle file and parse into list of tuples.
dig_plan = []
#with open('example_18.txt') as file:
with open('../inputs/input_18.txt') as file:
    lines = file.readlines()
    for line in lines:
        li = line.strip().split(' ')
        direction = li[0]
        length = int(li[1])
        color = li[2].replace('(', '').replace(')', '')
        dig_plan.append((direction, length, color))

print(dig_plan)

terrain = {}
pointer = (0, 0)
for instruction in dig_plan:
    (direction, length, color) = instruction
    step = (0, 0)
    match direction:
        case 'U':
            step = (-1, 0)
        case 'D':
            step = (1, 0)
        case 'L':
            step = (0, -1)
        case 'R':
            step = (0, 1)
    for k in range(length):
        pointer = (pointer[0] + step[0], pointer[1] + step[1])
        terrain.setdefault(pointer, '#')


min_x = min([t[0] for t in terrain.keys()])
max_x = max([t[0] for t in terrain.keys()])
min_y = min([t[1] for t in terrain.keys()])
max_y = max([t[1] for t in terrain.keys()])


def is_inside(point_x, point_y):
    """Checks if the given point is inside the loop given by the terrain.
    Doesn't work for points on the border itself."""
    # Count total crossings on the line of symbols from the point to the northern border.
    crossings = 0
    from_left = False
    from_right = False
    for k in range(min_x, point_x):
        # Look at the symbol and the symbols left/right of it.
        symbol_c = terrain.get((k, point_y)) == '#'
        symbol_l = terrain.get((k, point_y - 1)) == '#'
        symbol_r = terrain.get((k, point_y + 1)) == '#'

        # Patterns in the form '###' are always crossings.
        if symbol_l and symbol_c and symbol_r:
            crossings += 1
            continue

        # Patterns in the form '-##' or '##-' are only crossings if the there has previously been
        #  an opposite pattern '##-' or '-##'. We remember that with the from_left and from_right vars.
        if symbol_c and symbol_r:
            if from_left:
                crossings += 1
                from_left = False
                continue
            if from_right:
                from_right = False
            else:
                from_right = True

        if symbol_c and symbol_l:
            if from_right:
                crossings += 1
                from_right = False
                continue
            if from_left:
                from_left = False
            else:
                from_left = True
    # The point is an inner point iff there is an odd number of crossings.
    return crossings % 2 == 1


# Count total square meters.
total_sqm = 0
total_sqm += len(terrain)  # Count the squares on the border.
for x in range(min_x, max_x + 1):
    for y in range(min_y, max_y + 1):
        if (x, y) in terrain:  # Points on the border are already accounted for.
            continue
        if is_inside(x, y):
            total_sqm += 1

print(total_sqm)
