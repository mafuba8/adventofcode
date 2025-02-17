#!/usr/bin/python3
# Advent of Code 2024 - Day 24, Part 1
# Benedikt Otto
#
import re

# input_file = '../examples/example_24.txt'
input_file = '../inputs/input_24.txt'

# Since each wire is connected to at most one output, we name the gates according to their output wires.
# Parse input into dictionaries:
#  values_dict = dict(key=gate, val=int)
#  gate_dict   = dict(key=gate, val=(input_gate1, operation, input_gate2))
# e.g. gate_dict['z00'] == ('x00', 'AND', 'y00')
values_dict = {}
gate_dict = {}
regex_values = re.compile(r'^(.{3}):\s([01])$')
regex_and = re.compile(r'^(.{3})\sAND\s(.{3})\s->\s(.{3})$')
regex_or = re.compile(r'^(.{3})\sOR\s(.{3})\s->\s(.{3})$')
regex_xor = re.compile(r'^(.{3})\sXOR\s(.{3})\s->\s(.{3})$')
with open(input_file) as file:
    for line in file.readlines():
        if 'AND' in line:
            search = regex_and.search(line)
            output = search.group(3)
            gate = (search.group(1), 'AND', search.group(2))
            gate_dict.setdefault(output, gate)
        elif 'XOR' in line:
            search = regex_xor.search(line)
            output = search.group(3)
            gate = (search.group(1), 'XOR', search.group(2))
            gate_dict.setdefault(output, gate)
        elif 'OR' in line:
            search = regex_or.search(line)
            output = search.group(3)
            gate = (search.group(1), 'OR', search.group(2))
            gate_dict.setdefault(output, gate)
        elif line == '\n':
            continue
        else:
            search = regex_values.search(line)
            gate = search.group(1)
            value = int(search.group(2))
            values_dict.setdefault(gate, value)


def calculate_value(gate):
    """Returns the output value of the given gate."""
    if gate in values_dict:
        return values_dict[gate]

    # Recursively calculate the values of the input gates.
    input_gate1, op, input_gate2 = gate_dict[gate]
    input1 = calculate_value(input_gate1)
    input2 = calculate_value(input_gate2)
    match op:
        case 'AND':
            out = input1 & input2
            values_dict.setdefault(gate, out)
            return out
        case 'XOR':
            out = input1 ^ input2
            values_dict.setdefault(gate, out)
            return out
        case 'OR':
            out = input1 | input2
            values_dict.setdefault(gate, out)
            return out


# Outputs are all gates that start with 'z'.
output_gates = [g for g in gate_dict if g[0] == 'z']
output_gates.sort(reverse=True)

# Find the binary representation of the output number.
output_bin_number = ''
for gate in output_gates:
    output_bin_number += str(calculate_value(gate))
    print(f'Gate: {gate} - Value: {calculate_value(gate)}')

print(f'Output binary number: {output_bin_number}')
print(f'Decimal: {int(output_bin_number, 2)}')
