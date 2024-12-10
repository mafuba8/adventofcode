#!/usr/bin/python3
# Advent of Code 2024 - Day 10, Part 1
# Benedikt Otto
#

# input_file = '../examples/example_10.txt'
input_file = '../inputs/input_10.txt'

# Parse input into dict(key=xy, val=char).
top_map = {}
with open(input_file) as file:
    for row_num, row in enumerate(file.readlines()):
        for col_num, char in enumerate(row):
            if char != '\n':
                top_map.setdefault((row_num, col_num), int(char))


def get_neighbors(vertex):
    """Returns all neighbor tiles where it is allowed to walk vertex -> neighbor."""
    neighbor_list = []
    for x in [(vertex[0] + 1, vertex[1]), (vertex[0] - 1, vertex[1]),
              (vertex[0], vertex[1] + 1), (vertex[0], vertex[1] - 1)]:
        if x in top_map:
            if top_map[x] - top_map[vertex] == 1:
                neighbor_list.append(x)
    return neighbor_list


# All points with a height of 0 are potential trailheads.
trailheads = [x for x in top_map if top_map[x] == 0]

# Find all accessible peaks by iteratively adding neighbors until we end up on 9-tiles.
sum_of_scores = 0
for trailhead in trailheads:
    reachable_peaks = set()

    stack = [trailhead]
    while len(stack) > 0:
        x = stack.pop()
        if top_map[x] == 9:
            # Here we have reached a peak.
            reachable_peaks.add(x)
        else:
            neighbors = get_neighbors(x)
            stack = stack + neighbors
    sum_of_scores += len(reachable_peaks)
    print(f'Starting point {trailhead}: {len(reachable_peaks)} score.')

print(f'Sum of all trailhead scores on the map: {sum_of_scores}')


