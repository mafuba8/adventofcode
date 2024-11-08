#!/usr/bin/python3
# Advent of Code 2022 - Day 14, Part 1
# Benedikt Otto
import re

# input_file = '../examples/example_14.txt'
input_file = '../inputs/input_14.txt'

regex = re.compile(r'(\d+),(\d+)')

# Parse input into dict of pixels.
area = {}

def print_area():
    """ Prints the area."""
    min_x = min([t[0] for t in area.keys()])
    min_y = min([t[1] for t in area.keys()])
    max_x = max([t[0] for t in area.keys()])
    max_y = max([t[1] for t in area.keys()])

    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            if (x, y) in area:
                print(area[(x, y)], end='')
            else:
                print('.', end='')
        print()
    print()

def draw_pixels(x_from, x_to, y_from, y_to):
    """ Puts a '#' on every pixel in area on the line defined by the x/y ranges. """
    x_min, x_max = min(x_from, x_to), max(x_from, x_to)
    y_min, y_max = min(y_from, y_to), max(y_from, y_to)
    for x in range(x_min, x_max + 1):
        for y in range(y_min, y_max + 1):
            area.setdefault((x, y), '#')


# Parse input into the area dict.
with open(input_file) as file:
    for line in file.readlines():
        l = regex.findall(line)
        l = [(int(s1), int(s2)) for (s1, s2) in l]
        lx, ly = l[0]
        for x, y in l[1:]:
            draw_pixels(x, lx, y, ly)
            lx, ly = x, y

# Lower end of all wall pixels. Any pixel past that drops indefinitely ('abyss').
lower_end = max([t[1] for t in area.keys()])

# Simulate the movement of the sand
no_abyss = True
while no_abyss:
    no_rest = True
    sand = (500, 0)
    while no_rest and no_abyss:
        # Check if the sand has dropped past the lowest level of walls.
        if sand[1] >= lower_end:
            no_abyss = False
            break

        if (sand[0], sand[1] + 1) not in area:
            # Pixel below is free.
            sand = (sand[0], sand[1] + 1)
        elif (sand[0] - 1, sand[1] + 1) not in area:
            # Pixel below-left is free.
            sand = (sand[0] - 1, sand[1] + 1)
        elif (sand[0] + 1, sand[1] + 1) not in area:
            # Pixel below-right is free.
            sand = (sand[0] + 1, sand[1] + 1)
        else:
            # No free pixel, sand comes to rest
            no_rest = False
    area.setdefault(sand, 'o')

# Remove the sand pixel that dropped into the abyss.
del area[sand]

print("Final area:")
print_area()

print(f'Pixels with sand:')
sand_count = 0
for pixel in area:
    if area[pixel] == 'o':
        sand_count += 1

print(f'Units of sand: {sand_count}')
