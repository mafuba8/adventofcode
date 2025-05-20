#!/usr/bin/python3
# Advent of Code 2021 - Day 14, Part 1
# Benedikt Otto
#

# input_file = '../examples/example_14.txt'
input_file = '../inputs/input_14.txt'

# Parse input.
poly_template = []
insertion_rules = {}
with open(input_file) as file:
    first_part = True
    for line in file.readlines():
        if first_part:
            # Polymer template.
            if line == '\n':
                first_part = False
            else:
                poly_template = list(line.strip())
        else:
            # Pair insertion rules.
            req, ins = line.strip().split(' -> ')
            insertion_rules.setdefault(req, ins)


NUM_STEPS = 10
# Apply the insertion several times.
for step in range(NUM_STEPS):
    # Make a list of elements to be inserted.
    poly_insert = []
    for idx in range(len(poly_template) - 1):
        s = f'{poly_template[idx]}{poly_template[idx+1]}'
        poly_insert.append(insertion_rules[s])

    # Insert the elements on every second index.
    poly_new = []
    for idx in range(len(poly_template) + len(poly_insert)):
        if idx % 2 == 0:
            poly_new.append(poly_template[idx // 2])
        else:
            poly_new.append(poly_insert[(idx-1) // 2])
    poly_template = poly_new

# Count how many times each element appears.
element_tally = {}
for c in poly_template:
    if c in element_tally:
        element_tally[c] += 1
    else:
        element_tally.setdefault(c, 1)

print(element_tally)
print(f'Difference count between most common and least common element: '
      f'{max(element_tally.values()) - min(element_tally.values())}')
