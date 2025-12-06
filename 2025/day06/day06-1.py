#!/usr/bin/python3
# Advent of Code 2025 - Day 6, Part 1
# Benedikt Otto
#

# INPUT_FILE = '../examples/example_06.txt'
INPUT_FILE = '../inputs/input_06.txt'

# Parse input into list of number rows and a single operator list.
number_rows = []
operator_row = []
with open(INPUT_FILE) as file:
    for line in file.readlines():
        if '*' in line:
            operator_row = line.strip().split()
        else:
            r = line.strip().split()
            r = list(map(int, r))
            number_rows.append(r)


# Work through all columns.
grand_total = 0
for col in range(len(operator_row)):
    result = 0
    if operator_row[col] == '+':
        result = 0
        for r in number_rows:
            result += r[col]
    elif operator_row[col] == '*':
        result = 1
        for r in number_rows:
            result *= r[col]
    grand_total += result

print(f'The grand total is {grand_total}.')
