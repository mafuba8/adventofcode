#!/usr/bin/python3
# Advent of Code 2022 - Day 1, Part 1
# Benedikt Otto

# input_file = '../examples/example_1.txt'
input_file = '../inputs/input_1.txt'

# Parse input into list of elves.
elf_list = []
with open(input_file) as file:
    # Each elf is a list of calorie values.
    elf = []
    for line in file.readlines():
        if line != '\n':
            elf.append(int(line.strip()))
        else:
            elf_list.append(elf)
            elf = []

# Append last elf.
elf_list.append(elf)

# Elf carrying the most calories.
max_elf = []
max_elf_calories = 0
for elf in elf_list:
    if sum(elf) > max_elf_calories:
        max_elf = elf
        max_elf_calories = sum(elf)

print(f'Elf with the most calories: {max_elf}')
print(f'Total carried calories: {max_elf_calories}')
