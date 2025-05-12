#!/usr/bin/python3
# Advent of Code 2021 - Day 7, Part 1
# Benedikt Otto
#

# input_file = '../examples/example_7.txt'
input_file = '../inputs/input_7.txt'

# Parse input into list.
start_pos_list = []
with open(input_file) as file:
    start_pos_list = [int(s) for s in file.readline().strip().split(',')]


def fuel_usage(pos_from, pos_to):
    """Returns the fuel needed to move from pos_from to pos_to."""
    d = abs(pos_to - pos_from)
    # Triangular numbers (sum of first n natural numbers).
    return (d * (d + 1)) // 2


# Try out all horizontal positions and calculate the fuel needed for it.
min_fuel = None
min_pos = 0
for pos in range(len(start_pos_list)):
    # Checking the fuel usage for the horizontal position pos.
    total_fuel = 0
    for crab_pos in start_pos_list:
        total_fuel += fuel_usage(pos, crab_pos)

    print(f'Position {pos}: {total_fuel} fuel.')
    if min_fuel is None:
        min_fuel = total_fuel

    if total_fuel < min_fuel:
        min_fuel = total_fuel
        min_pos = pos

print(f'Minimum fuel needed: {min_fuel} at horizontal position {min_pos}.')

