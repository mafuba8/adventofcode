#!/usr/bin/python3
# Advent of Code 2024 - Day 12, Part 2
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


# Find all connected regions by flood-fill.
region_list = []
visited_plots = []
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

    # Mark all plots in the found region as visited.
    for x in region:
        if x in remaining_plots:
            remaining_plots.remove(x)
    region_list.append(region)


# A border is a list of neighbouring tiles, e.g. the border between
# the (0, 0) plot and the (1, 0) plot is defined as:
#   b = [(0, 0), (1, 0)]

def get_borders(vertex):
    """Returns a list of all four borders of the given vertex."""
    borders = []
    for n in [(vertex[0] + 1, vertex[1]), (vertex[0] - 1, vertex[1]),
              (vertex[0], vertex[1] + 1), (vertex[0], vertex[1] - 1)]:
        b = [vertex, n]
        # We need to makre sure the border pair is always in the form (left|right or up|down)
        # to keep track of where it is relative to the region.
        b.sort()
        borders.append(b)
    return borders


def get_region_borders(region):
    """Returns a list of all borders of the given region."""
    region_borders = []
    for v in region:
        b0 = get_borders(v)
        # Symmetric difference gives us the border of the connected set.
        region_borders = ([b for b in b0 if b not in region_borders]
                          + [b for b in region_borders if b not in b0])
    return region_borders


def get_border_neighbours(border):
    """For a given border, this returns the two adjacent borders.
    These will be on the same 'side' if they actually exist."""
    v1, v2 = border
    if v1[0] == v2[0]:
        # Vertical border -> borders over/under it.
        n1 = [(v1[0] - 1, v1[1]), (v1[0] - 1, v2[1])]
        n2 = [(v1[0] + 1, v1[1]), (v1[0] + 1, v2[1])]
    if v1[1] == v2[1]:
        # Horizontal border -> borders left/right of it.
        n1 = [(v1[0], v1[1] - 1), (v2[0], v1[1] - 1)]
        n2 = [(v1[0], v1[1] + 1), (v2[0], v1[1] + 1)]
    return [n1, n2]


# Determine the border around each region and its price.
total_price = 0
for region in region_list:
    region_area = len(region)

    # Get borders of the region and find all connected sides.
    plant = garden_plot[region[0]]  # Remember the plant type in this region.

    # Work through all borders of the region and find the sides.
    borders = get_region_borders(region)
    visited_borders = []
    sides_list = []

    for border in borders:
        if border in visited_borders:
            continue

        # Another flood-fill, but this time we work with borders and 'fill' up all
        # borders that reside on the same side of a region.
        side = []
        stack = [border]
        while len(stack) > 0:
            b = stack.pop()
            # We need to make sure that we only look at borders that have the plant type
            # on the same side. So we remember whether the tile with our plant
            # is the first or second in the border pair.
            if garden_plot.get(b[0],'') == plant:
                i = 0
            if garden_plot.get(b[1],'') == plant:
                i = 1

            side.append(b)
            for n in get_border_neighbours(b):
                if n in borders and n not in side:
                    if garden_plot.get(n[i], '') == plant:
                        # Only take borders that have the plant type on the same side.
                        stack.append(n)

        # Mark all plots in the found side as visited.
        visited_borders = visited_borders + side
        sides_list.append(side)

    print(f'Region {garden_plot[region[0]]} - Area: {len(region)}, Number of sides: {len(sides_list)} => Price: {len(region) * len(sides_list)}')
    total_price += len(region) * len(sides_list)

print(f'Total price: {total_price}')
