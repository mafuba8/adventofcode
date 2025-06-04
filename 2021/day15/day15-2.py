#!/usr/bin/python3
# Advent of Code 2021 - Day 15, Part 2
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


MAX_IDX = max([xy[0] for xy in map_dict]) + 1  # Assuming a square input.
NUM_COPIES = 5

# Since the whole map is NUM_COPIES copies of the original map in both x and y direction,
# we assume a graph with the vertices (x, y, X, Y), where
#  (x, y) = coordinates in the original map.
#  (X, Y) = coordinates (number) of the copy that the vertex is in.
#
# Instead of building the whole vertex list, we generate it gradually using an adjacency function.

def get_adjacent_vertices(vertex):
    """Returns a list of all vertices that are adjacent to the given vertex."""
    vx, vy, vX, vY = vertex
    adj_list = []
    for x, y in [(vx - 1, vy), (vx + 1, vy), (vx, vy - 1), (vx, vy + 1)]:
        nx = x % MAX_IDX
        ny = y % MAX_IDX

        nX = vX + (x // MAX_IDX)
        nY = vY + (y // MAX_IDX)
        if 0 <= nX < 5 and 0 <= nY < 5:
            adj_list.append((nx, ny, nX, nY))
    return adj_list


def get_weight(vertex):
    """Returns the weight of a vertex (technically: of an edge that ends at vertex)."""
    vx, vy, vX, vY = vertex
    w = int(map_dict[(vx, vy)]) + vX + vY
    # no zeroes, 9 wraps into 1.
    return (w - 1) % 9 + 1


# Start and end point.
start_vertex = (0, 0, 0, 0)
end_vertex = (MAX_IDX - 1, MAX_IDX - 1, NUM_COPIES - 1, NUM_COPIES - 1)

# DIJKSTRA ALGORITHM.
#  v not in dist = math.inf
#  v not in prev = None
non_visited = [start_vertex]
dist = {start_vertex: 0}
prev = {}

# Instead of prepping all the vertices, we gradually add them to our vertex list as we discover
# more and more neighbours.
vertices_added = {start_vertex}

while len(non_visited) > 0:
    # Get a vertex with minimum known distance.
    minimum = math.inf
    for v in non_visited:
        if v in dist and dist[v] < minimum:
            minimum = dist[v]
            min_vertex = v

    # Shortcut because we are only interested in the shortest path start -> end.
    if min_vertex == end_vertex:
        break

    non_visited.remove(min_vertex)
    # Work through all neighbours of min_vertex.
    for n_vertex in get_adjacent_vertices(min_vertex):
        alt = dist[min_vertex] + get_weight(n_vertex)
        if alt < dist.get(n_vertex, math.inf):
            dist[n_vertex] = alt
            prev[n_vertex] = min_vertex

        # Add newly discovered neighbours to our list of vertices.
        if n_vertex not in vertices_added:
            non_visited.append(n_vertex)
            vertices_added.add(n_vertex)


# Get the shortest path by backtracking.
path = []
v = end_vertex
while v != start_vertex:
    v = prev[v]
    w = get_weight(v)
    path.append(w)
path.reverse()

print(f'A path with lowest total risk is:')
print(path)
print(f'The total risk of this path is: {dist[end_vertex]}')
