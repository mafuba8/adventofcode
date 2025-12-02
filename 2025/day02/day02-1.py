#!/usr/bin/python3
# Advent of Code 2025 - Day 2, Part 1
# Benedikt Otto
#

# INPUT_FILE = '../examples/example_02.txt'
INPUT_FILE = '../inputs/input_02.txt'

# Parse input into a list of ranges (tuples).
id_ranges = []
with open(INPUT_FILE) as file:
    for word in file.readline().strip().split(','):
        r = map(int, word.split('-'))
        id_ranges.append(tuple(r))


def is_invalid(product_id: int) -> bool:
    """Checks if the given product id consists of a sequence of digits repeated twice."""
    s = str(product_id)
    l = len(s)
    return s[:l // 2] == s[l // 2:]


# Run through all ID ranges and find the invalid ones.
sum_of_invalid_ids = 0
for id_start, id_end in id_ranges:
    for k in range(id_start, id_end + 1):
        if is_invalid(k):
            print(f'{k} is invalid')
            sum_of_invalid_ids += k

print(f'Sum of all invalid IDs: {sum_of_invalid_ids}.')
