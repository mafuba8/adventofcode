#!/usr/bin/python3
# Advent of Code 2024 - Day 16, Part 2
# Benedikt Otto
#
import math

# input_file = '../examples/example_16a.txt'
# input_file = '../examples/example_16b.txt'
input_file = '../inputs/input_16.txt'

# Parse input into dict(key=xy, val=char). Also get the coordinates of the start and end.
start_coords = (0, 0)
end_coords = (0, 0)
maze_map = {}
with open(input_file) as file:
    for row_num, row in enumerate(file.readlines()):
        for col_num, char in enumerate(row.strip()):
            maze_map.setdefault((row_num, col_num), char)
            if char == 'S':
                start_coords = (row_num, col_num)
            if char == 'E':
                end_coords = (row_num, col_num)


# Define set of vertices. Each coordinate has a vertex for each of the four possible directions.
vertex_set = set()
for coord in maze_map:
    if maze_map[coord] != '#':
        vertex_set.add((coord, 'N'))
        vertex_set.add((coord, 'S'))
        vertex_set.add((coord, 'E'))
        vertex_set.add((coord, 'W'))


def get_neighbors(vertex):
    """Returns a list of all neighbours of the given vertex, where each
    neighbor is a tuple (ne_vertex, weight)."""
    coord, direction = vertex
    coord_x, coord_y = coord
    neighbors = []
    # We can either walk straight (moving one tile in this dir.) or rotate 90 degrees.
    match direction:
        case 'N':
            ne_straight = ((coord_x - 1, coord_y), 'N')
            ne_rotate1, ne_rotate2 = (coord, 'W'), (coord, 'E')
        case 'S':
            ne_straight = ((coord_x + 1, coord_y), 'S')
            ne_rotate1, ne_rotate2 = (coord, 'E'), (coord, 'W')
        case 'E':
            ne_straight = ((coord_x, coord_y + 1), 'E')
            ne_rotate1, ne_rotate2 = (coord, 'N'), (coord, 'S')
        case 'W':
            ne_straight = ((coord_x, coord_y - 1), 'W')
            ne_rotate1, ne_rotate2 = (coord, 'S'), (coord, 'N')
        case _:
            ne_straight = vertex
            ne_rotate1 = vertex
            ne_rotate2 = vertex

    # Straight walks cost 1 point.
    if ne_straight in vertex_set:
        neighbors.append((ne_straight, 1))

    # Rotations cost 1000 points.
    neighbors.append((ne_rotate1, 1000))
    neighbors.append((ne_rotate2, 1000))

    return neighbors


# Build graph:
#   maze_graph = dict(key=vertex, val=[neighbors])
#   graph_weights = dict(key=(vertex_from, vertex_to), val=weight)
#
maze_graph = {}
graph_weights = {}
for vertex in vertex_set:
    neighbour_list = []
    for ne in get_neighbors(vertex):
        ne_vertex, ne_weight = ne
        neighbour_list.append(ne_vertex)
        graph_weights.setdefault((vertex, ne_vertex), ne_weight)

    maze_graph.setdefault(vertex, neighbour_list)

# We don't care with which direction we end up at the last tile, so we add one additional vertex.
end_vertex = (end_coords, '.')  # End vertex
maze_graph.setdefault(end_vertex, [])
vertex_set.add(end_vertex)
# Add edges with weight 0 from any end tile direction to the end_vertex.
end_neighbours = [(end_coords, 'N'), (end_coords, 'S'), (end_coords, 'E'), (end_coords, 'W')]
for ne in end_neighbours:
    maze_graph[ne].append(end_vertex)
    maze_graph[end_vertex].append(ne)

    # 1 additional weight so that the shortest path finding works.
    graph_weights.setdefault((ne, end_vertex), 1)
    graph_weights.setdefault((end_vertex, ne), 1)


# DIJKSTRA ALGORITHM.
# This time we use Dijkstra to find the shortest distance to ALL vertices.
non_visited = []
dist = {}
prev = {}
for v in vertex_set:
    # Prepare dicts.
    dist.setdefault(v, math.inf)
    prev.setdefault(v, None)
    non_visited.append(v)
start_vertex = (start_coords, 'E')
dist[start_vertex] = 0

while len(non_visited) > 0:
    # Get vertex with minimum distance.
    minimum = math.inf
    for v in non_visited:
        if dist[v] < minimum:
            min_vertex = v
            minimum = dist[v]

    if minimum == math.inf:
        break  # Here the remaining vertices are unreachable.

    non_visited.remove(min_vertex)
    # Work through all neighbours of min_vertex.
    for n in maze_graph[min_vertex]:
        alt = dist[min_vertex] + graph_weights[(min_vertex, n)]
        if alt < dist[n]:
            dist[n] = alt
            prev[n] = min_vertex


# Need to subtract 1 to account for the extra vertex we added at the end.
print(f'Points needed for the shortest path: {dist[end_vertex] - 1}')


def find_shortest_paths(vertex):
    """Returns a list of shortest paths from start_vertex to vertex."""
    if vertex == start_vertex:
        return [[]]

    shortest_paths = []
    # Look at all vertices that have vertex as neighbour.
    for v_prev in [v for v in maze_graph if vertex in maze_graph[v]]:
        # Distance obtained when we walk to vertex through v_prev.
        new_length = dist[vertex] - graph_weights[(v_prev, vertex)]

        # We check if the path through v_prev is still minimal (i.e. = dist[v_prev]).
        if new_length == dist[v_prev] and new_length < dist[vertex]:
            # Here v_prev is on a shortest path, so we build the full path through recursion.
            for path in find_shortest_paths(v_prev):
                path.append(v_prev)
                shortest_paths.append(path)
    return shortest_paths


# Find all shortest paths from start_tile to end_tile.
shortest_paths_end = find_shortest_paths(end_vertex)

# Find all tiles that are on any of the shortest paths.
shortest_path_tiles = set()
for path in shortest_paths_end:
    for vertex in path:
        coord, direction = vertex
        shortest_path_tiles.add(coord)

print(f'Number of shortest paths: {len(shortest_paths_end)}')
print(f'Tiles on any shortest path: {shortest_path_tiles}')
print(f'Number of tiles: {len(shortest_path_tiles)}')
