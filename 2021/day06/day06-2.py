#!/usr/bin/python3
# Advent of Code 2021 - Day 6, Part 2
# Benedikt Otto
#
import functools

# input_file = '../examples/example_6.txt'
input_file = '../inputs/input_6.txt'

# Parse input into a tuple.
with open(input_file) as file:
    initial_state = (int(s) for s in file.readline().strip().split(','))


# Recursive approach using dynamic programming.
@functools.cache
def fish_count(fish_state, days):
    """Returns the number of fish that result from the initial fish_state after the given days."""
    if days == 0:
        return len(fish_state)

    total_count = 0
    for fish in fish_state:
        if fish > 0:
            total_count += fish_count((fish - 1,), days - 1)
        else:
            total_count += fish_count((6,), days - 1) + fish_count((8,), days - 1)
    return total_count


# Find the number of fish.
NUM_DAYS = 256
print(f'Number of fish after {NUM_DAYS} days: {fish_count(initial_state, NUM_DAYS)}')
