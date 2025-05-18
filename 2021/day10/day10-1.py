#!/usr/bin/python3
# Advent of Code 2021 - Day 10, Part 1
# Benedikt Otto
#

# input_file = '../examples/example_10.txt'
input_file = '../inputs/input_10.txt'

# Parse input into list of lines.
nav_subsystem = []
with open(input_file) as file:
    for line in file.readlines():
        nav_subsystem.append(line.strip())


# Matching brace pairs.
brace_pairs = {'(': ')', ')': '(', '[': ']', ']': '[',
               '{': '}', '}': '{', '<': '>', '>': '<'}

# Check each line for corrupted chunks.
illegal_characters = []
for line in nav_subsystem:
    print(f'Line: {line}')
    stack = []
    for c in line:
        # Opening braces.
        if c in '([{<':
            stack.append(c)
        # Closing braces.
        elif c in ')]}>':
            expected_brace = brace_pairs[stack[-1]]
            if c == expected_brace:
                stack.pop()
            else:
                print(f"  Corrupted: Expected '{expected_brace}', but found '{c}' instead.")
                illegal_characters.append(c)
                break

# Calculate the syntax error score:
total_error_score = 0
for c in illegal_characters:
    match c:
        case ')':
            total_error_score += 3
        case ']':
            total_error_score += 57
        case '}':
            total_error_score += 1197
        case '>':
            total_error_score += 25137

print(f'Total syntax error score: {total_error_score}')
