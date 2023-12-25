#!/usr/bin/python3
# Advent of Code 2023 - Day 25, Part 1
# Benedikt Otto
import math
import random
from copy import deepcopy

# Open puzzle file and parse into list
lines = []
#with open('example_25.txt') as file:
with open('input_25.txt') as file:
    for line in file.readlines():
        lines.append(line.strip())


# Create set of vertices (modules) of the graph.
graph_vertices = set()
for line in lines:
    li = line.strip().split(': ')
    module = li[0]
    graph_vertices.add(module)
    for m in li[1].split(' '):
        graph_vertices.add(m)

# Set up graph with the given vertices.
graph = {}
for v in graph_vertices:
    graph.setdefault(v, [])

# Add all corresponding edges.
for line in lines:
    li = line.strip().split(': ')
    module = li[0]
    for m in li[1].split(' '):
        graph[module].append(m)
        graph[m].append(module)


def choose_random_edge(g):
    v1 = random.choice(list(g.keys()))
    v2 = random.choice(list(g[v1]))
    return v1, v2


def karger(contraction_graph):
    """KARGER'S MINIMUM CUT ALGORITHM.
    Contracts random edges until there are only two vertices left. The number of edges between those
    will be a cut in the original graph. Returns the length, the fully contracted graph and a dictionary
    that tells us which vertices got contracted."""
    length = []
    # contraction_dict[v] = list of vertices that were contracted into v.
    contraction_dict = {v: [v] for v in contraction_graph}
    while len(contraction_graph) > 2:
        v1, v2 = choose_random_edge(contraction_graph)  # we will contract the edge v1-v2 onto v1.
        if v1 == v2:
            continue  # Only contract when we have different vertices.

        # Add all neighbors of v2 to v1.
        contraction_graph[v1] += contraction_graph[v2]
        for x in contraction_graph[v2]:
            # on all neighbors x of v2 replace v2 with v1 as neighbor.
            contraction_graph[x].remove(v2)
            contraction_graph[x].append(v1)

        # Remove loops and then delete v2.
        while v1 in contraction_graph[v1]:
            contraction_graph[v1].remove(v1)
        del contraction_graph[v2]

        # Add all the contracted vertices of v2 to v1.
        contraction_dict[v1] += contraction_dict[v2]

    # Count the edges of the fully contracted graph.
    for v in contraction_graph.keys():
        length.append(len(contraction_graph[v]))
    return length[0], contraction_graph, contraction_dict


# Run Karger's algorithm until we find a cut of only three edges.
cut_number = 0
while cut_number != 3:
    cut_number, contracted_graph, contracted_dict = karger(deepcopy(graph))
    print(cut_number)
    #minimum = min(minimum, cut_number)

print('Fully contracted graph with a 3-cut:')
print(contracted_graph)
print()

print('Cutting the original graph along the respective edges will give us the two connected components:')
result_number = 1
for v in contracted_graph:
    print(f'Size {len(contracted_dict[v])}: Vertex {v} - {contracted_dict[v]}')
    result_number *= len(contracted_dict[v])

print()
print(f'Resulting number: {result_number}')
