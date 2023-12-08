#!/usr/bin/python3
# Advent of Code 2023 - Day 8, Part 2
# Benedikt Otto
import functools
import itertools
import re
import math

# Open puzzle file.
#with open('example_8-3.txt') as file:
with open('input_8.txt') as file:
    lines = file.readlines()

# Parse input file.
instructions = []
for d in lines[0].strip():
    instructions.append(d)

#regex = re.compile(r'(.{3})\s=\s\((.{3}),(.{3})\)')
node_dict = {}
for line in lines[2:]:
    a = line.split(' = ')
    node_name = a[0]
    b = a[1].strip().replace('(', '').replace(')', '').split(', ')
    node_dirs = (b[0], b[1])
    node_dict[node_name] = node_dirs


# Find starting nodes.
starting_nodes = []
for node_name in node_dict.keys():
    # Starting nodes always end with 'A'.
    if node_name[2] == 'A':
        starting_nodes.append(node_name)


def move(direction, current_node):
    """Finds the next node if you start from current_node and go in direction d."""
    (node_left, node_right) = node_dict[current_node]
    if d == 'L':
        return node_left
    elif d == 'R':
        return node_right
    else:
        return None


# Find minimum step count for each starting node and add them to the list.
step_count_list = []
for index, node in enumerate(starting_nodes):
    print(f'Starting node: {node}')

    step_count = 0
    for d in itertools.cycle(instructions):
        step_count += 1
        new_node = move(d, node)
        node = new_node

        # End node is reached when the last letter of the node is a 'Z'.
        if node[2] == 'Z':
            break

    print(f'Number of steps: {step_count}')
    step_count_list.append(step_count)


# The minimum step count where you are on all end nodes at the same time is the
# least common multiple of all the individual step counts.
lcm = functools.reduce(math.lcm, step_count_list)
print('')
print(f'Minimum steps until you are only on end nodes: {lcm}')
