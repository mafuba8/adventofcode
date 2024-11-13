#!/usr/bin/python3
# Advent of Code 2022 - Day 13, Part 1
# Benedikt Otto
from copy import deepcopy

input_file = '../examples/example_13.txt'
# input_file = '../inputs/input_13.txt'

# Parse input into list of pairs pf packages.
packet_pairs_list = []
with open(input_file) as file:
    first_of_pair = True
    for row in file.readlines():
        # I am so mad that this actually works.
        if row == '\n':
            continue
        if first_of_pair:
            a = []
            exec('a = ' + row)
            first_of_pair = False
        else:
            b = []
            exec('b = ' + row)
            packet_pairs_list.append((a, b))
            first_of_pair = True


def compare(left_packet, right_packet):
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

    # Now both sides are lists. Iterate through them and compare their elements.
    while len(left_packet) > 0 and len(right_packet) > 0:
        c = compare(left_packet[0], right_packet[0])
        if c is None:
            del left_packet[0]
            del right_packet[0]
            continue
        else:
            return c

    # One of the lists ran out of elements.
    if len(left_packet) == 0 and len(right_packet) > 0:
        return True
    elif len(left_packet) > 0 and len(right_packet) == 0:
        return False
    else:
        return None


# Run through packet pairs and compare them.
index_sum = 0
for index, packet_pair in enumerate(packet_pairs_list):
    left, right = packet_pair
    # Not pretty, having to copy the lists so that they don't get mangled.
    c = compare(deepcopy(left), deepcopy(right))
    if c:
        print(index + 1)
        index_sum += index + 1

print(f'Sum of indexes of pairs in the right order: {index_sum}')
