#!/usr/bin/python3
# Advent of Code 2022 - Day 1, Part 2
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

# List of carried calories for each elf.
elf_calorie_list = [sum(elf) for elf in elf_list]

# Sort list descending to get the top three.
elf_calorie_list.sort(reverse=True)

print(f'Top three calorie values: {elf_calorie_list[:3]}')
print(f'Total sum: {sum(elf_calorie_list[:3])}')
