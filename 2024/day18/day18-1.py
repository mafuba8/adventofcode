#!/usr/bin/python3
# Advent of Code 2024 - Day 18, Part 1
# Benedikt Otto
#
import math

# input_file = '../examples/example_18.txt'
input_file = '../inputs/input_18.txt'

# Constraints are different for example/input.
# MEM_SPACE_SIZE = 6 + 1
# NUM_BYTES_FALLEN = 12
MEM_SPACE_SIZE = 70 + 1
NUM_BYTES_FALLEN = 1024


# Parse input into list of coordinates.
byte_list = []
with open(input_file) as file:
    for line in file.readlines():
        x, y = line.strip().split(',')
        byte_list.append((int(x), int(y)))

# Build Memory space as dict(key=xy, val=char).
memory_space = {}
for x in range(MEM_SPACE_SIZE):
    for y in range(MEM_SPACE_SIZE):
        if (x, y) in byte_list[:NUM_BYTES_FALLEN]:
            memory_space.setdefault((x, y), '#')
        else:
            memory_space.setdefault((x, y), '.')


def find_neighbours(vertex):
    """Returns a list of neighbours of the given vertex."""
    neighbours = []
    # Neighbours are bordering tiles U/D/L/R that don't have a corrupted byte.
    x, y = vertex
    for ne in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
        if ne in memory_space and memory_space[ne] == '.':
            neighbours.append(ne)
    return neighbours


# Build graph as dict(key=xy, val=[neighbours]).
start_vertex = (0, 0)
end_vertex = (MEM_SPACE_SIZE - 1, MEM_SPACE_SIZE - 1)
vertex_set = set(memory_space.keys())
graph = {}
for v in vertex_set:
    graph.setdefault(v, find_neighbours(v))


# DIJKSTRA ALGORITHM
non_visited = []
dist = {}
prev = {}
# Prepare dicts.
for v in vertex_set:
    dist.setdefault(v, math.inf)
    prev.setdefault(v, None)
    non_visited.append(v)
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
        break  # here the remaining vertices are unreachable.

    non_visited.remove(min_vertex)
    # Work through all neighbours of min_vertex.
    for n in graph[min_vertex]:
        alt = dist[min_vertex] + 1  # all weights are 1 here.
        if alt < dist[n]:
            dist[n] = alt
            prev[n] = min_vertex


# Get the shortest path by backtracking through prev and reversing the list.
path = []
vertex = end_vertex
while vertex != start_vertex:
    vertex = prev[vertex]
    path.append(vertex)
path.reverse()

print(f'Shortest path from {start_vertex} to {end_vertex}:')
print(path)
print(f'Number of steps: {len(path)}')
