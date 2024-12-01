#!/usr/bin/python3
# Advent of Code 2024 - Day 1, Part 1
# Benedikt Otto
#
import re

# input_file = '../examples/example_1.txt'
input_file = '../inputs/input_1.txt'

# Parse input into two lists.
left_list = []
right_list = []
regex = re.compile(r'^(\d+)\s+(\d+)$')
with open(input_file) as file:
    for line in file.readlines():
        search = regex.search(line)
        l = int(search.group(1))
        r = int(search.group(2))
        left_list.append(l)
        right_list.append(r)

# Sort lists and compare them element-by-element.
left_list.sort()
right_list.sort()
dist = 0
for i in range(len(left_list)):
    dist += abs(left_list[i] - right_list[i])

print(f'Total distance between the left and right list: {dist}')
