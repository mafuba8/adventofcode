#!/usr/bin/python3
# Advent of Code 2022 - Day 12, Part 2
# Benedikt Otto
import math

# Compared to Part 1, we now use Dijkstra to find the distances of all tiles
# to the END point 'E'. Amongst those, we then look only at the tiles with elevation 'a'.

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
    # We now walk backwards from end, so the neighbors are all tiles with elevation >= -1.
    return [n for n in neigh if ord(area[n]) - ord(area[tile]) >= -1]


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
dist[end] = 0

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


# Find the 'a' tile with the lowest distance to end.
tiles_a = [tile for tile in area if area[tile] == 'a']
min_distance = math.inf
for tile in tiles_a:
    if dist[tile] < min_distance:
        min_tile = tile
        min_distance = dist[tile]

print(f'a-Tile with shortest path: {min_tile}')
print(f'Path length: {min_distance}')
