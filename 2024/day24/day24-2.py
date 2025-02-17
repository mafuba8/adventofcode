#!/usr/bin/python3
# Advent of Code 2024 - Day 24, Part 2
# Benedikt Otto
#
# This is one of the AoC problems where there is no good way to fully automate the process of finding the solution.
# Finding the solution involves trying out different combinations and deducing the right wire pairs to swap
# via analyzing the error, knowing how a binary Added has to be implemented.
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
        print(f'  {gate}: {values_dict[gate]}')
        return values_dict[gate]

    # Recursively calculate the values of the input gates.
    input_gate1, op, input_gate2 = gate_dict[gate]
    print(f' {input_gate1} {op} {input_gate2} == {gate}')
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


def find_gate(op, inputs):
    """Returns the gate with the given operation and inputs (i1, i2)."""
    i1, i2 = inputs
    g1 = (i1, op, i2)
    g2 = (i2, op, i1)
    l = [g for g in gate_dict if gate_dict[g] == g1 or gate_dict[g] == g2]
    if len(l) > 0:
        return l[0]
    else:
        print(f'One of the inputs {i1} or {i2} is wrong. (Gate: {i1} {op} {i2})')
        return None


# A binary Adder has the following structure:
#  c = carry
#  z00 == x00 XOR y00
#  c00 == x00 AND y00
#
#  u01 == x01 XOR y01
#  v01 == x01 AND y01
#  w01 == u01 AND c00
#  z01 == u01 XOR c00
#  c01 == v01 OR w01

# The first set of inputs are easy to figure out.
z00 = find_gate('XOR', ('x00', 'y00'))
c00 = find_gate('AND', ('x00', 'y00'))
new_dict = {'z00': z00, 'c00': c00}


def swap_outputs(gate1, gate2):
    """Modifies gate_dict and swaps the outputs of the two gates."""
    global gate_dict
    a = gate_dict[gate1]
    b = gate_dict[gate2]
    gate_dict[gate1] = b
    gate_dict[gate2] = a


# These are the final pairs of wires that need to be swapped in order to get the right result.
# Determined after trial-and-error by gradually walking up the levels.
swap_list = [('rpv', 'z11'),
             ('rpb', 'ctg'),
             ('z31', 'dmh'),
             ('z38', 'dvq')]

# Swap wires according to swap_list.
for swap_pair in swap_list:
    swap_outputs(swap_pair[0], swap_pair[1])


# This is the trial-and-error part.
# We gradually increase the level (up to 40) and check if all binary relations still work. If that results in an error,
# it means that there must be a falsely connected wire in this level. We then need to manually figure out what the
# right connection would be.
max_level = 40

# Check if the structure of the Adder is right up until the given level.
for level in range(1, max_level):
    # Obtain the wires on this level.
    name_u = f'u{level:02}'
    name_v = f'v{level:02}'
    name_w = f'w{level:02}'
    name_x = f'x{level:02}'
    name_y = f'y{level:02}'
    name_z = f'z{level:02}'
    name_c = f'c{level:02}'
    name_c_prev = f'c{level - 1:02}'

    # The uxx and vxx names are easy to find, since their operation only depend on x and y.
    print(f'Finding {name_z}:')
    uxx = find_gate('XOR', (name_x, name_y))
    vxx = find_gate('AND', (name_x, name_y))
    new_dict.setdefault(name_u, uxx)
    new_dict.setdefault(name_v, vxx)
    print(f' {name_u} == {uxx}')
    print(f' {name_v} == {vxx}')

    # Figuring out the name of the wxx input.
    wxx = find_gate('AND', (new_dict[name_u], new_dict[name_c_prev]))
    new_dict.setdefault(name_w, wxx)
    print(f' {name_w} == {wxx}')

    # Figuring out the name of the zxx input.
    zxx = find_gate('XOR', (new_dict[name_u], new_dict[name_c_prev]))
    if zxx == name_z:
        new_dict.setdefault(name_z, zxx)
        print(f' {name_z} == {zxx}')
    else:
        print(f'Wrong output at {zxx} (should be {name_z}).')

    cxx = find_gate('OR', (new_dict[name_v], new_dict[name_w]))
    print(f' {name_c} == {cxx}')
    new_dict.setdefault(name_c, cxx)
    print()


# Print solution string.
solution = []
for pair in swap_list:
    solution.append(pair[0])
    solution.append(pair[1])

solution.sort()
print(f'Solution: {",".join(solution)}')
