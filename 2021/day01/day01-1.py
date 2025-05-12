#!/usr/bin/python3
# Advent of Code 2021 - Day 1, Part 1
# Benedikt Otto
#

# input_file = '../examples/example_1.txt'
input_file = '../inputs/input_1.txt'

# Parse input into list of integers.
depth_list = []
with open(input_file) as file:
    for line in file.readlines():
        depth_list.append(int(line))


# Count the measurements that are larger than the previous one
count = 0
prev = depth_list[0]
for k in depth_list[1:]:
    if k > prev:
        count += 1
    prev = k

print(f'Number of measurements that are larger than the previous one: {count}')
