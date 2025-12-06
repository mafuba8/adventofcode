#!/usr/bin/python3
# Advent of Code 2025 - Day 6, Part 2
# Benedikt Otto
#

# INPUT_FILE = '../examples/example_06.txt'
INPUT_FILE = '../inputs/input_06.txt'

# Parse input into list of number rows and a single operator list.
number_rows = []
operator_row = []
with open(INPUT_FILE) as file:
    for line in file.readlines():
        # Here we need to get the exact contents (except the line break).
        if '*' in line:
            operator_row = line[:-1]
        else:
            number_rows.append(line[:-1])


# Create list of tuples (op, num_digits).
operators = []
digit_count = 0
operator = ''
for char in operator_row:
    if char in '+*':
        operators.append((operator, digit_count))
        operator = char
        digit_count = 0
    else:
        digit_count += 1

# Remove the first (empty) operator and add the last one.
operators = operators[1:]
operators.append((operator, digit_count + 1))


def calculate_column(operator, digit_count, offset):
    """Calculates the result of the operator at the given offset."""
    col_start = 0 + offset
    col_end = digit_count + offset

    # Initial value.
    if operator == '*':
        result = 1
    else:
        result = 0

    # Pick the digits from the right spots and concatenate them.
    num = ''
    for k in reversed(range(col_start, col_end)):
        for num_row in number_rows:
            num += num_row[k]

        if operator == '*':
            result *= int(num)
        else:
            result += int(num)
        num = ''
    return result


# Run through operators and pick the right digits to add/multiply.
grand_total = 0
offset = 0
for operator, digit_count in operators:
    x = calculate_column(operator, digit_count, offset)
    print(x)
    grand_total += x
    offset += digit_count + 1

print(f'The grand total is {grand_total}.')
