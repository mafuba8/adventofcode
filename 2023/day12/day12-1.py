#!/usr/bin/python3
# Advent of Code 2023 - Day 12, Part 1
# Benedikt Otto
import re
import itertools

# Open puzzle file.
#with open('example_12.txt') as file:
with open('../inputs/input_12.txt') as file:
    lines = file.readlines()

# Parse puzzle file.
# records = list(tuple(string, pattern))
records = []
regex = re.compile(r'([.?#]*)\s((\d+,)*\d+)')
for line in lines:
    search = regex.search(line)
    string = search.group(1)
    pattern = search.group(2).split(',')

    records.append((string, [int(c) for c in pattern]))


def find_pattern(line):
    """Returns the pattern of the record as a list."""
    line += '\n'
    pattern = []
    count = 0
    for c in line:
        if c == '#':
            count += 1
        elif c == '.' or c == '\n':
            if count > 0:
                pattern.append(count)
                count = 0
    return pattern


total_arrangement_count = 0
for string, pattern in records:
    # Determine how many '#' are missing.
    total_sum = sum(pattern)
    count_num_signs = len([c for c in string if c == '#'])
    remaining_num_signs = total_sum - count_num_signs

    # Get the list of indices for all '?'.
    unknown_places = []
    for num, c in enumerate(string):
        if c == '?':
            unknown_places.append(num)

    # Try out each combination of '#' on the '?' spots and check if it has the right pattern.
    arrangement_count = 0
    for comb in itertools.combinations(unknown_places, remaining_num_signs):
        temp = list(string)
        # Replace the '?' according to the combination comb.
        for k in range(len(temp)):
            if k in comb:
                temp[k] = '#'
            else:
                if temp[k] == '?':
                    temp[k] = '.'

        s = "".join(temp)
        p = find_pattern(s)
        if p == pattern:
            arrangement_count += 1

    print(f'{string} / {pattern} - {arrangement_count}')
    total_arrangement_count += arrangement_count

print(f'Total sum of arrangements: {total_arrangement_count}')
