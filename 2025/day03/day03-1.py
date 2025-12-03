#!/usr/bin/python3
# Advent of Code 2025 - Day 3, Part 1
# Benedikt Otto
#

# INPUT_FILE = '../examples/example_03.txt'
INPUT_FILE = '../inputs/input_03.txt'

# Parse input into a list of banks.
battery_banks = []
with open(INPUT_FILE) as file:
    for line in file.readlines():
        battery_bank = []
        for char in line.strip():
            battery_bank.append(int(char))
        battery_banks.append(battery_bank)


def max_joltage(bank: list[int]) -> int:
    """Returns the maximum joltage possible by two batteries from a given bank."""
    m = 0
    for k, b1 in enumerate(bank):
        for b2 in bank[k+1:]:
            # Concatenate the two integers.
            num = int(str(b1) + str(b2))
            m = max(num, m)
    return m


# Run through all battery banks and sum up their maximum joltage.
output_joltage = 0
for battery_bank in battery_banks:
    n = max_joltage(battery_bank)
    output_joltage += n

print(f'The total output joltage is: {output_joltage}.')
