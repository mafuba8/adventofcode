#!/usr/bin/python3
# Advent of Code 2022 - Day 12, Part 1
# Benedikt Otto
import math

# input_file = '../examples/example_12.txt'
input_file = '../inputs/input_12.txt'

# Parse input into dict(key=(x, y), val=char)
area = {}
with open(input_file) as file:
    for row_num, row in enumerate(file.readlines()):
        for col_num, char in enumerate(row.strip()):
            if char == 'S':
                # Remember starting point and replace with actual height.
                start = (row_num, col_num)
                area.setdefault((row_num, col_num), 'a')
            elif char == 'E':
                # Remember end point and replace with actual height.
                end = (row_num, col_num)
                area.setdefault((row_num, col_num), 'z')
            else:
                area.setdefault((row_num, col_num), char)


def adjacent_tiles(tile):
    """ Takes coordinates of a tile and returns all adjacent tiles that are walkable from there."""
    x, y = tile
    neigh = []  # neighbouring tiles.
    for u in [1, -1]:
        if (x, y+u) in area:
            neigh.append((x, y+u))
        if (x + u, y) in area:
            neigh.append((x+u, y))
    # destination tile n may be at most one higher than tile (but can be way lower!).
    return [n for n in neigh if ord(area[n]) - ord(area[tile]) <= 1]


# Build graph as dict(key=vertex, val=[walkable neighbors]).
vertex_set = set()
graph = {}
for tile in area:
    vertex_set.add(tile)
    graph.setdefault(tile, adjacent_tiles(tile))


# DIJKSTRA ALGORITHM.
# Prepare dicts for Dijkstra
non_visited = []
dist = {}
prev = {}
for v in graph:
    dist.setdefault(v, math.inf)
    prev.setdefault(v, None)
    non_visited.append(v)
dist[start] = 0

while len(non_visited) > 0:
    # Get vertex with minimum dist.
    minimum = math.inf
    for v in non_visited:
        if dist[v] < minimum:
            minimum = dist[v]
            min_vertex = v

    if minimum == math.inf:
        break  # Here the remaining nodes are unreachable.

    non_visited.remove(min_vertex)
    # Work through all neighbors of min_vertex.
    for n in graph[min_vertex]:
        # In this graph all edge values are 1.
        alt = dist[min_vertex] + 1
        if alt < dist[n]:
            dist[n] = alt
            prev[n] = min_vertex


# Get the shortest path start->end by backtracking through prev and reversing the list.
path = []
node = end
while node != start:
    node = prev[node]
    path.append(node)
path.reverse()

print('Shortest path from S to E:')
print(path)
print(f'Length: {dist[end]}')
