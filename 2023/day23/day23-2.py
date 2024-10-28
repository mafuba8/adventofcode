#!/usr/bin/python3
# Advent of Code 2023 - Day 23, Part 2
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

    adjacent_tiles = [(vertex_x - 1, vertex_y), (vertex_x + 1, vertex_y),
                      (vertex_x, vertex_y - 1), (vertex_x, vertex_y + 1)]

    for tile in adjacent_tiles:
        if 0 <= tile[0] < map_height and 0 <= tile[1] < map_width and hiking_map[tile] != '#':
            neighbours.add(tile)

    return neighbours


# Define graph.
vertex_set = {t for t in hiking_map if hiking_map[t] != '#'}
hiking_graph = {}
for vertex in vertex_set:
    hiking_graph.setdefault(vertex, get_neighbors(vertex))

# Define new graph where the only vertices are the crossroads and start/destination.
simplified_vertices = set()
for vertex in hiking_graph:
    neighbors = hiking_graph[vertex]
    if len(neighbors) >= 3:
        simplified_vertices.add(vertex)
simplified_vertices.add(start)
simplified_vertices.add(destination)

# Straight lines get condensed into one edge and their weight (#steps) saved in simplified_weights.
simplified_graph = {}
simplified_weights = {}
for vertex in simplified_vertices:
    neighbor_list = []
    begin_vertex = vertex
    neighbors = hiking_graph[vertex]
    for n in neighbors:
        prev = vertex
        v = n
        adjacent_to_v = hiking_graph[v] - {prev}
        steps = 1

        while len(adjacent_to_v) == 1:
            # Walk straight lines (1 non-prev neighbor) and count steps.
            prev = v
            v = adjacent_to_v.pop()
            adjacent_to_v = hiking_graph[v] - {prev}
            steps += 1

        neighbor_list.append(v)
        simplified_weights.setdefault((vertex, v), steps)
    simplified_graph.setdefault(vertex, neighbor_list)


# Preparation for depth-first search.
visited = {v: False for v in simplified_graph}
current_path = []
simple_paths = []

def dfs(u, v):
    """Get all simple paths using depth-first search."""
    if visited[u]:
        return

    visited[u] = True
    current_path.append(u)
    if u == v:
        simple_paths.append(current_path.copy())
        visited[u] = False
        del current_path[-1]
        return

    for n in simplified_graph[u]:
        dfs(n, v)

    del current_path[-1]
    visited[u] = False


# Actual DFS start.
dfs(start, destination)

# Count total weight (steps) for each path.
max_steps = 0
for path_num, path in enumerate(simple_paths):
    steps = 0
    prev = path[0]
    for v in path[1:]:
        weight = simplified_weights[prev, v]
        steps += weight
        prev = v
    if steps > max_steps:
        max_steps = steps
    print(f'Path #{path_num}: {steps} Steps.')

print(f'Longest hike: {max_steps} Steps.')
