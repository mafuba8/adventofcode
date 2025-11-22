#!/usr/bin/python3
# Advent of Code 2021 - Day 22, Part 2
# Benedikt Otto
#
import re

# input_file = '../examples/example_22b.txt'
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

    def size(self):
        return (self.x_max - self.x_min + 1) * (self.y_max - self.y_min + 1) * (self.z_max - self.z_min + 1)

    def inside(self, xyz):
        return (self.x_min <= xyz[0] <= self.x_max
                and self.y_min <= xyz[1] <= self.y_max
                and self.z_min <= xyz[2] <= self.z_max)

    def intersect(self, other):
        """The intersection of two cuboids is again a cuboid."""
        ix_min = max(self.x_min, other.x_min)
        ix_max = min(self.x_max, other.x_max)
        iy_min = max(self.y_min, other.y_min)
        iy_max = min(self.y_max, other.y_max)
        iz_min = max(self.z_min, other.z_min)
        iz_max = min(self.z_max, other.z_max)
        if ix_min <= ix_max and iy_min <= iy_max and iz_min <= iz_max:
            return Cuboid(ix_min, ix_max, iy_min, iy_max, iz_min, iz_max)
        else:
            return None


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

# Idea: Track a list of positive and negative cuboids and count them up at the end.
# At each step, intersect the new cuboid with all the current cuboids (both positive and negative)
# and add the new intersections to the list of opposite cuboids to account for over-/undercounting.
cuboids_positive = []
cuboids_negative = []

# Add the first cuboid to the positive cuboids. (we ASSUME that the first one is always 'on').
_, first_cuboid = cuboid_list[0]
cuboids_positive.append(first_cuboid)

# Run through all the remaining cuboids, intersecting them with all known positive and negative cuboids.
for new_state, new_cuboid in cuboid_list[1:]:
    print(f'adding {new_cuboid} (State: {new_state})...')
    new_cuboids_positive = []
    new_cuboids_negative = []

    # A new 'on' cuboids get added to the positive cuboids, but we need to account for over- and undercounting.
    if new_state == 'on':
        new_cuboids_positive.append(new_cuboid)
        for cuboid in cuboids_positive:
            intersection = cuboid.intersect(new_cuboid)
            if intersection:
                new_cuboids_negative.append(intersection)
        for cuboid in cuboids_negative:
            intersection = cuboid.intersect(new_cuboid)
            if intersection:
                new_cuboids_positive.append(intersection)

    # A new 'off' cuboid does NOT get added to the negative cuboids, but we still calculate and add the intersections.
    elif new_state == 'off':
        for cuboid in cuboids_positive:
            intersection = cuboid.intersect(new_cuboid)
            if intersection:
                new_cuboids_negative.append(intersection)
        for cuboid in cuboids_negative:
            intersection = cuboid.intersect(new_cuboid)
            if intersection:
                new_cuboids_positive.append(intersection)

    # Add the new cuboids to the list.
    cuboids_positive = cuboids_positive + new_cuboids_positive
    cuboids_negative = cuboids_negative + new_cuboids_negative

    print(f'  we obtain {len(new_cuboids_positive)} new positive and {len(new_cuboids_negative)} negative cuboids.')
    print(f'  new total: {len(cuboids_positive)} positive and {len(cuboids_negative)} negative cuboids.')


# Calculate the number of cubes that are on:
on_count = 0
for cuboid in cuboids_positive:
    on_count += cuboid.size()
for cuboid in cuboids_negative:
    on_count -= cuboid.size()

print(f'After running the full reboot, a total of {on_count} cubes are on.')
