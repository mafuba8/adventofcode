#!/usr/bin/python3
# Advent of Code 2021 - Day 22, Part 1
# Benedikt Otto
#
import re

# input_file = '../examples/example_22.txt'
input_file = '../inputs/input_22.txt'


class Cuboid:
    """Cuboid defined through the min and max values for each coordinate x, y, z."""
    def __init__(self, x_min, x_max, y_min, y_max, z_min, z_max):
        self.x_min = x_min
        self.y_min = y_min
        self.z_min = z_min
        self.x_max = x_max
        self.y_max = y_max
        self.z_max = z_max

    def __repr__(self):
        return f'Cuboid({self.x_min}, {self.x_max}, {self.y_min}, {self.y_max}, {self.z_min}, {self.z_max})'

    def inside(self, xyz):
        return (self.x_min <= xyz[0] <= self.x_max
                and self.y_min <= xyz[1] <= self.y_max
                and self.z_min <= xyz[2] <= self.z_max)


# Parse input into a list of cuboids.
cuboid_list = []
regex = re.compile(r'^(on|off)\sx=(-?\d+)\.\.(-?\d+),y=(-?\d+)\.\.(-?\d+),z=(-?\d+)\.\.(-?\d+)$')
with open(input_file) as file:
    for line in file.readlines():
        s = regex.search(line)
        c_state = s[1]
        cx_min, cx_max = int(s[2]), int(s[3])
        cy_min, cy_max = int(s[4]), int(s[5])
        cz_min, cz_max = int(s[6]), int(s[7])
        cuboid_list.append((c_state, Cuboid(cx_min, cx_max, cy_min, cy_max, cz_min, cz_max)))


def check_on(xyz):
    """Checks if the cube at xyz is on after applying all instructions."""
    global cuboid_list
    is_on = False
    for state, cuboid in cuboid_list:
        if cuboid.inside(xyz):
            is_on = (state == 'on')
    return is_on

# The inefficient method: Run through all 100x100x100 cubes and check them.
on_count = 0
for x in range(-50, 50 + 1):
    for y in range(-50, 50 + 1):
        for z in range(-50, 50 + 1):
            if check_on((x, y, z)):
                on_count += 1

print(f'After running the initialization, a total of {on_count} cubes are on.')
