#!/usr/bin/python3
# Advent of Code 2023 - Day 8, Part 1
# Benedikt Otto
import itertools
import re

# Open puzzle file.
#with open('example_8-3.txt') as file:
with open('input_8.txt') as file:
    lines = file.readlines()


instructions = []
# Parse input.
for d in lines[0].strip():
    instructions.append(d)

regex = re.compile(r'(.{3})\s=\s\((.{3}),(.{3})\)')
node_dict = {}
for line in lines[2:]:
    a = line.split(' = ')
    node_name = a[0]
    b = a[1].strip().replace('(', '').replace(')', '').split(', ')
    node_dirs = (b[0], b[1])
    node_dict[node_name] = node_dirs


def move(direction, current_node):
    """Finds the next node if you start from current_node and go in direction d."""
    (node_left, node_right) = node_dict[current_node]
    if d == 'L':
        return node_left
    elif d == 'R':
        return node_right
    else:
        return None


starting_node = 'AAA'
step_count = 0
# Cycle through the instructions until we end up on the 'ZZZ' node.
for d in itertools.cycle(instructions):
    step_count += 1
    new_node = move(d, starting_node)
    starting_node = new_node

    # End the loop if we are on the 'ZZZ' node.
    if new_node == 'ZZZ':
        break


print(f'Total numbers of steps: {step_count}')
