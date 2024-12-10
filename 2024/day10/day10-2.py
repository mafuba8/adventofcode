#!/usr/bin/python3
# Advent of Code 2024 - Day 10, Part 2
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
starting_points = [x for x in top_map if top_map[x] == 0]

# Find all paths to 9-height tiles by continuing all known paths to their accessible neighbors.
# NOTE: we could have used the same code as in part 1
#       but replaced the 'reachable_peaks' set with a list.
sum_of_ratings = 0
for start in starting_points:
    hiking_trails = []

    # This time we put paths on the stack. Path = list[xy-coords].
    stack = [[start]]
    while len(stack) > 0:
        path = stack.pop()
        last_tile = path[-1]
        if top_map[last_tile] == 9:
            # Here we have a complete hiking trail.
            hiking_trails.append(path)
        else:
            for n in get_neighbors(last_tile):
                new_path = path + [n]
                stack.append(new_path)
    sum_of_ratings += len(hiking_trails)
    print(f'Trailhead {start}: {len(hiking_trails)} rating.')

print(f'Sum of all trailhead ratings on the map: {sum_of_ratings}')

