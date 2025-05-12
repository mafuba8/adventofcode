#!/usr/bin/python3
# Advent of Code 2021 - Day 3, Part 1
# Benedikt Otto
#

# input_file = '../examples/example_3.txt'
input_file = '../inputs/input_3.txt'

# Parse input into list of strings
diagnostic = []
with open(input_file) as file:
    for line in file.readlines():
        diagnostic.append(line.strip())


# Count the number of 0 and 1 bits in each column.
length = len(diagnostic[0])
count_ones = [0 for k in range(length)]
count_zeros = [0 for k in range(length)]
for line in diagnostic:
    for num, c in enumerate(line):
        if c == '0':
            count_zeros[num] += 1
        if c == '1':
            count_ones[num] += 1


# Determine gamma and epsilon rates.
gamma_word = ''
epsilon_word = ''
for k in range(length):
    if count_zeros[k] > count_ones[k]:
        gamma_word += '0'
        epsilon_word += '1'
    else:
        gamma_word += '1'
        epsilon_word += '0'


print(f'Gamma Rate: {gamma_word} ~ {int(gamma_word, 2)}')
print(f'Epsilon Rate: {epsilon_word} ~ {int(epsilon_word, 2)}')
print(f'Power consumption: {int(gamma_word, 2) * int(epsilon_word, 2)}')
