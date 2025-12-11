#!/usr/bin/python3
# Advent of Code 2025 - Day 11, Part 1
# Benedikt Otto
#

# INPUT_FILE = '../examples/example_11.txt'
INPUT_FILE = '../inputs/input_11.txt'

# Parse input into a dict of lists.
connections = {}
with open(INPUT_FILE) as file:
    for line in file.readlines():
        l_device, l_output = line.strip().split(': ')
        connections[l_device] = l_output.split(' ')


def count_paths(device: str):
    """Recursively counts the number of paths from the given device to the reactor."""
    # Recursion end.
    if device == 'out':
        return 1

    # Recursively count the paths through all the neighbors.
    path_count = 0
    for next_dev in connections[device]:
        path_count += count_paths(next_dev)

    return path_count

print(f"Number of paths to the reactor: {count_paths('you')}.")
