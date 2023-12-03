#!/usr/bin/python3
# Advent of Code 2023 - Day 3, Part 1
# Benedikt Otto
import re

# Open puzzle file
#with open('example_3.txt') as file:
with open('input_3.txt') as file:
    lines = file.readlines()


def is_adj_to_symbol(row_num, start, end):
    """Checks whether the symbols on row 'row_num' between indices 'start' and 'end'
    are adjacent to a symbol (non-digit, not a dot '.')."""
    # Determine which chars need to be scanned for symbols.
    scan_dict = {'top': True, 'bottom': True, 'left': True, 'right': True}
    if row_num == 0:
        scan_dict['top'] = False
    if row_num == len(lines) - 1:
        scan_dict['bottom'] = False
    if start == 0:
        scan_dict['left'] = False
    if end == len(lines[row_num]) - 1:
        scan_dict['right'] = False

    # Put all the scannable chars in one search string.
    search_area = ""
    if scan_dict['top']:
        # Top-left character.
        if scan_dict['left']:
            search_area += lines[row_num - 1][start - 1]
        # Characters directly over the number.
        search_area += lines[row_num - 1][start:end]
        # Top-right character.
        if scan_dict['right']:
            search_area += lines[row_num - 1][end]
    if scan_dict['bottom']:
        # Bottom-left character.
        if scan_dict['left']:
            search_area += lines[row_num + 1][start - 1]
        # Characters directly under the number.
        search_area += lines[row_num + 1][start:end]
        # Bottom-right character.
        if scan_dict['right']:
            search_area += lines[row_num + 1][end]
    if scan_dict['left']:
        # Character directly left of the number.
        search_area += lines[row_num][start - 1]
    if scan_dict['right']:
        # Character directly right of the number.
        search_area += lines[row_num][end]

    # Symbols are all characters except digits and the dot '.'
    re_symbol = re.compile(r'[^\d.]')
    if re_symbol.search(search_area) is not None:
        return True
    else:
        return False


# Finding the part numbers.
part_num_list = []
part_num_total = 0

# Numbers are one or more connected digits
re_number = re.compile(r'\d+')
for row_num, line in enumerate(lines):
    for match in re_number.finditer(line):
        # Check for each matched number whether they are close to a symbol and add them to the list
        if is_adj_to_symbol(row_num, match.start(), match.end()):
            part_num = int(match.group())
            part_num_list.append(part_num)
            part_num_total += part_num


print('Part numbers:')
print(part_num_list)

print('')
print('Sum of part numbers:', part_num_total)
