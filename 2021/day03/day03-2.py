#!/usr/bin/python3
# Advent of Code 2021 - Day 3, Part 2
# Benedikt Otto
#

# input_file = '../examples/example_3.txt'
input_file = '../inputs/input_3.txt'

# Parse input into list of strings
diagnostic = []
with open(input_file) as file:
    for line in file.readlines():
        diagnostic.append(line.strip())


def bit_criteria(diag_list, idx = 0):
    """Returns the number of zero-bits and one-bits in the given column."""
    zero_count = 0
    ones_count = 0
    for diag in diag_list:
        if diag[idx] == '0':
            zero_count += 1
        if diag[idx] == '1':
            ones_count += 1

    return zero_count, ones_count


def oxygen_rating(diag_list, idx = 0):
    """ Determines the oxygen generator rating of the given list. """
    # A single list value is the rating.
    if len(diag_list) == 1:
        return diag_list[0]

    # Find the most common bit at column idx.
    most_common_bit = ''
    zero_count, ones_count = bit_criteria(diag_list, idx)
    if zero_count > ones_count:
        most_common_bit = '0'
    elif zero_count < ones_count:
        most_common_bit = '1'
    elif zero_count == ones_count:
        most_common_bit = '1'  # precedence for 1 at parity for oxygen.

    # Filter out values that have the most common value in their column.
    filtered_list = [d for d in diag_list if d[idx] == most_common_bit]

    # Recursively find rating of the filtered list.
    return oxygen_rating(filtered_list, idx + 1)


def co2_rating(diag_list, idx = 0):
    """ Determines the CO2 scrubber rating of the given list. """
    # A single list value is the rating.
    if len(diag_list) == 1:
        return diag_list[0]

    # Find the most common bit at column idx.
    least_common_bit = ''
    zero_count, ones_count = bit_criteria(diag_list, idx)
    if zero_count > ones_count:
        least_common_bit = '1'
    elif zero_count < ones_count:
        least_common_bit = '0'
    elif zero_count == ones_count:
        least_common_bit = '0'  # precedence for 0 at parity for C02.

    # Filter out values that have the most common value in their column.
    filtered_list = [d for d in diag_list if d[idx] == least_common_bit]

    # Recursively find rating of the filtered list.
    return co2_rating(filtered_list, idx + 1)


# Determine the life support rating of the submarine.
oxygen_generator_rating = oxygen_rating(diagnostic)
co2_scrubber_rating = co2_rating(diagnostic)
print(f'Oxygen generator rating: {oxygen_generator_rating} ({int(oxygen_generator_rating, 2)})')
print(f'CO2 scrubber rating: {co2_scrubber_rating} ({int(co2_scrubber_rating, 2)})')
print(f'Life support rating: {int(oxygen_generator_rating, 2) * int(co2_scrubber_rating, 2)}')
