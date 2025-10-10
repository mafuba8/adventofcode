#!/usr/bin/python3
# Advent of Code 2020 - Day 9, Part 1
# Benedikt Otto
#

# input_file = '../examples/example_9.txt'
input_file = '../inputs/input_9.txt'

# Parse input into a list of numbers.
data = []
with open(input_file) as file:
    for line in file.readlines():
        data.append(int(line))


# Size of the sliding window.
# WINDOW_SIZE = 5   # For example data.
WINDOW_SIZE = 25  # For real input.

def is_valid(num, prev_num_list):
    """Checks if a given number is valid in the sense that it can be written as the sum of
    two distinct numbers in the given list."""
    for a in prev_num_list:
        for b in prev_num_list:
            if a != b and a + b == num:
                return True
    return False


# Sliding window iteration.
invalid_number = 0
for k in range(WINDOW_SIZE, len(data)):
    number = data[k]
    prev_window = data[k-WINDOW_SIZE:k]

    if not is_valid(number, prev_window):
        invalid_number = number
        break

print(f'First number without the sum property: {invalid_number}')
