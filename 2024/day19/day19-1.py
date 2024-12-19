#!/usr/bin/python3
# Advent of Code 2024 - Day 19, Part 1
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
    # Check if the first few characters in the design matches with any pattern.
    for pattern in pattern_list:
        l = len(pattern)
        if design[:l] == pattern:
            working_patterns.append((pattern, design[l:]))
    return working_patterns


@functools.cache
def check_design(design):
    """Checks if the given design can be realized with the available patterns."""
    if design == '':
        return True

    # Recursively check the rest of all matching patterns.
    for pattern, design_rest in match_pattern(design):
        if check_design(design_rest):
            return True
    return False


# Run through all patterns and check if they are possible.
count_possible = 0
for design in design_list:
    if check_design(design):
        print(f' Design: {design} - Possible: yes')
        count_possible += 1
    else:
        print(f' Design: {design} - Possible: no')

print(f'Number of possible Designs: {count_possible}')
