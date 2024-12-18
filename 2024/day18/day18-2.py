#!/usr/bin/python3
# Advent of Code 2024 - Day 18, Part 2
# Benedikt Otto
#

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


def find_neighbours(vertex, space_dict):
    """Returns a list of neighbours of the given vertex."""
    neighbours = []
    # Neighbours are bordering tiles U/D/L/R that don't have a corrupted byte.
    x, y = vertex
    for ne in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
        if ne in space_dict and space_dict[ne] == '.':
            neighbours.append(ne)
    return neighbours


def build_graph(space_dict):
    """Returns the graph and vertex set derived from the given memory space dict."""
    vertex_set = set(space_dict.keys())
    graph = {}
    for v in vertex_set:
        graph.setdefault(v, find_neighbours(v, space_dict))
    return graph, vertex_set


def is_connected(graph, vertex_set):
    """Checks whether the start_vertex and end_vertex are connected."""
    # Depth-first-search to find the connected component of end_vertex.
    component = []
    stack = [end_vertex]
    while len(stack) > 0:
        v = stack.pop()
        if v not in component:
            component.append(v)
            for n in graph[v]:
                stack.append(n)
    return start_vertex in component


# Build Memory space as dict(key=xy, val=char) with the first 1024 bytes.
memory_space = {}
for x in range(MEM_SPACE_SIZE):
    for y in range(MEM_SPACE_SIZE):
        if (x, y) in byte_list[:NUM_BYTES_FALLEN]:
            memory_space.setdefault((x, y), '#')
        else:
            memory_space.setdefault((x, y), '.')

start_vertex = (0, 0)
end_vertex = (MEM_SPACE_SIZE - 1, MEM_SPACE_SIZE - 1)


# Perform a binary search to find the point after which we don't have a path anymore.
low_limit = 1024
high_limit = len(byte_list)
memory_space_low = memory_space.copy()
memory_space_high = memory_space.copy()

while low_limit != high_limit:
    middle_point = (high_limit + low_limit) // 2
    print(f'Checking after {middle_point} bytes have dropped.')

    # Build graph with all bytes until middle_point.
    memory_space = {}
    for x in range(MEM_SPACE_SIZE):
        for y in range(MEM_SPACE_SIZE):
            if (x, y) in byte_list[:middle_point]:
                memory_space.setdefault((x, y), '#')
            else:
                memory_space.setdefault((x, y), '.')
    memory_space_graph, memory_space_vertices = build_graph(memory_space)

    # Check if we still have a path.
    if is_connected(memory_space_graph, memory_space_vertices):
        print(f' Still connected => between {middle_point} and {high_limit}')
        low_limit = middle_point + 1
    else:
        print(f' Not connected a => between {low_limit} and {middle_point}')
        high_limit = middle_point

print()
print(f'After adding byte number {high_limit}, we do not have a path anymore.')
print(f'Last byte added: {byte_list[high_limit - 1]}')
