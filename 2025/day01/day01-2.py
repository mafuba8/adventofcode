#!/usr/bin/python3
# Advent of Code 2025 - Day 1, Part 2
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
    rot, num = instruction
    pos = old_pos
    zero_hits = 0
    for _ in range(num):
        match rot:
            case 'R':
                pos = (pos + 1) % 100
            case 'L':
                pos = (pos - 1) % 100
        if pos == 0:
            zero_hits += 1
    return pos, zero_hits


# Rotate the dial according to the instructions and count the number of times it hits zero.
password = 0
dial_position = 50
for ins in instructions:
    dial_position, zero_count = rotate_dial(dial_position, ins)
    print(f'{ins} -> {dial_position}, ({zero_count})')
    password += zero_count

print(f'The password is: {password}')
