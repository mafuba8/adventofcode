#!/usr/bin/python3
# Advent of Code 2023 - Day 24, Part 1
# Benedikt Otto
import itertools
import re

# Open puzzle file and parse into list of tuples.
hailstone_list = []
regex = re.compile(r'(\d+),\s(\d+),\s(\d+)\s@\s+(-?\d+),\s+(-?\d+),\s+(-?\d+)')
#with open('example_24.txt') as file:
with open('input_24.txt') as file:
    for line in file.readlines():
        search = regex.search(line.strip())
        hailstone = (int(search.group(1)), int(search.group(2)), int(search.group(3)),
                     int(search.group(4)), int(search.group(5)), int(search.group(6)))
        hailstone_list.append(hailstone)


def intersection(h1, h2):
    """Returns the intersection point (x, y) of the two hailstones, and the time points
    t1/t2 where h1/h2 are at the moment of the intersection."""

    # Write in implicit form y = mx + c with:
    #   m = vy / vx
    #   c = py - px * (vy / vx)
    # (assuming vx != 0).
    m1 = h1[4] / h1[3]
    m2 = h2[4] / h2[3]
    c1 = h1[1] - h1[0] * (h1[4] / h1[3])
    c2 = h2[1] - h2[0] * (h2[4] / h2[3])
    if m1 == m2:
        return None  # parallel

    # Intersection formula obtained by equating both sides:
    x = (c2 - c1) / (m1 - m2)
    y = m1 * ((c2 - c1) / (m1 - m2)) + c1

    # Parametrized form gives time point at the intersection: t = (x - px) / vx
    t1 = (x - h1[0]) / h1[3]
    t2 = (x - h2[0]) / h2[3]

    return x, y, t1, t2


#LOWER_BOUND = 7
#UPPER_BOUND = 27
LOWER_BOUND = 200000000000000
UPPER_BOUND = 400000000000000

ints_count = 0
for h1, h2 in itertools.combinations(hailstone_list, 2):
    ints = intersection(h1, h2)
    if ints is None:
        continue  # h1 and h2 are parallel.
    (x, y, t1, t2) = ints
    if LOWER_BOUND <= x <= UPPER_BOUND and LOWER_BOUND <= y <= UPPER_BOUND:
        # Intersection within the area.
        if t1 > 0 and t2 > 0:
            # Intersection is in the future.
            ints_count += 1

print(f'Total future intersections within the area: {ints_count}')
