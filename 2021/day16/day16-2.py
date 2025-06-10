#!/usr/bin/python3
# Advent of Code 2021 - Day 16, Part 2
# Benedikt Otto
#

# input_file = '../examples/example_16b.txt'
input_file = '../inputs/input_16.txt'

# Our input is a single value (single line), but we have merged all the examples into one file.
hex_string_list = []
with open(input_file) as file:
    for line in file.readlines():
        hex_string_list.append(line.strip())


class Packet:
    def __init__(self, packet_version=0, packet_type=0):
        self.packet_version = packet_version
        self.packet_type = packet_type

    def get_total_version(self):
        return self.packet_version

    def evaluate(self):
        return None


class Literal(Packet):
    def __init__(self, packet_version, packet_type=4, literal_value=0):
        super().__init__(packet_version, packet_type)
        self.literal_value = literal_value

    def evaluate(self):
        return self.literal_value


class Operator(Packet):
    def __init__(self, packet_version=0, packet_type=0, sub_packet_list=[]):
        super().__init__(packet_version, packet_type)
        self.sub_packet_list = sub_packet_list

    def get_total_version(self):
        total_version = self.packet_version
        for sub in self.sub_packet_list:
            total_version += sub.get_total_version()
        return total_version

    def evaluate(self):
        match self.packet_type:
            case 0:
                return sum([sub.evaluate() for sub in self.sub_packet_list])
            case 1:
                x = 1
                for sub in self.sub_packet_list:
                    x *= sub.evaluate()
                return x
            case 2:
                return min([sub.evaluate() for sub in self.sub_packet_list])
            case 3:
                return max([sub.evaluate() for sub in self.sub_packet_list])
            case 5:
                sub1, sub2 = self.sub_packet_list
                if sub1.evaluate() > sub2.evaluate():
                    return 1
                else:
                    return 0
            case 6:
                sub1, sub2 = self.sub_packet_list
                if sub1.evaluate() < sub2.evaluate():
                    return 1
                else:
                    return 0
            case 7:
                sub1, sub2 = self.sub_packet_list
                if sub1.evaluate() == sub2.evaluate():
                    return 1
                else:
                    return 0
        return None


def parse_packet_from(offset, bin_rep):
    """Starts parsing a packet from the given index in the bit stream. Assumes that a new packet starts there.
    Returns a nested display of the packet and the total number of bits parsed."""
    ver = int(bin_rep[offset:offset + 3], 2)
    typ = int(bin_rep[offset + 3:offset + 6], 2)
    if typ == 4:  # Literal packet.
        literal_value = ''
        # Read blocks of 5 bytes until we get a block that starts with a 0.
        is_last_group = False
        idx = offset + 6
        while not is_last_group:
            group = bin_rep[idx:idx + 5]
            if group[0] == '0':
                is_last_group = True
            literal_value += group[1:]
            idx += 5

        return Literal(ver, typ, int(literal_value, 2)), idx - offset

    else:  # Operator packet.
        sub_packets = []
        length_type = bin_rep[offset + 6]
        total_bits_parsed = 7
        if length_type == '0':
            # next 15 bits represent the total length of the sub-packets in bits.
            sub_packet_length = int(bin_rep[offset + 7:offset + 7 + 15], 2)
            total_bits_parsed += 15

            # Read bits until the total_bits_parsed is zero.
            idx = offset + 7 + 15
            while sub_packet_length > 0:
                sub, sub_bits_parsed = parse_packet_from(idx, bin_rep)
                idx = idx + sub_bits_parsed
                total_bits_parsed += sub_bits_parsed
                sub_packets.append(sub)
                sub_packet_length -= sub_bits_parsed

        elif length_type == '1':
            # next 11 bits represent the number of sub-packets.
            sub_packet_count = int(bin_rep[offset + 7:offset + 7 + 11], 2)
            total_bits_parsed += 11

            # Read sub-packets until the sub_packet_count is zero.
            idx = offset + 7 + 11
            while sub_packet_count > 0:
                sub, sub_bits_parsed = parse_packet_from(idx, bin_rep)
                idx = idx + sub_bits_parsed
                total_bits_parsed += sub_bits_parsed
                sub_packets.append(sub)
                sub_packet_count -= 1

        return Operator(ver, typ, sub_packets), total_bits_parsed


def parse_hex(hex_string):
    """Translates the given hexadecimal string into a nested display of the packets."""
    # Translate into bit string.
    translator = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101',
                  '6': '0110', '7': '0111', '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
                  'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}
    bin_rep = ''
    for c in hex_string:
        bin_rep += translator[c]
    packets, _ = parse_packet_from(0, bin_rep)
    return packets


# Parse each hexadecimal string.
for hex_string in hex_string_list:
    pack = parse_hex(hex_string)
    print(hex_string)
    print(f' Version sum: {pack.get_total_version()}')
    print(f' Packet value: {pack.evaluate()}')
