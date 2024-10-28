#!/usr/bin/python3
# Advent of Code 2022 - Day 4, Part 1
# Benedikt Otto

# input_file = '../examples/example_4.txt'
input_file = '../inputs/input_4.txt'

# Parse input into list of pairs
pair_list = []
with open(input_file) as file:
    for line in file.readlines():
        p = line.strip().split(',')
        p0 = [int(x) for x in p[0].split('-')]
        p1 = [int(x) for x in p[1].split('-')]
        pair_list.append((p0, p1))

num_fully_contains = 0
for pair in pair_list:
    p0, p1 = pair
    if p0[0] <= p1[0] and p0[1] >= p1[1] or p1[0] <= p0[0] and p1[1] >= p0[1]:
        print(pair)
        num_fully_contains += 1

print(f'Total number of pairs that fully contain each other: {num_fully_contains}')
