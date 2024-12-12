#!/usr/bin/python3
# Advent of Code 2024 - Day 12, Part 1
# Benedikt Otto
#

# input_file = '../examples/example_12.txt'
input_file = '../inputs/input_12.txt'

# Parse into dict(key=xy, val=char).
garden_plot = {}
with open(input_file) as file:
    for row_num, row in enumerate(file.readlines()):
        for col_num, char in enumerate(row):
            if char != '\n':
                garden_plot.setdefault((row_num, col_num), char)


def get_neighbours(vertex):
    """Return a list of all neighbours of the given vertex."""
    n_list = []
    for n in [(vertex[0] + 1, vertex[1]), (vertex[0] - 1, vertex[1]),
              (vertex[0], vertex[1] + 1), (vertex[0], vertex[1] - 1)]:
        if n in garden_plot:
            n_list.append(n)
    return n_list


def get_borders(vertex):
    """Returns a set of all four borders of the given vertex.
    A border is a set of two neighbouring tiles."""
    borders = []
    for n in [(vertex[0] + 1, vertex[1]), (vertex[0] - 1, vertex[1]),
              (vertex[0], vertex[1] + 1), (vertex[0], vertex[1] - 1)]:
        b = {vertex, n}
        borders.append(b)
    return borders


# Find all connected regions by flood-fill.
region_list = []
remaining_plots = list(garden_plot.keys())
while len(remaining_plots) > 0:
    start_vertex = remaining_plots.pop()
    region = []
    stack = [start_vertex]
    while len(stack) > 0:
        v = stack.pop()
        if v not in region:
            region.append(v)
            for n in get_neighbours(v):
                if garden_plot[n] == garden_plot[v]:
                    stack.append(n)

    for x in region:
        if x in remaining_plots:
            remaining_plots.remove(x)
    region_list.append(region)
    print(f'Region: {garden_plot[start_vertex]}: {region}')


# Determine the border around each region and its price.
total_price = 0
for region in region_list:
    region_area = len(region)

    # Finding all borders of each region. A border is a set {v1, v2} of two tiles that are next to each other.
    region_borders = []
    for v in region:
        b0 = get_borders(v)
        # Symmetric difference gives us the shared border.
        region_borders = [b for b in b0 if b not in region_borders] + [b for b in region_borders if b not in b0]
    region_perimeter = len(region_borders)

    print(f'Area: {region_area}, Borders: {region_perimeter}, Price: {region_area * region_perimeter}')
    total_price += region_area * region_perimeter

print(f'Total price: {total_price}')
