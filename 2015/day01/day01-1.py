#!/usr/bin/python3
# Advent of Code 2015 - Day 1, Part 1
# Benedikt Otto
#

INPUT_FILE = '../inputs/input_01.txt'

# Parse input into a string.
with open(INPUT_FILE) as file:
    instruction = file.readline()

# Traverse floors as in the instruction.
floor = 0
for c in instruction:
    match c:
        case '(':
            floor += 1
        case ')':
            floor -= 1

print(f'The instructions take Santa to floor number {floor}.')
