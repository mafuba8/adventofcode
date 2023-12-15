#!/usr/bin/python3
# Advent of Code 2023 - Day 15, Part 1
# Benedikt Otto

# Open and parse puzzle file.
sequence = []
#with open('example_15.txt') as file:
with open('input_15.txt') as file:
    for line in file:
        # The input is one single line.
        sequence = line.strip().split(',')


def hash_algorithm(string):
    """Calculates the hash value of the given string."""
    val = 0
    for char in string:
        val += ord(char)
        val *= 17
        val = val % 256
    return val


# Calculate the hash of each word and sum it.
total_ha = 0
for word in sequence:
    ha = hash_algorithm(word)
    total_ha += ha

print(f'Sum of all the hash values: {total_ha}')
