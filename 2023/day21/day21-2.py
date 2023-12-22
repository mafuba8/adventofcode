#!/usr/bin/python3
# Advent of Code 2023 - Day 21, Part 2
import math

# Open puzzle file and parse it.
map_dict = {}
start = (0, 0)
map_width = 0
map_height = 0
#with open('example_21.txt') as file:
with open('input_21.txt') as file:
    lines = file.readlines()
    map_height = len(lines)
    for row_num, row in enumerate(lines):
        map_width = len(row) - 1
        for col_num, char in enumerate(row.strip()):
            map_dict.setdefault((row_num, col_num), char)
            if char == 'S':
                start = (row_num, col_num)

# Build graph for dijkstra, so we can assign each plot in the map the shortest number of steps needed to get there.
map_graph = {}
for x in range(map_height):
    for y in range(map_width):
        vertex = (x, y)
        if map_dict[vertex] == '#':
            continue
        adjacent = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
        neighbors = []
        for v in adjacent:
            if 0 <= v[0] < map_height and 0 <= v[1] < map_width and map_dict[v] != '#':
                neighbors.append(v)
        map_graph.setdefault(vertex, neighbors)


# DIJKSTRA ALGORITHM.
non_visited = []
dist = {}
prev = {}
for v in map_graph:
    # Prepare dicts.
    dist.setdefault(v, math.inf)
    prev.setdefault(v, None)
    non_visited.append(v)
dist[start] = 0

while len(non_visited) > 0:
    # Get vertex with minimum dist:
    minimum = math.inf
    for v in non_visited:
        if dist[v] < minimum:
            minimum = dist[v]
            min_vertex = v

    if minimum == math.inf:
        break  # Here the remaining nodes are unreachable.

    non_visited.remove(min_vertex)
    # Work through all neighbors of min_vertex.
    for n in map_graph[min_vertex]:
        # In this graph all edge values are 1.
        alt = dist[min_vertex] + 1
        if alt < dist[n]:
            dist[n] = alt
            prev[n] = min_vertex


# Geometric solution with the help of
#   https://github.com/villuna/aoc23/wiki/A-Geometric-solution-to-advent-of-code-2023,-day-21
# All the reachable plots are within a giant diamond that contains some copies (squares)
# of the full map and an additional set of corners (triangles). Because the diamond is perfectly
# centered, their number is easy to compute.

# Number of squares that we can traverse by going horizontal.
horizontal_number = int((26501365 - (map_width - 1)/2) / map_width)  # 202300

# Number of even/odd squares within the giant diamond.
num_even_squares = horizontal_number ** 2
num_odd_squares = (horizontal_number + 1) ** 2

# Number of even/odd triangles that are cut out.
# In order to make the diamond, we later need to add the even triangles to the squares
# and remove the odd triangles.
num_even_triangles = horizontal_number
num_odd_triangles = horizontal_number + 1

# Find number of plots with even/odd parity in one square:
square_even_count = len([v for v in map_graph if dist[v] % 2 == 0])
square_odd_count = len([v for v in map_graph if dist[v] % 2 == 1])

# Find number of plots with even/odd parity just inside the triangles.
# Triangles are those plot points that have a manhattan distance greater than 65 to the middle (start).
triangle_even_count = len([v for v in map_graph if abs(v[0] - start[0]) + abs(v[1] - start[1]) > 65 and dist[v] % 2 == 0])
triangle_odd_count = len([v for v in map_graph if abs(v[0] - start[0]) + abs(v[1] - start[1]) > 65 and dist[v] % 2 == 1])

# Count points in all the squares.
total_number = num_odd_squares * square_odd_count + num_even_squares * square_even_count

# Subtract points in odd triangles and add points in even triangles.
total_number -= num_odd_triangles * triangle_odd_count
total_number += num_even_triangles * triangle_even_count

print(f'Total number of reachable plots: {total_number}.')
