#!/usr/bin/python3
# Advent of Code 2024 - Day 16, Part 1
# Benedikt Otto
#
import math

# input_file = '../examples/example_16a.txt'
# input_file = '../examples/example_16b.txt'
input_file = '../inputs/input_16.txt'

# Parse input into dict(key=xy, val=char).
start_tile = (0, 0)
end_tile = (0, 0)
maze_map = {}
with open(input_file) as file:
    for row_num, row in enumerate(file.readlines()):
        for col_num, char in enumerate(row.strip()):
            maze_map.setdefault((row_num, col_num), char)
            if char == 'S':
                start_tile = (row_num, col_num)
            if char == 'E':
                end_tile = (row_num, col_num)


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


# Build graph as dict(key=vertex, val=[neighbors])
maze_graph = {}
for vertex in vertex_set:
    maze_graph.setdefault(vertex, get_neighbors(vertex))

# We don't care with which direction we end up at End, so we add one additional vertex.
end_vertex = (end_tile, '.')  # End vertex
vertex_set.add(end_vertex)
# Add edges with weight 0 from any end tile direction to the end_vertex.
end_neighbours = [(end_tile, 'N'), (end_tile, 'S'), (end_tile, 'E'), (end_tile, 'W')]
for ne in end_neighbours:
    maze_graph[ne].append((end_vertex, 0))


# DIJKSTRA ALGORITHM.
non_visited = []
dist = {}
prev = {}
for v in vertex_set:
    # Prepare dicts.
    dist.setdefault(v, math.inf)
    prev.setdefault(v, None)
    non_visited.append(v)
start_vertex = (start_tile, 'E')
dist[start_vertex] = 0

while len(non_visited) > 0:
    # Get vertex with minimum distance.
    minimum = math.inf
    for v in non_visited:
        if dist[v] < minimum:
            min_vertex = v
            minimum = dist[v]

    # Shortcut because we are only interested in the shortest path start_vertex -> end_vertex.
    if min_vertex == end_vertex:
        break

    if minimum == math.inf:
        break  # Here the remaining vertices are unreachable.

    non_visited.remove(min_vertex)
    # Work through all neighbours of min_vertex.
    for n in maze_graph[min_vertex]:
        n_vertex, n_weight = n
        alt = dist[min_vertex] + n_weight
        if alt < dist[n_vertex]:
            dist[n_vertex] = alt
            prev[n_vertex] = min_vertex


# Get the shortest path by backtracking through prev and reversing the list.
path = []
vertex = end_vertex
while vertex != start_vertex:
    vertex = prev[vertex]
    path.append(vertex)
path.reverse()

print(f'Shortest path from {start_vertex} to {end_vertex}:')
print(path)
print(f'Points needed: {dist[end_vertex]}')
