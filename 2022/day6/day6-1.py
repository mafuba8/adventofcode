#!/usr/bin/python3
# Advent of Code 2022 - Day 6, Part 1
# Benedikt Otto

# input_file = '../examples/example_6.txt'
input_file = '../inputs/input_6.txt'

# Parse input
buffer = ''
with open(input_file) as file:
    buffer += file.readline().strip()

# Run through 4-character sets.
for k in range(4, len(buffer)):
    b = buffer[k-4:k]
    # First occurrence of 4 distinct characters.
    if len(set(b)) == 4:
        print(f'First packet marker is at character number {k}.')
        break

