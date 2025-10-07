#!/usr/bin/python3
# Advent of Code 2020 - Day 2, Part 2
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
        p_first, p_second, p_char, password = search.groups()
        entry = (int(p_first), int(p_second), p_char, password)
        entry_list.append(entry)

num_valid_passwords = 0
for entry in entry_list:
    p_first, p_second, p_char, password = entry
    # XOR of both include-statements.
    if (password[p_first-1] == p_char) ^ (password[p_second-1] == p_char):
        num_valid_passwords += 1
        print(password)

print(f'There are {num_valid_passwords} valid passwords in the list.')
