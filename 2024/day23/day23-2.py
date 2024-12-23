#!/usr/bin/python3
# Advent of Code 2024 - Day 23, Part 2
# Benedikt Otto
#
import re

# input_file = '../examples/example_23.txt'
input_file = '../inputs/input_23.txt'

# Parse input into a list of sets.
connection_list = []
computer_set = set()
regex = re.compile(r'^([a-z]{2})-([a-z]{2})$')
with open(input_file) as file:
    for line in file.readlines():
        search = regex.search(line)
        comp1 = search.group(1)
        comp2 = search.group(2)
        connection_list.append({comp1, comp2})
        computer_set.add(comp1)
        computer_set.add(comp2)


def get_connections_to(comp):
    """Returns a list of all computers that the given comp is connected to."""
    connected_to = set()
    for connection in connection_list:
        if comp in connection:
            connected_to = connected_to.union(connection)
    connected_to.remove(comp)
    return connected_to


# Find all maximal cliques:
max_clique = set()
for comp in computer_set:
    clique = {comp}
    potential_comps = computer_set - clique
    # For each remaining computer check if it is connected to all computers in the clique.
    while len(potential_comps) > 0:
        c = potential_comps.pop()
        if clique.issubset(get_connections_to(c)):
            clique.add(c)

    # Check if we found a new maximum clique
    if len(clique) > len(max_clique):
        max_clique = clique

    print(f'Computer {comp} - max. clique: {clique}')


print()
print(f'Maximal clique (Size {len(max_clique)}): {max_clique}')

# Figure out the password.
l = list(max_clique)
l.sort()
password = ','.join(l)
print(f'Password: {password}')
