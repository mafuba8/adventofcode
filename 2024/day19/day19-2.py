#!/usr/bin/python3
# Advent of Code 2024 - Day 19, Part 2
# Benedikt Otto
#
import functools

# input_file = '../examples/example_19.txt'
input_file = '../inputs/input_19.txt'

# Parse input into lists of patterns and designs.
pattern_list = []
design_list = []
with open(input_file) as file:
    design_input = False
    for line in file.readlines():
        if line == '\n':
            design_input = True
        else:
            if design_input:
                design_list.append(line.strip())
            else:
                pattern_list = line.strip().split(', ')


@functools.cache
def match_pattern(design):
    """Finds patterns that match the beginning of the given design. Returns a list
    of pairs (pattern, design_rest) of matching patterns and the remainder of the design."""
    global pattern_list
    working_patterns = []
    for pattern in pattern_list:
        l = len(pattern)
        if design[:l] == pattern:
            working_patterns.append((pattern, design[l:]))
    return working_patterns


@functools.cache
def count_arrangements(design):
    """Counts the number of pattern arrangements that will result in the given design."""
    if design == '':
        return 1

    # Recursively count the arrangements of the rest of all patterns.
    arrangement_count = 0
    for pattern, design_rest in match_pattern(design):
        arrangement_count += count_arrangements(design_rest)
    return arrangement_count


# Run through all patterns and check if they are possible.
arrangement_sum = 0
for design in design_list:
    c = count_arrangements(design)
    print(f'Design: {design} - Number of arrangements: {c}')
    arrangement_sum += c

print(f'Sum of all arrangement counts: {arrangement_sum}')
