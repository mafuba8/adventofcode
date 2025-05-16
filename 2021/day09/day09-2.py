#!/usr/bin/python3
# Advent of Code 2021 - Day 9, Part 2
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


# Find all the low points.
low_points = [c for c in height_map if is_low_point(c)]


def find_basin(base_point):
    # Flood-fill like algorithm to find basins.
    basin_points = set()
    visited = set()

    queue = [base_point]
    while len(queue) > 0:
        p = queue.pop()
        if p in visited:
            continue

        # Here p is a new point part of this basin.
        basin_points.add(p)

        # Add all neighbours that flow downwards to p.
        x, y = p
        for neigh in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
            if neigh in height_map:
                if height_map[p] <= height_map[neigh] < 9:
                    queue.append(neigh)
        visited.add(p)

    return basin_points


# Find all the basins and record their sizes.
basin_sizes = []
for low_point in low_points:
    basin = find_basin(low_point)
    print(f'Point {low_point}: Basin size {len(basin)}.')
    basin_sizes.append(len(basin))

# Multiply the three largest basin sizes.
basin_sizes.sort(reverse=True)
top_three_sizes = basin_sizes[:3]

result = 1
for n in top_three_sizes:
    result *= n

print(f'Top three basin sizes: {top_three_sizes}.')
print(f'Product of the three largest basin sizes: {result}.')



