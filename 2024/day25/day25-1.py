#!/usr/bin/python3
# Advent of Code 2024 - Day 25, Part 1
# Benedikt Otto
#

# input_file = '../examples/example_25.txt'
input_file = '../inputs/input_25.txt'

# Parse input into lists of dicts.
schematics_list = []
with open(input_file) as file:
    schematic = {}
    row_num = 0
    for row in file.readlines():
        if row == '\n':
            schematics_list.append(schematic)
            schematic = {}
            row_num = 0
            continue
        else:
            for col_num, char in enumerate(row.strip()):
                schematic.setdefault((row_num, col_num), char)
        row_num += 1

    # Append last schematic.
    schematics_list.append(schematic)


schematic_width = 5
schematic_height = 7

keys_list = []
locks_list = []
# Convert schematics into keys and locks.
for schematic in schematics_list:
    # Obtain pin heights.
    pin_heights = []
    for col_num in range(schematic_width):
        pin_height = 0
        for row_num in range(1,6):
            # We assume that there are no 'holes' in a column.
            if schematic[(row_num, col_num)] == '#':
                pin_height += 1
        pin_heights.append(pin_height)

    # Check whether it's a key or a lock:
    upper_row = [schematic[xy] for xy in schematic if xy[0] == 0]
    lower_row = [schematic[xy] for xy in schematic if xy[0] == 7 - 1]
    if ''.join(upper_row) == '#####':
        # Lock
        locks_list.append(pin_heights)

    if ''.join(lower_row) == '#####':
        # Key
        keys_list.append(pin_heights)


# Find the lock/key pairs that fit together.
unique_lock_key_pairs = 0
for lock in locks_list:
    print(f'Lock: {lock}')

    for key in keys_list:
        print(f' - Key: {key}')
        # Check if all columns of the key/lock pair fit.
        if all([lock[col_num] + key[col_num] <= 5 for col_num in range(schematic_width)]):
            print(f'    Key fits.')
            unique_lock_key_pairs += 1

print(f'Number of unique lock/key pairs that fit together: {unique_lock_key_pairs}.')
