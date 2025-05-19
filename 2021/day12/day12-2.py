#!/usr/bin/python3
# Advent of Code 2021 - Day 12, Part 2
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


def count_paths(base_vertex: str, visited_vertices: set, double_visited: bool) -> int:
    """Counts all paths from base_vertex to the vertex 'end' which only uses each lowercase vertex at most once.
    The double_visited parameter indicates, whether a lowercase vertex has already been visited twice. Otherwise,
    we still have the option to visit one lowercase vertex for a second time."""
    global graph

    if base_vertex == 'end':
        return 1  # End of recursion.

    path_count = 0
    if double_visited:
        # There has already been one lowercase vertex which has been visited twice.
        for n in graph[base_vertex]:
            new_visited = set.union(visited_vertices, {base_vertex})
            # Vertices with uppercase name can be visited more than once.
            if n.isupper() or n not in visited_vertices:
                path_count += count_paths(n, new_visited, True)
    else:
       # We can visit one lowercase vertex twice.
        for n in graph[base_vertex]:
            new_visited = set.union(visited_vertices, {base_vertex})
            # Vertices with uppercase name can always be visited more than once.
            if n.isupper():
                path_count += count_paths(n, new_visited, False)
            # For vertices with lowercase we need to check if it has been visited yet.
            elif n.islower():
                if n not in visited_vertices:
                    # Lowercase and not visited yet.
                    path_count += count_paths(n, new_visited, False)
                elif n not in ('start', 'end'):
                    # Lowercase and visited, but we decide to visit it again.
                    path_count += count_paths(n, new_visited, True)
    return path_count


print(f'Paths through the cave system where we can visit one small cave twice: '
      f'{count_paths('start', set(), False)}')
