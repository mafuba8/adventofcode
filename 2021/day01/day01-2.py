#!/usr/bin/python3
# Advent of Code 2021 - Day 1, Part 2
# Benedikt Otto
#

# input_file = '../examples/example_1.txt'
input_file = '../inputs/input_1.txt'

# Parse input into list of integers.
depth_list = []
with open(input_file) as file:
    for line in file.readlines():
        depth_list.append(int(line))


# Length 3 sliding windows.
count = 0
prev = None
for idx in range(len(depth_list) - 2):
    s = sum(depth_list[idx:idx+3])
    if prev is not None:
        if s > prev:
            count += 1
    prev = s

print(f'Number of sliding-window sums that are larget than the previous one: {count}')
