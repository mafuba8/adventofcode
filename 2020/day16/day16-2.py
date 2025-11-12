#!/usr/bin/python3
# Advent of Code 2020 - Day 16, Part 2
# Benedikt Otto
#
import re

# input_file = '../examples/example_16b.txt'
input_file = '../inputs/input_16.txt'

# Parse input.
valid_ranges = {}
my_ticket = ()
nearby_tickets = []
section = ''
regex = re.compile(r'^(.*):\s(\d+)-(\d+)\sor\s(\d+)-(\d+)$')
with open(input_file) as file:
    for line in file.readlines():
        if 'your ticket' in line:
            section = 'your_ticket'
            continue
        elif 'nearby tickets' in line:
            section = 'nearby_tickets'
            continue
        elif line == '\n':
            continue

        match section:
            case '':
                search = regex.search(line)
                field_name = search.group(1)
                range1 = (int(search.group(2)), int(search.group(3)))
                range2 = (int(search.group(4)), int(search.group(5)))
                valid_ranges[field_name] = [range1, range2]
            case 'your_ticket':
                my_ticket = tuple(line.strip().split(','))
                my_ticket = [int(s) for s in my_ticket]
            case 'nearby_tickets':
                ticket = tuple(line.strip().split(','))
                ticket = [int(s) for s in ticket]
                nearby_tickets.append(ticket)


def get_valid_fields(num: int, list_of_fields: list[str]) -> list[str]:
    """Returns a list of all the field names in the given list that
    are valid for the given number."""
    valid_fields = []
    for field in list_of_fields:
        for r1, r2 in valid_ranges[field]:
            if r1 <= num <= r2:
                valid_fields.append(field)
    return valid_fields


def is_valid_ticket(tck: list[int]) -> bool:
    """Checks if a given ticket is valid."""
    global valid_ranges
    for num in tck:
        valid_fields = get_valid_fields(num, valid_ranges)
        if len(valid_fields) == 0:
            return False
    return True


# Discard all invalid tickets.
valid_nearby_tickets = [ticket for ticket in nearby_tickets if is_valid_ticket(ticket)]

# Figure out the mappings field -> position.
field_mapping = {}
field_count = len(valid_ranges)
while len(field_mapping) < field_count:
    # Check for each position how many fields are valid for all tickets.
    for pos in range(field_count):
        possible_fields = [field for field in valid_ranges if field not in field_mapping]
        if pos not in field_mapping.values():
            for ticket in valid_nearby_tickets:
                possible_fields = get_valid_fields(ticket[pos], possible_fields)

        # If only one field works for all ticket, this must be the right one.
        if len(possible_fields) == 1:
            field_mapping[possible_fields[0]] = pos

print('The field mapping is:')
print(field_mapping)

# In my_ticket, multiply the values of all fields that start with 'departure'.
result = 1
for field in field_mapping:
    if field.startswith('departure'):
        pos = field_mapping[field]
        result *= my_ticket[pos]

print(f'Result: {result}.')
