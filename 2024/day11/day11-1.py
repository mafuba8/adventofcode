#!/usr/bin/python3
# Advent of Code 2024 - Day 11, Part 1
# Benedikt Otto
#

# input_file = '../examples/example_11.txt'
input_file = '../inputs/input_11.txt'

with open(input_file) as file:
    line = file.readline()
    stone_row = [int(x) for x in line.split()]


def blink(stone_row):
    """Transforms the stone rows as per the given rules."""
    new_stone_row = []
    for stone in stone_row:
        if stone == 0:
            # 0-stones turn to 1-stones.
            new_stone_row.append(1)
        elif len(str(stone)) % 2 == 0:
            # Stones with even number of digits are split into two stones,
            # each inheriting half of the original digits.
            l = len(str(stone)) // 2
            s = str(stone)
            new_stone_row.append(int(s[:l]))
            new_stone_row.append(int(s[l:]))
        else:
            # Otherwise we multiply the stone number by 2024.
            new_stone_row.append(stone * 2024)
    return new_stone_row


# Simulate all blinks.
NUM_BLINKS = 25
print(stone_row)
for k in range(NUM_BLINKS):
    print(f'Blink #{k+1}')
    stone_row = blink(stone_row)

print(f'Number of stones after {NUM_BLINKS} blinks: {len(stone_row)}.')
