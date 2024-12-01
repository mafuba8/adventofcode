#!/usr/bin/python3
# Advent of Code 2024 - Day 1, Part 2
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


# Calculate the similarity score.
total_similarity_score = 0
for num in left_list:
    # Count number of times num appears in right_list.
    count = 0
    for elem in right_list:
        if num == elem:
            count += 1
    total_similarity_score += num * count

print(f'Total similarity score:: {total_similarity_score}')
