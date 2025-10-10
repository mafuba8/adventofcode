#!/usr/bin/python3
# Advent of Code 2020 - Day 10, Part 2
# Benedikt Otto
#
import functools

# input_file = '../examples/example_10a.txt'
# input_file = '../examples/example_10b.txt'
input_file = '../inputs/input_10.txt'

# Parse input into a list of numbers.
adapter_list = []
with open(input_file) as file:
    for line in file.readlines():
        adapter_list.append(int(line))


@functools.cache
def count_arrangements(initial_voltage):
    """Counts the number of adapter arrangements possible when we start with the given initial voltage."""
    global adapter_list
    # The built-in adapter always has three more joltage than the highest adapter in the list.
    max_adapter = max(adapter_list)

    # Recursion end.
    if initial_voltage == max_adapter:
        return 1

    num_arrangements = 0
    # Check possible adapters recursively.
    if initial_voltage + 1 in adapter_list:
        num_arrangements += count_arrangements(initial_voltage + 1)

    if initial_voltage + 2 in adapter_list:
        num_arrangements += count_arrangements(initial_voltage + 2)

    if initial_voltage + 3 in adapter_list:
        num_arrangements += count_arrangements(initial_voltage + 3)

    return num_arrangements

print(f'Number of possible adapter arrangements: {count_arrangements(0)}.')
