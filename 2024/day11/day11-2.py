#!/usr/bin/python3
# Advent of Code 2024 - Day 11, Part 2
# Benedikt Otto
#
# The first real scaling problem this year. Two important things to note here are:
#  - The stones are independent of each other. We can compute results about stone rows by
#    combining the results of the computation of each stone.
#  - A lot of the occurring stone numbers are repeating, which enables us to use dynamic processing.
#
import functools

# input_file = '../examples/example_11.txt'
input_file = '../inputs/input_11.txt'

# Parse input into list of numbers.
with open(input_file) as file:
    line = file.readline()
    stone_row = [int(x) for x in line.split()]


def blink(stone):
    """Transforms the given stone as per the given rules, returning the list of stones
    that replaced the original stone.
    """
    replaced_stones = []
    if stone == 0:
        # 0-stones turn to 1-stones.
        replaced_stones.append(1)
    elif len(str(stone)) % 2 == 0:
        # Stones with even number of digits split into two.
        l = len(str(stone)) // 2
        s = str(stone)
        replaced_stones.append(int(s[:l]))
        replaced_stones.append(int(s[l:]))
    else:
        # Otherwise we multiply the stone number by 2024.
        replaced_stones.append(stone * 2024)
    return replaced_stones


@functools.cache
def num_stones(stone, num_blinks = 1):
    """Counts the number of stones that the given stone splits into
    after num_blinks iterations. Since a lot of the values will be repeated,
    caching the results will drastically speed up the computation.
    """
    count = 0
    if num_blinks == 1:
        count = len(blink(stone))
    if num_blinks >= 2:
        for st in blink(stone):
            count += num_stones(st, num_blinks - 1)
    return count


# For each stone, count the number of splitting results and add them up.
NUM_BLINKS = 75
total_number_of_stones = 0
for stone in stone_row:
    total_number_of_stones += num_stones(stone, NUM_BLINKS)

print(f'Number of stones after {NUM_BLINKS} blinks: {total_number_of_stones}.')
