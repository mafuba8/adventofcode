#!/usr/bin/python3
# Advent of Code 2024 - Day 3, Part 2
# Benedikt Otto
#
import re

# input_file = '../examples/example_3b.txt'
input_file = '../inputs/input_3.txt'

# Parse input into list of instruction rows.
re_instruction = re.compile(r'mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)')
instruction_row_list = []
with open(input_file) as file:
    for line in file.readlines():
        search = re_instruction.findall(line)
        instruction_row_list.append(search)


# Run through all instructions, collecting all mul instructions within enabled areas.
re_multiplication = re.compile(r'mul\((\d+),(\d+)\)')
mul_list = []
enable_instruction = True
for instruction_row in instruction_row_list:
    instruction_list = instruction_row
    for instruction in instruction_list:
        if instruction[:3] == 'mul':
            if enable_instruction:
                s = re_multiplication.search(instruction)
                x, y = s.group(1), s.group(2)
                mul_list.append((int(x), int(y)))
        elif instruction[:3] == 'do(':
            enable_instruction = True
        elif instruction[:3] == 'don':
            enable_instruction = False


# Add up all the results of the enabled mul instructions.
total_sum = 0
for mul in mul_list:
    total_sum += mul[0] * mul[1]

print(f'Total sum of valid enabled multiplications: {total_sum}')


