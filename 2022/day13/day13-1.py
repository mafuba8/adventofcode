#!/usr/bin/python3
# Advent of Code 2022 - Day 13, Part 1
# Benedikt Otto

# input_file = '../examples/example_13.txt'
input_file = '../inputs/input_13.txt'

# Parse input into list of pairs pf packets.
packet_pairs_list = []
with open(input_file) as file:
    first_of_pair = True
    for row in file.readlines():
        if row == '\n':
            continue
        if first_of_pair:
            a = []
            # I am so mad that this actually works.
            exec('a = ' + row)
            first_of_pair = False
        else:
            b = []
            exec('b = ' + row)
            packet_pairs_list.append((a, b))
            first_of_pair = True


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


# Run through packet pairs and compare them.
index_sum = 0
for index, packet_pair in enumerate(packet_pairs_list):
    left, right = packet_pair
    if compare(left, right):
        print(index + 1)
        index_sum += index + 1

print(f'Sum of indexes of pairs in the right order: {index_sum}')
