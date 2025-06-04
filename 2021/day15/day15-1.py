#!/usr/bin/python3
# Advent of Code 2021 - Day 15, Part 1
# Benedikt Otto
#
import math

# input_file = '../examples/example_15.txt'
input_file = '../inputs/input_15.txt'

# Parse input into dict(key=xy, val=char).
map_dict = {}
with open(input_file) as file:
    for row_num, line in enumerate(file.readlines()):
        for col_num, c in enumerate(line.strip()):
            map_dict[(row_num, col_num)] = c


# Create a graph with vertices = xy, and edges according to the grid.
vertex_list = [xy for xy in map_dict]
adjacency_dict = {}
for xy in vertex_list:
    x, y = xy
    adjacency_dict.setdefault(xy, [])
    for n_xy in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
        if n_xy in vertex_list:
            weight = int(map_dict[n_xy])
            adjacency_dict[xy].append((n_xy, weight))

# Start and end point.
max_x = max([xy[0] for xy in vertex_list])
max_y = max([xy[1] for xy in vertex_list])
start_vertex = (0, 0)
end_vertex = (max_x, max_y)


# Find the shortest path using DIJKSTRA.
non_visited = set()
dist = {}
prev = {}
# Prepare dicts.
for v in vertex_list:
    dist.setdefault(v, math.inf)
    prev.setdefault(v, None)
    non_visited.add(v)
dist[start_vertex] = 0

while len(non_visited) > 0:
    # Get vertex with minimum distance.
    minimum = math.inf
    for v in non_visited:
        if dist[v] < minimum:
            minimum = dist[v]
            min_vertex = v

    if min_vertex == end_vertex:
        break  # Shortcut because we are only interested in the shortest path start-end.

    non_visited.remove(min_vertex)
    for n_xy, n_weight in adjacency_dict[min_vertex]:
        alt = dist[min_vertex] + n_weight
        if alt < dist[n_xy]:
            dist[n_xy] = alt
            prev[n_xy] = min_vertex


# Get the shortest path by backtracking.
path = []
v = end_vertex
while v != start_vertex:
    v = prev[v]
    w = int(map_dict[v])
    path.append((v, w))
path.reverse()

print(f'A path with lowest total risk is:')
print(path)
print(f'The total risk of this path is: {dist[end_vertex]}')
