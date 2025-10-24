#!/usr/bin/python3
# Advent of Code 2020 - Day 14, Part 2
# Benedikt Otto
#
import re

# input_file = '../examples/example_14b.txt'
input_file = '../inputs/input_14.txt'

# Parse input into a list of strings.
program = []
with open(input_file) as file:
    for line in file.readlines():
        program.append(line.strip())


def int_to_36bit(num: int) -> str:
    """Translates an integer into the string of the 36-bit representation."""
    result = bin(num)
    result = result[2:]
    result = result.rjust(36, '0')
    return result


def apply_mask(bits: str, bit_mask: str) -> str:
    """Applies the bitmask to the bit string, returning another bit string which might
    include floating bits 'X'."""
    result = ['0'] * 36
    for i in range(36):
        match bit_mask[i]:
            case '0':
                result[i] = bits[i]
            case '1':
                result[i] = '1'
            case 'X':
                result[i] = 'X'
    return ''.join(result)


def floating_combinations(bits: str) -> list[str]:
    """Returns a list of all bit strings that result from the combinations of floating bits."""
    if len(bits) == 0:
        return ['']
    else:
        rest = floating_combinations(bits[1:])
        match bits[0]:
            case '0':
                return ['0' + r for r in rest]
            case '1':
                return ['1' + r for r in rest]
            case 'X':
                return ['0' + r for r in rest] + ['1' + r for r in rest]


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

        mem_addr_bits = int_to_36bit(mem_addr)
        mem_addr_floating = apply_mask(mem_addr_bits, mask)
        for addr_bits in floating_combinations(mem_addr_floating):
            addr = int(addr_bits, 2)
            memory[addr] = mem_val


# Sum the values in all memory addresses.
sum_values = sum(memory.values())
print(f'Sum of all values left in memory: {sum_values}')
