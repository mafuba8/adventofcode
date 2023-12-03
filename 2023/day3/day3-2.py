#!/usr/bin/python3
# Advent of Code 2023 - Day 3, Part 2
# Benedikt Otto
import re

# Open puzzle file
#with open('example_3.txt') as file:
with open('input_3.txt') as file:
    lines = file.readlines()


def list_adj_numbers(row_num, col_num):
    """Lists all the numbers that are adjacent to the given square (row_num, col_num)."""
    # Determine whether the top and/or bottom line can be scanned.
    scan_top = True
    scan_bottom = True
    if row_num == 0:
        scan_top = False
    if row_num == len(lines) - 1:
        scan_bottom = False

    # Numbers are one or more connected digits
    re_number = re.compile(r'\d+')

    # Scan all potential squares for a number.
    adj_num_list = []

    if scan_top:
        # Scan line over the symbol for numbers.
        for match in re_number.finditer(lines[row_num - 1]):
            # Check if the number is close enough to the symbol.
            if abs(col_num - match.start()) <= 1 or abs(col_num - match.end() + 1) <= 1:
                adj_num_list.append(int(match.group()))

    # Scan left and right side.
    for match in re_number.finditer(lines[row_num]):
        # Check if the number is close enough to the symbol.
        if abs(col_num - match.start()) <= 1 or abs(col_num - match.end() + 1) <= 1:
            adj_num_list.append(int(match.group()))

    if scan_bottom:
        # Scan line below the symbol for numbers.
        for match in re_number.finditer(lines[row_num + 1]):
            # Check if the number is close enough to the symbol.
            if abs(col_num - match.start()) <= 1 or abs(col_num - match.end() + 1) <= 1:
                adj_num_list.append(int(match.group()))

    return adj_num_list


# Finding the part numbers.
gear_ratio_list = []
gear_ratio_total = 0

# Find stars '*' and determine their gear numbers (if they are a valid gear).
re_star = re.compile(r'\*')
for row_num, line in enumerate(lines):
    for match in re_star.finditer(line):
        # For each star find the list of adjacent part numbers
        adj_num_list = list_adj_numbers(row_num, match.start())

        print(f'* found at ({row_num}, {match.start()}) - ', end='')
        print('Adjacent part numbers: ', end='')

        print(adj_num_list)
        # A star is only a valid gear if there are exactly two numbers adjacent to it.
        if len(adj_num_list) == 2:
            gear_ratio = adj_num_list[0] * adj_num_list[1]
            print(f' => Gear ratio is {gear_ratio}.')
            gear_ratio_list.append(gear_ratio)
            gear_ratio_total += gear_ratio


print('')
print('Gear ratio list:')
print(gear_ratio_list)

print('')
print('Sum of gear ratios:', gear_ratio_total)
