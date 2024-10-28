#!/usr/bin/python3
# Advent of Code 2023 - Day 17, Part 1
# Benedikt Otto
#
# OLD VERSION with vertex = (x, y, direction, steps).
# Takes rather long to compute (>1 hour).
import math

# Open puzzle file and parse into dict(key=(x, y), val=symbol)
traffic_map = {}
with open('../examples/example_17.txt') as file:
#with open('input_17.txt') as file:
    for row_num, row in enumerate(file.readlines()):
        row = row.strip()
        for col_num, char in enumerate(row):
            traffic_map.setdefault((row_num, col_num), int(char))


map_height = max([t[0] for t in traffic_map.keys()]) + 1
map_width = max([t[1] for t in traffic_map.keys()]) + 1


def get_neighbors(vertex_x, vertex_y, direction='', vertex_steps=0):
    """Create the list of all valid neighbors of the given vertex."""
    directions = ['U', 'D', 'L', 'R']
    # Because we can't do a reverse, remove the invalid direction.
    match direction:
        case 'U':
            directions.remove('D')
        case 'D':
            directions.remove('U')
        case 'L':
            directions.remove('R')
        case 'R':
            directions.remove('L')

    neighbors = []
    for d in directions:
        steps = vertex_steps
        match d:
            case 'U':
                if direction == 'U':
                    steps += 1
                else:
                    steps = 1
                new_x = vertex_x - 1
                new_y = vertex_y
                if 0 <= new_x < map_height and 0 <= new_y < map_width and steps <= 3:
                    weight = traffic_map[(new_x, new_y)]
                    ne = ((new_x, new_y, 'U', steps), weight)
                    neighbors.append(ne)

            case 'D':
                if direction == 'D':
                    steps += 1
                else:
                    steps = 1
                new_x = vertex_x + 1
                new_y = vertex_y
                if 0 <= new_x < map_height and 0 <= new_y < map_width and steps <= 3:
                    weight = traffic_map[(new_x, new_y)]
                    ne = ((new_x, new_y, 'D', steps), weight)
                    neighbors.append(ne)

            case 'L':
                if direction == 'L':
                    steps += 1
                else:
                    steps = 1
                new_x = vertex_x
                new_y = vertex_y - 1
                if 0 <= new_x < map_height and 0 <= new_y < map_width and steps <= 3:
                    weight = traffic_map[(new_x, new_y)]
                    ne = ((new_x, new_y, 'L', steps), weight)
                    neighbors.append(ne)

            case 'R':
                if direction == 'R':
                    steps += 1
                else:
                    steps = 1
                new_x = vertex_x
                new_y = vertex_y + 1
                if 0 <= new_x < map_height and 0 <= new_y < map_width and steps <= 3:
                    weight = traffic_map[(new_x, new_y)]
                    ne = ((new_x, new_y, 'R', steps), weight)
                    neighbors.append(ne)
    return neighbors


# Define source vertex and create the graph.
source_vertex = (0, 0, '', 0)
vertex_set = set()
vertex_set.add(source_vertex)

# Create set of all vertices.
for coord in traffic_map:
    (coord_x, coord_y) = coord
    for direction in ['U', 'D', 'L', 'R']:
        for steps in range(1, 4):
            vertex = (coord_x, coord_y, direction, steps)
            vertex_set.add(vertex)

# Create graph as dict(key=vertex, val=[neighbors])
traffic_graph = {}
for vertex in vertex_set:
    (vertex_x, vertex_y, direction, steps) = vertex
    neighbors = []
    n_list = get_neighbors(vertex_x, vertex_y, direction, steps)
    for n in n_list:
        neighbors.append(n)

    traffic_graph.setdefault(vertex, neighbors)

# Add destination vertex, its neighbors and add the destination as neighbor of all adjacent vertices.
destination_vertex = (map_height - 1, map_width - 1, '', 0)
destination_neighbors = []
for k in range(1, 4):
    for direction in ['D', 'R']:
        vertex = (destination_vertex[0], destination_vertex[1], direction, k)
        destination_neighbors.append((vertex, 0))
        # Add edges to destination_vertex to all adjacent vertices.
        traffic_graph[vertex].append((destination_vertex, 0))
traffic_graph.setdefault(destination_vertex, destination_neighbors)


# DIJKSTRA
non_visited = []
dist = {}
prev = {}
for v in traffic_graph:
    # Prepare dicts.
    dist.setdefault(v, math.inf)
    prev.setdefault(v, None)
    non_visited.append(v)
dist[source_vertex] = 0

while len(non_visited) > 0:
    if len(non_visited) % 10000 == 0:
        print(len(non_visited))
    # Get vertex with minimum dist:
    minimum = math.inf
    for v in non_visited:
        if dist[v] < minimum:
            minimum = dist[v]
            min_vertex = v

    # Shortcut because we are only interested in the shortest path source -> destination.
    if min_vertex == destination_vertex:
        break

    if minimum == math.inf:
        break  # Here the remaining nodes are unreachable.

    non_visited.remove(min_vertex)
    # Work through all neighbors of min_vertex.
    for n in traffic_graph[min_vertex]:
        (n_vertex, n_weight) = n
        # In this graph all edge values are 1.
        alt = dist[min_vertex] + n_weight
        if alt < dist[n_vertex]:
            dist[n_vertex] = alt
            prev[n_vertex] = min_vertex


# Get the shortest path by backtracking through prev and reversing the list.
path = []
node = destination_vertex
while node != source_vertex:
    node = prev[node]
    path.append(node)
path.reverse()

print(f'Shortest path to {destination_vertex}:')
print(path)
print(f'Length: {dist[destination_vertex]}')
