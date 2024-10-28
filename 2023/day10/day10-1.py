#!/usr/bin/python3
# Advent of Code 2023 - Day 10, Part 1
# Benedikt Otto
import math

# Open puzzle file.
#with open('example_10.txt') as file:
with open('../inputs/input_10.txt') as file:
    lines = file.readlines()

# Assuming rectangular area (accounting for \n).
height = len(lines)
width = len(lines[0]) - 1

# Parse input into dict with key=Tuple(coords) and val=Symbol
pipes = {}
for row, line in enumerate(lines):
    for col, s in enumerate(line.strip()):
        pipes[(row, col)] = s


def connectable(coord, direction):
    """Checks if the pipe at coords can be connected in the direction "NORTH", "SOUTH, "EAST" or "WEST"."""
    is_connectable = False
    (row, col) = coord

    next_coord = (0, 0)
    viable_symbols = []
    match direction:
        case "NORTH":
            next_coord = (row - 1, col)
            viable_symbols = ['|', '7', 'F']
        case "SOUTH":
            next_coord = (row + 1, col)
            viable_symbols = ['|', 'L', 'J']
        case "EAST":
            next_coord = (row, col + 1)
            viable_symbols = ['-', 'J', '7']
        case "WEST":
            next_coord = (row, col - 1)
            viable_symbols = ['-', 'L', 'F']

    # Connectable only if the pipe in that direction is within the rectangle
    # and it is one of the viable symbols.
    if 0 <= next_coord[0] < height and 0 <= next_coord[1] < width:
        is_connectable = pipes[next_coord] in viable_symbols

    return is_connectable


# Build graph as dict(key=coords, val=[neighbors])
graph = {}
for coord in pipes:
    (row, col) = coord
    north_coord = (row - 1, col)
    south_coord = (row + 1, col)
    west_coord = (row, col - 1)
    east_coord = (row, col + 1)

    neighbors = []
    # TODO: refactor using a dict of directions.
    match pipes[coord]:
        case '|':
            if connectable(coord, "NORTH"):
                neighbors.append(north_coord)
            if connectable(coord, "SOUTH"):
                neighbors.append(south_coord)
        case '-':
            if connectable(coord, "EAST"):
                neighbors.append(east_coord)
            if connectable(coord, "WEST"):
                neighbors.append(west_coord)
        case 'F':
            if connectable(coord, "EAST"):
                neighbors.append(east_coord)
            if connectable(coord, "SOUTH"):
                neighbors.append(south_coord)
        case '7':
            if connectable(coord, "SOUTH"):
                neighbors.append(south_coord)
            if connectable(coord, "WEST"):
                neighbors.append(west_coord)
        case 'J':
            if connectable(coord, "WEST"):
                neighbors.append(west_coord)
            if connectable(coord, "NORTH"):
                neighbors.append(north_coord)
        case 'L':
            if connectable(coord, "NORTH"):
                neighbors.append(north_coord)
            if connectable(coord, "EAST"):
                neighbors.append(east_coord)
        case 'S':
            # Special case for the start 'S', could connect in all directions.
            if connectable(coord, "NORTH"):
                neighbors.append(north_coord)
            if connectable(coord, "SOUTH"):
                neighbors.append(south_coord)
            if connectable(coord, "EAST"):
                neighbors.append(east_coord)
            if connectable(coord, "WEST"):
                neighbors.append(west_coord)
            # Also remember S as the source node.
            source_node = coord
    graph.setdefault(coord, neighbors)

# Determine distance of all nodes to source using the Dijkstra-Algorithm.
#   dist[v] = distance from source to v
#   prev[v] = previous vertex that has the shortest distance to v
non_visited = []
dist = {}
prev = {}
for v in graph:
    # Prepare dicts.
    dist.setdefault(v, math.inf)
    prev.setdefault(v, None)
    non_visited.append(v)
dist[source_node] = 0

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
    for n in graph[min_vertex]:
        # In this graph all edge values are 1.
        alt = dist[min_vertex] + 1
        if alt < dist[n]:
            dist[n] = alt
            prev[n] = min_vertex

# Get node with the maximum non-infinity value.
max_steps = 0
steps_node = None
for v in dist:
    steps = dist[v]
    if steps != math.inf:
        max_steps = max(steps, max_steps)
        steps_node = v

print(f'Max Steps are {max_steps}.')
