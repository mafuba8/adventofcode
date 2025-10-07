#!/usr/bin/python3
# Advent of Code 2020 - Day 2, Part 1
# Benedikt Otto
#
import re

# input_file = '../examples/example_2.txt'
input_file = '../inputs/input_2.txt'

# Parse input into a list of dicts.
regex = re.compile(r'^(\d+)-(\d+)\s(.):\s(.*)$')
entry_list = []
with open(input_file) as file:
    for line in file.readlines():
        search = regex.search(line)
        p_min, p_max, p_char, password = search.groups()
        entry = (int(p_min), int(p_max), p_char, password)
        entry_list.append(entry)

# Count valid password entries.
num_valid_passwords = 0
for entry in entry_list:
    p_min, p_max, p_char, password = entry
    count = password.count(p_char)
    if p_min <= count <= p_max:
        num_valid_passwords += 1

print(f'There are {num_valid_passwords} valid passwords in the list.')
