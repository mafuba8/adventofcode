#!/usr/bin/python3
# Advent of Code 2023 - Day 23, Part 1
# Benedikt Otto

# Open puzzle file and parse into dict(key=(x, y), val=symbol)
hiking_map = {}
#with open('example_23.txt') as file:
with open('../inputs/input_23.txt') as file:
    for row_num, row in enumerate(file.readlines()):
        row = row.strip()
        for col_num, char in enumerate(row):
            hiking_map.setdefault((row_num, col_num), char)
            if row_num == 0 and char == '.':
                start = (row_num, col_num)
        map_width = col_num + 1
    map_height = row_num + 1

# Get destination square.
destination = (0, 0)
for col_num in range(map_width):
    if hiking_map[(map_height - 1, col_num)] == '.':
        destination = (map_height - 1, col_num)


def get_neighbors(vertex):
    """Returns the neighbors of the given square, as allowed by the arrows."""
    vertex_x, vertex_y = vertex
    neighbours = set()
    north_tile = (vertex_x - 1, vertex_y)
    south_tile = (vertex_x + 1, vertex_y)
    west_tile = (vertex_x, vertex_y - 1)
    east_tile = (vertex_x, vertex_y + 1)

    if 0 <= north_tile[0] < map_height and 0 <= north_tile[1] < map_width:
        north_symbol = hiking_map[north_tile]
        if north_symbol in ['^', '.']:
            neighbours.add(north_tile)

    if 0 <= south_tile[0] < map_height and 0 <= south_tile[1] < map_width:
        south_symbol = hiking_map[south_tile]
        if south_symbol in ['v', '.']:
            neighbours.add(south_tile)

    if 0 <= west_tile[0] < map_height and 0 <= west_tile[1] < map_width:
        west_symbol = hiking_map[west_tile]
        if west_symbol in ['<', '.']:
            neighbours.add(west_tile)

    if 0 <= east_tile[0] < map_height and 0 <= east_tile[1] < map_width:
        east_symbol = hiking_map[east_tile]
        if east_symbol in ['>', '.']:
            neighbours.add(east_tile)

    return neighbours


# Define graph.
vertex_set = {t for t in hiking_map if hiking_map[t] != '#'}
hiking_graph = {}
for vertex in vertex_set:
    hiking_graph.setdefault(vertex, get_neighbors(vertex))


def get_path(vertex, prev_vertex):
    """Returns a list of paths that are possible from vertex to destination,
    when coming from prev_vertex. A path is a list of tuples."""
    path_list = []
    initial_path = []

    neighbors = get_neighbors(vertex)
    neighbors.discard(prev_vertex)

    # On straight paths keep replacing vertex and prev_vertex with their next tiles.
    # (to prevent deep recursion)
    while len(neighbors) == 1:
        new_prev_vertex = vertex
        vertex = neighbors.pop()
        prev_vertex = new_prev_vertex
        neighbors = get_neighbors(vertex)
        neighbors.discard(prev_vertex)
        initial_path.append(vertex)

    # Recursion end when we have reached the destination.
    if vertex == destination:
        return [initial_path]

    # On crossroads walk all the possible paths via recursion.
    for n in neighbors:
        for path in get_path(n, vertex):
            new_path = initial_path + [n] + path
            path_list.append(new_path)

    return path_list


# Determine all possible paths from start to destination and count their steps.
max_steps = 0
possible_paths = get_path(start, (0, 0))
for path_num, path in enumerate(possible_paths):
    print(f'Path #{path_num}: {len(path)} Steps.')
    if len(path) > max_steps:
        max_steps = len(path)

print(f'Longest hike: {max_steps} Steps.')
