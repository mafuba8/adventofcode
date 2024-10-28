#!/usr/bin/python3
# Advent of Code 2022 - Day 4, Part 2
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

num_overlaps = 0
for pair in pair_list:
    p0, p1 = pair
    # Find non-overlapping pairs and negate it.
    if not (p0[1] < p1[0] or p1[1] < p0[0]):
        print(pair)
        num_overlaps += 1

print(f'Total number of pairs that overlap: {num_overlaps}')
