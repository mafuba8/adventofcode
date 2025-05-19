#!/usr/bin/python3
# Advent of Code 2021 - Day 12, Part 1
# Benedikt Otto
#

# input_file = '../examples/example_12c.txt'
input_file = '../inputs/input_12.txt'

# Parse input into a graph.
graph = {}  # Graph as dict(key=vertex, val=set(neighbours)).
with open(input_file) as file:
    for line in file.readlines():
        v1, v2 = line.strip().split('-')
        # Add vertices.
        graph.setdefault(v1, set())
        graph.setdefault(v2, set())
        # Add v1 as neighbour of v2 and vice versa.
        graph[v1].add(v2)
        graph[v2].add(v1)


def count_paths(base_vertex: str, visited_vertices: set) -> int:
    """Counts all paths from base_vertex to the vertex 'end' which only uses each lowercase vertex at most once."""
    global graph

    if base_vertex == 'end':
        return 1  # End of recursion.

    # Count all paths.
    path_count = 0
    for n in graph[base_vertex]:
        # Vertices with uppercase name can be visited more than once.
        if n.isupper() or n not in visited_vertices:
            new_visited = set.union(visited_vertices, {base_vertex})
            path_count += count_paths(n, new_visited)
    return path_count


print(f'Paths through the cave system: {count_paths('start', set())}')
