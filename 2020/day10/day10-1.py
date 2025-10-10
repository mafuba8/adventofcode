#!/usr/bin/python3
# Advent of Code 2020 - Day 10, Part 1
# Benedikt Otto
#

# input_file = '../examples/example_10a.txt'
# input_file = '../examples/example_10b.txt'
input_file = '../inputs/input_10.txt'

# Parse input into a list of numbers.
adapter_list = []
with open(input_file) as file:
    for line in file.readlines():
        adapter_list.append(int(line))

print(adapter_list)

# Add the built-in adapter.
built_in_adapter = max(adapter_list) + 3
adapter_list.append(built_in_adapter)

# Run through adapters and add the adapter with the smallest step, increasing the joltage.
joltage = 0
difference_count = {1: 0, 2: 0, 3: 0}
while True:
    if joltage + 1 in adapter_list:
        print(f'Taking adapter {joltage + 1} (+1).')
        joltage = joltage + 1
        difference_count[1] += 1
    elif joltage + 2 in adapter_list:
        print(f'Taking adapter {joltage + 2} (+2).')
        joltage = joltage + 2
        difference_count[2] += 1
    elif joltage + 3 in adapter_list:
        print(f'Taking adapter {joltage + 3} (+3).')
        joltage = joltage + 3
        difference_count[3] += 1
    else:
        print(f'No adapter found that would fit another joltage step.')
        break

print()
print(f'1-steps: {difference_count[1]}, 2-steps: {difference_count[2]}, 3-steps: {difference_count[3]}')
print(f'Result: {difference_count[1] * difference_count[3]}')
