#!/usr/bin/python3
# Advent of Code 2015 - Day 1, Part 2
# Benedikt Otto
#

INPUT_FILE = '../inputs/input_01.txt'

# Parse input into a string.
with open(INPUT_FILE) as file:
    instruction = file.readline()

# Traverse floors as in the instruction.
floor = 0
for num, c in enumerate(instruction):
    match c:
        case '(':
            floor += 1
        case ')':
            floor -= 1
    if floor < 0:
        break

print(f'The position of the first character that causes him to enter the basement is {num + 1}.')
