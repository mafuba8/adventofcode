#!/usr/bin/python3
# Advent of Code 2021 - Day 2, Part 1
# Benedikt Otto
#

# input_file = '../examples/example_2.txt'
input_file = '../inputs/input_2.txt'

# Parse input into list of tuples (dir, val)
instruction_list = []
with open(input_file) as file:
    for line in file.readlines():
        direction, value = line.split(' ')
        value = int(value)
        instruction_list.append((direction, value))

# Starting position
h_pos = 0
depth = 0
for instr in instruction_list:
    direction, value = instr
    match direction:
        case "forward":
            h_pos += value
        case "up":
            depth -= value
        case "down":
            depth += value

print(f'Final horizontal position: {h_pos}, Final depth: {depth}')
print(f'Solution value: {h_pos * depth}')
