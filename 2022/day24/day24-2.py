#!/usr/bin/python3
# Advent of Code 2022 - Day 24, Part 2
# Benedikt Otto
#
import math

# input_file = '../examples/example_24.txt'
input_file = '../inputs/input_24.txt'

# Parse input into dict
map_dict = {}
row_max = 0
col_max = 0
with open(input_file) as file:
    for row_num, line in enumerate(file.readlines()):
        for col_num, c in enumerate(line.strip()):
            map_dict[(row_num, col_num)] = c
            col_max = col_num  # assuming rectangular area.
        row_max = max(row_max, row_num)

# Find start/end position.
start_pos = (0, 1)
end_pos = (row_max, max([xy[1] for xy in map_dict if map_dict[xy] != '#' and xy[0] == row_max]))

# Constraints for the inner area.
row_min_inner = 1
row_max_inner = row_max - 1
col_min_inner = 1
col_max_inner = col_max - 1

def move_blizzards(blizzard_list):
    """Moves all blizzards in the given list one step according to their direction."""
    new_blizzard_list = []
    for blizzard in blizzard_list:
        xy, direction = blizzard
        x, y = xy
        new_xy = xy
        match direction:
            case '^':
                new_xy = (x - 1, y)
                if x - 1 < row_min_inner:
                    new_xy = (row_max_inner, y)
            case 'v':
                new_xy = (x + 1, y)
                if x + 1 > row_max_inner:
                    new_xy = (row_min_inner, y)
            case '<':
                new_xy = (x, y - 1)
                if y - 1 < col_min_inner:
                    new_xy = (x, col_max_inner)
            case '>':
                new_xy = (x, y + 1)
                if y + 1 > col_max_inner:
                    new_xy = (x, col_min_inner)
        new_blizzard = new_xy, direction
        new_blizzard_list.append(new_blizzard)
    return new_blizzard_list


# A blizzard is a tuple (xy, direction) of the position and the direction of the blizzard.
# A blizzard pattern is a list of all blizzards at this point in time.
initial_blizzard_pattern = []
for xy in map_dict:
    if map_dict[xy] in ('^', 'v', '<', '>'):
        blizzard = (xy, map_dict[xy])
        initial_blizzard_pattern.append(blizzard)

# Record all the possible blizzard patterns by simulating them until they repeat.
blizzard_pattern = []
p = initial_blizzard_pattern
blizzard_pattern.append(p)
while True:
    p = move_blizzards(p)
    if p not in blizzard_pattern:
        blizzard_pattern.append(p)
    else:
        break


# A state is the position (x,y) of the expedition and the current blizzard pattern (index in the blizzard_pattern list).
# We image a graph with vertices = states and edges between them if there is a possible movement between them.

def is_movement_possible(state):
    """Checks if it is possible to move to the given position in the given blizzard pattern."""
    position, pattern_idx = state
    x, y = position
    if position == end_pos:
        return True
    if position == start_pos:
        return True
    unsafe_spots = [s[0] for s in blizzard_pattern[pattern_idx]]
    if row_min_inner <= position[0] <= row_max_inner:
        if col_min_inner <= position[1] <= col_max_inner:
            return position not in unsafe_spots
    return False


def get_neighbours(state):
    """Neighbours of the state (vertex), e.g. there is a path state -> neighbour."""
    position, pattern_idx = state
    x, y = position

    # Pattern in the following minute, accounting for their periodic nature.
    new_pattern_idx = (pattern_idx + 1) % len(blizzard_pattern)

    # Positions for each option
    pos_north = (position[0] - 1, position[1])
    pos_south = (position[0] + 1, position[1])
    pos_west = (position[0], position[1] - 1)
    pos_east = (position[0], position[1] + 1)

    neighbours = []
    for new_pos in [position, pos_north, pos_south, pos_west, pos_east]:
        new_state = new_pos, new_pattern_idx
        if is_movement_possible(new_state):
            neighbours.append(new_state)
    return neighbours


def shortest_path(start, end_xy):
    """Determines the shortest path from the state <start> to the state <end> using Dijkstra."""
    non_visited = [start]
    dist = {}
    prev = {}
    dist[start] = 0

    # Instead of prepping all the vertices, we gradually add them to our vertex list as we discover
    # more and more neighbours. To prevent adding the same node over and over we need to remember them.
    vertices_added = [start]

    # DIJKSTRA-ALGORITHM
    while len(non_visited) > 0:
        # Get vertex with minimum distance.
        minimum = math.inf
        for v in non_visited:
            if v in dist and dist[v] < minimum:
                minimum = dist[v]
                min_vertex = v

        # Shortcut because we are only interested in the shortest path start -> end.
        if min_vertex[0] == end_xy:
            end_state = min_vertex
            break

        non_visited.remove(min_vertex)

        # Work through all neighbours of min_vertex.
        for n in get_neighbours(min_vertex):
            # Here all edge weights are 1.
            alt = dist[min_vertex] + 1
            if alt < dist.get(n, math.inf):
                dist[n] = alt
                prev[n] = min_vertex

            # Gradually build the vertex set with the neighbours.
            if n not in vertices_added:
                non_visited.append(n)
                vertices_added.append(n)

    # Get the path by backtracking from end_state through the prev dict.
    vertex = end_state
    path = [vertex]
    while vertex != start:
        vertex = prev[vertex]
        path.append(vertex)
    path.reverse()

    return path, dist[end_state]



starting_state = (start_pos, 0)

# First run start -> end.
path1, dist1 = shortest_path(starting_state, end_pos)
state_after_first_run = path1[-1]
print(f'First trip to the end: {dist1} minutes.')

# Second run end -> start.
path2, dist2 = shortest_path(state_after_first_run, start_pos)
state_after_second_run = path2[-1]
print(f'Trip back to the start: {dist2} minutes.')

# Third run start -> end.
path3, dist3 = shortest_path(state_after_second_run, end_pos)
print(f'Trip back to the goal again: {dist3} minutes')

print(f'Total time: {dist1 + dist2 + dist3} minutes.')
