#!/usr/bin/python3
# Advent of Code 2020 - Day 1, Part 1
# Benedikt Otto
#

# input_file = '../examples/example_1.txt'
input_file = '../inputs/input_1.txt'

# Parse input into a list.
expense_report = []
with open(input_file) as file:
    for line in file.readlines():
        expense_report.append(int(line))


# Run through all pairs and check if they sum up to 2020.
for k in range(len(expense_report)):
    a = expense_report[k]
    for b in expense_report[k:]:
        if a + b == 2020:
            print(f'The two entries are {a} and {b}, multiplying up to {a*b}.')
