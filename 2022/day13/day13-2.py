#!/usr/bin/python3
# Advent of Code 2022 - Day 13, Part 2
# Benedikt Otto
from copy import deepcopy

# input_file = '../examples/example_13.txt'
input_file = '../inputs/input_13.txt'

# Parse input into list of packets.
packet_list = []
with open(input_file) as file:
    for row in file.readlines():
        if row == '\n':
            continue
        # I am so mad this actually works.
        a = []
        exec('a = ' + row)
        packet_list.append(a)


def compare(left_packet, right_packet):
    """Compares the two packets as defined in the exercise. Returns True, if
    they are in the right order, False if they are not, and None if it is undecided."""
    # Check for the case that both sides are integers.
    if isinstance(left_packet, int) and isinstance(right_packet, int):
        if left_packet < right_packet:
            return True
        elif left_packet > right_packet:
            return False
        else:
            return None

    # At least one side is a list. Then convert the other side to a list too.
    if isinstance(left_packet, int):
        left_packet = [left_packet]
    elif isinstance(right_packet, int):
        right_packet = [right_packet]

    # Now both sides are lists.
    if len(left_packet) > 0 and len(right_packet) == 0:
        return False
    elif len(left_packet) == 0 and len(right_packet) > 0:
        return True
    elif len(left_packet) == 0 == len(right_packet):
        return None

    # Now both sides are nonempty lists.
    c = compare(left_packet[0], right_packet[0])
    if c is None:
        return compare(left_packet[1:], right_packet[1:])
    return c


# Append the two divider packets.
packet_list.append([[2]])
packet_list.append([[6]])

# Sort packet_list using Bubblesort.
for n in range(len(packet_list), 0, -1):
    for i in range(n - 1):
        if not compare(packet_list[i], packet_list[i+1]):
            # Swap packets.
            packet_list[i], packet_list[i+1] = packet_list[i+1], packet_list[i]

# Find decoder keys.
i1 = packet_list.index([[2]])
i2 = packet_list.index([[6]])
print(f'Indices: {i1 + 1} (for [[2]]) and {i2 + 1} (for [[6]]).')
print(f'Decoder key: {(i1 + 1) * (i2 + 1)}.')
