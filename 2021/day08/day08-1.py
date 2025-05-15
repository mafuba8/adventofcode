#!/usr/bin/python3
# Advent of Code 2021 - Day 8, Part 1
# Benedikt Otto
#

# input_file = '../examples/example_8.txt'
input_file = '../inputs/input_8.txt'

# Parse input into list of entries.
entries = []
with open(input_file) as file:
    for line in file.readlines():
        sig, out = line.strip().split(' | ')
        entries.append((sig.split(' '), out.split(' ')))


# Count the number of times that 1, 4, 7 or 8 appear in the outputs.
count = 0
for entry in entries:
    sig, out = entry
    for val in out:
        # (1) <> 2, (4) <> 4, (7) <> 3, (8) <> 7.
        if len(val) in {2, 3, 4, 7}:
            count += 1

print(f'Number of times that 1, 4, 7 or 8 appears in the output values: {count}.')
