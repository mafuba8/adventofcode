#!/usr/bin/python3
# Advent of Code 2021 - Day 10, Part 2
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
completion_strings = []
for line in nav_subsystem:
    print(f'Line: {line}')
    is_corrupted = False
    stack = []
    for pos, c in enumerate(line):
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
                is_corrupted = True
                break

    # Complete non-corrupted lines.
    if not is_corrupted:
        # The line is completed by adding the pairs of all remaining braces on the stack.
        completion = ''
        while len(stack) > 0:
            a = stack.pop()
            completion += brace_pairs[a]
        print(f"  Incomplete: Completion via '{completion}'.")
        completion_strings.append(completion)


# Calculate the completion scores.
completion_scores = []
for string in completion_strings:
    x = 0
    for c in string:
        x = x * 5
        match c:
            case ')':
                x += 1
            case ']':
                x += 2
            case '}':
                x += 3
            case '>':
                x += 4
    completion_scores.append(x)

completion_scores.sort()
print(f'Completion scores: {completion_scores}')
print(f'Middle score: {completion_scores[len(completion_scores) // 2]}')
