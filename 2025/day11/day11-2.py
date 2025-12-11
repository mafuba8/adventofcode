#!/usr/bin/python3
# Advent of Code 2025 - Day 11, Part 2
# Benedikt Otto
#
import functools

# INPUT_FILE = '../examples/example_11b.txt'
INPUT_FILE = '../inputs/input_11.txt'

# Parse input into a dict of lists.
connections = {}
with open(INPUT_FILE) as file:
    for line in file.readlines():
        l_device, l_output = line.strip().split(': ')
        connections[l_device] = l_output.split(' ')


@functools.cache
def count_paths(device_from: str, device_to: str) -> int:
    """Counts the number of paths from device_from to device_to."""
    global connections
    # Recursion end.
    if device_from == device_to:
        return 1
    if device_from == 'out':
        return 0

    # Recursively count the paths through all the neighbors.
    path_count = 0
    for neighbor in connections[device_from]:
        path_count += count_paths(neighbor, device_to)
    return path_count


# We assume that there are no loops in the graph, so one of the two path counts is always zero.
# Paths srv -> fft -> dac -> out
count_fft_dac = count_paths('svr', 'fft') * count_paths('fft', 'dac') * count_paths('dac', 'out')
# Paths srv -> dac -> fft -> out
count_dac_fft = count_paths('svr', 'dac') * count_paths('dac', 'fft') * count_paths('fft', 'out')

result = count_fft_dac + count_dac_fft
print(f'Number of paths from svr to the reactor through fft and dac: {result}.')
