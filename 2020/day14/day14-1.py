#!/usr/bin/python3
# Advent of Code 2020 - Day 14, Part 1
# Benedikt Otto
#
import re

# input_file = '../examples/example_14.txt'
input_file = '../inputs/input_14.txt'

# Parse input into a list of strings.
program = []
with open(input_file) as file:
    for line in file.readlines():
        program.append(line.strip())


def translate(value: int, bit_mask: str) -> int:
    """Applies the bit mask to the decimal value and returns the decimal value of the result."""
    # Get bitwise representation.
    s = str(bin(value))
    s = s[2:]

    # Pad with zeroes to 36 digits.
    s = s.rjust(36, '0')

    # Build list of the resulting binary representation.
    res = ['0'] * 36
    for idx in range(36):
        match bit_mask[idx]:
            case '0':
                res[idx] = '0'
            case '1':
                res[idx] = '1'
            case 'X':
                res[idx] = s[idx]

    # Turn result back into decimal.
    result = ''.join(res)
    return int(result, 2)


# Regexes for parsing the program lines.
re_mask = re.compile(r'^mask\s=\s([10X]{36})$')
re_mem = re.compile(r'^mem\[(\d+)\]\s=\s(\d+)$')

# Simulate the program.
mask = '000000000000000000000000000000000000'
memory = {}  # We only record memories that have been changed.
for line in program:
    if 'mask' in line:
        search = re_mask.search(line)
        mask = search.group(1)
        print(f'Mask change: {mask}')
    else:
        search = re_mem.search(line)
        mem_addr = int(search.group(1))
        mem_val = int(search.group(2))
        x = translate(mem_val, mask)
        print(f'Writing to memory {mem_addr}: {x}')
        memory[mem_addr] = x


# Sum the values in all memory addresses.
sum_values = sum(memory.values())
print(f'Sum of all values left in memory: {sum_values}')
