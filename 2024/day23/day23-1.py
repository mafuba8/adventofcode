#!/usr/bin/python3
# Advent of Code 2024 - Day 23, Part 1
# Benedikt Otto
#
import re

# input_file = '../examples/example_23.txt'
input_file = '../inputs/input_23.txt'

# Parse input into a list of sets.
connection_list = []
regex = re.compile(r'^([a-z]{2})-([a-z]{2})$')
with open(input_file) as file:
    for line in file.readlines():
        search = regex.search(line)
        comp1 = search.group(1)
        comp2 = search.group(2)
        connection_list.append({comp1, comp2})


def get_connections_to(comp):
    """Returns a list of all computers that the given comp is connected to."""
    connected_to = set()
    for connection in connection_list:
        if comp in connection:
            connected_to = connected_to.union(connection)
    connected_to.remove(comp)
    return connected_to


# Find all computer trios that are all connected to each other.
trio_list = []
for connection in connection_list:
    comp1, comp2 = tuple(connection)
    print(f'Connection: {comp1}-{comp2}')

    # Find computers that both comp1 and comp2 are connected to.
    comp1_connections = get_connections_to(comp1)
    comp2_connections = get_connections_to(comp2)
    intersection = comp1_connections.intersection(comp2_connections)

    if len(intersection) > 0:
        for comp3 in intersection:
            print(f' Trio found: {comp1},{comp2},{comp3}')
            trio = [comp1, comp2, comp3]
            trio.sort()
            if trio not in trio_list:
                trio_list.append(trio)


print(f'Total number of computer trios: {len(trio_list)}')

# Find the number of trios that contain a computer that starts with 't'.
trios_with_t = 0
for trio in trio_list:
    comp1, comp2, comp3 = trio
    if comp1[0] == 't' or comp2[0] == 't' or comp3[0] == 't':
        trios_with_t += 1

print(f'Number of computer trios that contain at least one computer starting with t: {trios_with_t}')
