#!/usr/bin/python3
# Advent of Code 2022 - Day 6, Part 2
# Benedikt Otto

# input_file = '../examples/example_6.txt'
input_file = '../inputs/input_6.txt'

# Parse input
buffer = ''
with open(input_file) as file:
    buffer += file.readline().strip()

# Run through 14-character sets.
for k in range(14, len(buffer)):
    b = buffer[k-14:k]
    # First occurrence of 14 distinct characters.
    if len(set(b)) == 14:
        print(f'First message marker is at character number {k}.')
        break

