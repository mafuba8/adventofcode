#!/usr/bin/python3
# Advent of Code 2025 - Day 3, Part 2
# Benedikt Otto
#
import functools

# INPUT_FILE = '../examples/example_03.txt'
INPUT_FILE = '../inputs/input_03.txt'

# Parse input into a list of banks.
battery_banks = []
with open(INPUT_FILE) as file:
    for line in file.readlines():
        battery_bank = ''
        for char in line.strip():
            battery_bank += char
        battery_banks.append(battery_bank)


@functools.cache
def max_joltage(bank: str, length: int) -> int:
    # Recursion end.
    if length == 1:
        return max(int(c) for c in bank)
    if len(bank) <= length:
        return int(bank)

    # Run through all single digits, find the maximum of the remainder via recursion
    # and check if the concatenated number is a new maximum.
    m = 0
    for k in range(len(bank) - length + 1):
        b1 = bank[k]
        max_remainder = max_joltage(bank[k + 1:], length - 1)
        num = int(str(b1) + str(max_remainder))
        m = max(num, m)
    return m


# Run through all battery banks and sum up their maximum joltage.
output_joltage = 0
for battery_bank in battery_banks:
    n = max_joltage(battery_bank, 12)
    output_joltage += n

print(f'The total output joltage is: {output_joltage}.')
