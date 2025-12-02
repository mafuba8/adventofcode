#!/usr/bin/python3
# Advent of Code 2025 - Day 2, Part 2
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
    """Checks if the given product contains a repeating pattern of any length."""
    product_str = str(product_id)
    # A repeating pattern can at most be half as long as the full string.
    for pattern_length in range(1, len(product_str) // 2 + 1):
        pattern_count = len(product_str) // pattern_length
        pattern = product_str[:pattern_length]

        if product_str == pattern * pattern_count:
            return True
    return False


# Run through all ID ranges and find the invalid ones.
sum_of_invalid_ids = 0
for id_start, id_end in id_ranges:
    for k in range(id_start, id_end + 1):
        if is_invalid(k):
            print(f'{k} is invalid')
            sum_of_invalid_ids += k

print(f'Sum of all invalid IDs: {sum_of_invalid_ids}.')
