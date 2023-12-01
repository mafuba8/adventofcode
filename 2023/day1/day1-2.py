#!/usr/bin/python3
# Advent of Code 2023 - Day 1, Part 2
# Benedikt Otto
import re

# Open puzzle file.
with open('input_1.txt') as file:
    lines = file.readlines()

# Replacing all the spelled-out digits with their digit counterpart.
# We can't just gradually replace the words because of concatenated words that share letters,
# like 'eightwo'. So we use Regex to lazy-search for all keywords at the same time.
regex = re.compile(r'one|two|three|four|five|six|seven|eight|nine')
# Because the puzzle counts 'eightwo' as '82' we preserve the last letter
# This doesn't cause any issued because letters are ignored and no extra digit-words are made that way
rpl_dict = {'one': '1e', 'two': '2o', 'three': '3e', 'four': '4r', 'five': '5e',
            'six': '6x', 'seven': '7n', 'eight': '8t', 'nine': '9e'}

replaced_lines = []
for line in lines:
    s = line
    while True:
        search = regex.search(s)
        # Repeat until no match is found
        if search is not None:
            # Utilizing lazy regex search to find first digit-word
            found = search.group()
            # Only replace the first occurrence of the word
            s = s.replace(found, rpl_dict[found], 1)
        else:
            break
    replaced_lines.append(s)


# Find first and last digit in each line.
# Note: there can be only one digit in a line, which makes first_digit == last_digit.
cal_list = []
for line in replaced_lines:

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
