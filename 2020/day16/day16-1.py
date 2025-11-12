#!/usr/bin/python3
# Advent of Code 2020 - Day 16, Part 1
# Benedikt Otto
#
import re

# input_file = '../examples/example_16.txt'
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


def is_valid(num):
    global valid_ranges
    for field in valid_ranges:
        r1, r2 = valid_ranges[field]
        if r1[0] <= num <= r1[1] or r2[0] <= num <= r2[1]:
            return True
    return False


# Run through all nearby tickets and find the numbers that cannot be valid.
error_rate = 0
for ticket in nearby_tickets:
    for n in ticket:
        if not is_valid(n):
            error_rate += n

print(f'The ticket scanning error rate is {error_rate}.')
