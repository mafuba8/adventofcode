#!/usr/bin/python3
# Advent of Code 2024 - Day 7, Part 1
# Benedikt Otto
#
import re

# input_file = '../examples/example_7.txt'
input_file = '../inputs/input_7.txt'

# Parse input into list of equations tuple(results, [arguments]) ).
equation_list = []
regex = re.compile(r'^(\d+):\s([\d\s]+)$')
with open(input_file) as file:
    for line in file.readlines():
        search = regex.search(line)
        result = int(search.group(1))
        arguments = [x for x in search.group(2).strip().split(' ')]
        # arguments = [int(x) for x in search.group(2).strip().split(' ')]
        equation_list.append((result, arguments))


# Find all possible equations and check their results.
calibration_result = 0
for equation in equation_list:
    result, arguments = equation

    # Build list of possible equations.
    possible_results = [arguments[0]]
    for arg in arguments[1:]:
        # For both possible operators evaluate the result and store it back into possible_results.
        l = []
        while len(possible_results) > 0:
            s = possible_results.pop(0)
            sp = str(s) + ' + ' + arg
            sm = str(s) + ' * ' + arg
            l += [eval(sp), eval(sm)]
        possible_results = l

    # Find and sum up the results of equations that can be true.
    if result in possible_results:
        print(f'Equation {equation} can be true.')
        calibration_result += result


print(f'Total calibration result: {calibration_result}')
