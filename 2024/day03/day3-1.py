#!/usr/bin/python3
# Advent of Code 2024 - Day 3, Part 1
# Benedikt Otto
#
import re

# input_file = '../examples/example_3.txt'
input_file = '../inputs/input_3.txt'

# Parse input into list of instructions.
multiplication_list = []
regex = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')
with open(input_file) as file:
    for line in file.readlines():
        search = regex.findall(line)
        multiplication_list += [(int(x), int(y)) for x,y in search]


# Add up all the results of the valid mul instructions.
total_sum = 0
for mul in multiplication_list:
    total_sum += mul[0] * mul[1]

print(f'Total sum of valid multiplications: {total_sum}')


