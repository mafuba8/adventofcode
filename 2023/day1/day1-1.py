#!/usr/bin/python3
# Advent of Code 2023 - Day 1, Part 1
# Benedikt Otto

# Open puzzle file.
with open('input_1.txt') as file:
    lines = file.readlines()

# Find first and last digit in each line.
# Note: there can be only one digit in a line, which makes first_digit == last_digit.
cal_list = []
for line in lines:
    first_digit = None
    last_digit = None

    for char in line:
        if char.isdigit():
            # Each new digit in the line overwrites last_digit.
            last_digit = char
            if first_digit is None:
                # Only set first_digit on the first appearance.
                first_digit = char

    cal_list.append(int(first_digit + last_digit))


print('Calibration list:', cal_list)
print()

# Sum all the calibration values.
total = 0
for num in cal_list:
    total += num

print('Total:', total)
