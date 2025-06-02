#!/usr/bin/python3
# Advent of Code 2022 - Day 25, Part 1
# Benedikt Otto
#

# input_file = '../examples/example_25.txt'
input_file = '../inputs/input_25.txt'

# Parse input into list of strings.
snafu_list = []
with open(input_file) as file:
    for line in file.readlines():
        snafu_list.append(line.strip())


def snafu_to_int(snafu):
    """Converts a given snafu-number into an integer."""
    l = list(snafu)
    l.reverse()

    num = 0
    for idx, c in enumerate(l):
        m = 0
        match c:
            case '=':
                m = -2
            case '-':
                m = -1
            case '0':
                m = 0
            case '1':
                m = 1
            case '2':
                m = 2
        num += m * (5 ** idx)
    return num


def int_to_snafu(num, needed_digits=0):
    """Converts a given integer into its snafu-form."""
    # Single digit numbers:
    match num:
        case -2:
            return '='
        case -1:
            return '-'
        case 0:
            return '0'
        case 1:
            return '1'
        case 2:
            return '2'

    # Find the number of digits num will need.
    num_digits = 0
    x = 0
    while not -x < num < x:
        x += 2 * 5 ** num_digits
        num_digits += 1

    # Pad the number with zeroes if the wanted number of digits is higher than necessary.
    prefix = ''
    if needed_digits > num_digits:
        prefix = '0' * (needed_digits - num_digits)

    # Thresholds for the different digits.
    min_1 = snafu_to_int('1' + '=' * (num_digits - 1))
    max_1 = snafu_to_int('1' + '2' * (num_digits - 1))
    min_2 = snafu_to_int('2' + '=' * (num_digits - 1))
    max_2 = snafu_to_int('2' + '2' * (num_digits - 1))

    # Positive numbers.
    if min_1 <= num <= max_1:
        # '1=====' <= num <= '122222'
        r = num - 5**(num_digits - 1)
        return prefix + '1' + int_to_snafu(r, num_digits - 1)
    elif min_2 <= num <= max_2:
        # '2=====' <= num <= '222222'
        r = num - 2 * 5**(num_digits - 1)
        return prefix + '2' + int_to_snafu(r, num_digits - 1)

    # Negative numbers.
    if -max_1 <= num <= -min_1:
        # '-=====' <= num <= '-22222'
        r = num + 5**(num_digits - 1)
        return prefix + '-' + int_to_snafu(r, num_digits - 1)
    elif -max_2 <= num <= -min_2:
        # '======' <= num <= '=22222'
        r = num + 2 * 5**(num_digits - 1)
        return prefix + '=' + int_to_snafu(r, num_digits - 1)
    return ''


# Convert and sum up all snafu numbers.
total_sum = 0
for snafu in snafu_list:
    n = snafu_to_int(snafu)
    total_sum += n
    print(f' {snafu}: {n}')

print(f'Sum of all numbers: {total_sum}')
print(f'in SNAFU form: "{int_to_snafu(total_sum)}"')
