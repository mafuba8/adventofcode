#!/usr/bin/python3
# Advent of Code 2022 - Day 3, Part 1
# Benedikt Otto

# input_file = '../examples/example_3.txt'
input_file = '../inputs/input_3.txt'

# Parse file into lists of rucksacks.
rucksack_list = []
with open(input_file) as file:
    for line in file.readlines():
        rucksack_list.append(line.strip())

def priority(character):
    # Calculate the priority of a given character.
    abc = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return abc.index(character) + 1

total_priority = 0
for rucksack in rucksack_list:
    # Divide into compartments
    mid = len(rucksack) // 2
    c0 = set(rucksack[:mid])
    c1 = set(rucksack[mid:])

    inters = c0.intersection(c1).pop()
    total_priority += priority(inters)
    print(f'Character: {inters}, Priority: {priority(inters)}')

print(f'Sum of all priorities: {total_priority}')
