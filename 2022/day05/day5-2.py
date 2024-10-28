#!/usr/bin/python3
# Advent of Code 2022 - Day 5, Part 2
# Benedikt Otto
import re

# input_file = '../examples/example_5.txt'
input_file = '../inputs/input_5.txt'

# Parse input into boxes and procedure.
procedure = []  # List of triples.
box_rows = []  # List of rows.

boxes_part = True
regex_procedure = re.compile(r'^move\s(\d+)\sfrom\s(\d+)\sto\s(\d+)$')
with open(input_file) as file:
    for line in file.readlines():
        if line == '\n':
            boxes_part = False
            continue
        if boxes_part:
            box_rows.append([line[n] for n in range(1, len(line) + 1, 4)])
        else:
            result = regex_procedure.search(line)
            res = result.groups()
            procedure.append(tuple([int(s) for s in res]))

# Run through rows bottom-up to build the stacks.
num_stacks = len(box_rows[0])
box_stacks = [[] for n in range(num_stacks)]
for row in reversed(box_rows[:num_stacks]):
    for k in range(num_stacks):
        if row[k] != ' ':
            box_stacks[k].append(row[k])


# Execute the procedure on the box stacks.
for cr_num, cr_from, cr_to in procedure:
    # To retain the order we pop the crates onto a temporary stack.
    tmp_stack = []
    for k in range(cr_num):
        # Crate no. in procedure start at 1.
        cr = box_stacks[cr_from - 1].pop()
        tmp_stack.append(cr)

    # Reverse temp stack before putting them on top of the new stack.
    tmp_stack.reverse()
    box_stacks[cr_to - 1] += tmp_stack

# Collect names of crates at the top of each stack.
top_crates = ''
for st in box_stacks:
    top_crates += st[-1]

print('Final box arrangement:')
print(box_stacks)
print(f'Crates on top: {top_crates}')
