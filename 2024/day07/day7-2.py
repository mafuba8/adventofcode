#!/usr/bin/python3
# Advent of Code 2024 - Day 7, Part 2
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
    possible_equations = [arguments[0]]
    for arg in arguments[1:]:
        l = []
        while len(possible_equations) > 0:
            s = possible_equations.pop()
            sp = str(s) + ' + ' + arg
            sm = str(s) + ' * ' + arg
            sc = str(s) + ' || ' + arg
            l += [sp, sm, sc]
        possible_equations = l

    # Evaluate all possible equations.
    possible_results = []
    for eq in possible_equations:
        eq_as_list = eq.split(' ')
        # Evaluate the equation left-to-right.
        val = eq_as_list.pop(0)
        while len(eq_as_list) > 0:
            op = eq_as_list.pop(0)
            arg = eq_as_list.pop(0)
            match op:
                case '+':
                    x = int(val) + int(arg)
                case '*':
                    x = int(val) * int(arg)
                case '||':
                    x = val + arg  # String concatenation.
            val = str(x)

        # Add the result to the list of possible results.
        possible_results.append(int(val))

    # Find and sum up the results of equations that can be true.
    if result in possible_results:
        print(f'Equation {equation} can be true.')
        calibration_result += result


print(f'Total calibration result: {calibration_result}')