#!/usr/bin/python3
# Advent of Code 2025 - Day 1, Part 1
# Benedikt Otto
#

# INPUT_FILE = '../examples/example_01.txt'
INPUT_FILE = '../inputs/input_01.txt'

# Parse input into a list of instructions.
instructions = []
with open(INPUT_FILE) as file:
    for line in file.readlines():
        s = line.strip()
        r = s[0]
        n = int(s[1:])
        instructions.append((r, n))


def rotate_dial(old_pos, instruction):
    new_pos = old_pos
    rot, num = instruction
    match rot:
        case 'R':
            new_pos = (new_pos + num) % 100
        case 'L':
            new_pos = (new_pos - num) % 100
    return new_pos


# Rotate the dial according to the instructions and count the number of times it hits zero.
password = 0
dial_position = 50
for ins in instructions:
    dial_position = rotate_dial(dial_position, ins)
    print(f'{ins} -> {dial_position}')
    if dial_position == 0:
        password += 1

print(f'The password is: {password}')
