#!/usr/bin/python3
# Advent of Code 2025 - Day 5, Part 1
# Benedikt Otto
#

# INPUT_FILE = '../examples/example_05.txt'
INPUT_FILE = '../inputs/input_05.txt'

# Parse inputs into lists.
# ingredient range = tuple(int)
fresh_ingredient_ranges = []
available_ingredients = []
with open(INPUT_FILE) as file:
    first_part = True
    for line in file.readlines():
        if line == '\n':
            first_part = False
            continue
        if first_part:
            fresh_from, fresh_to = line.strip().split('-')
            t = (int(fresh_from), int(fresh_to))
            fresh_ingredient_ranges.append(t)
        else:
            available_ingredients.append(int(line.strip()))


# Count all the fresh ingredients.
count_fresh = 0
for ingredient in available_ingredients:
    for r1, r2 in fresh_ingredient_ranges:
        if r1 <= ingredient <= r2:
            count_fresh += 1
            break

print(f'A total of {count_fresh} ingredients are fresh.')
