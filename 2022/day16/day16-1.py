#!/usr/bin/python3
# Advent of Code 2022 - Day 16, Part 1
# Benedikt Otto
import functools
import re

# input_file = '../examples/example_16.txt'
input_file = '../inputs/input_16.txt'

# Start node and total available time.
START_NODE = 'AA'
TOTAL_TIME = 30

# Parse input into graph of nodes and dict of flow values.
graph = {}
flow = {}
regex = re.compile(r'^Valve\s([A-Z]{2})\s.*rate=(\d+);.*valves?\s(.*)$')
with open(input_file) as file:
    for line in file.readlines():
        search = regex.search(line)
        node_name = search.group(1)
        flow_rate = int(search.group(2))
        neighbors = search.group(3).split(', ')
        graph.setdefault(node_name, neighbors)
        flow.setdefault(node_name, flow_rate)


@functools.cache
def max_pressure_release(node, remaining_time, valves_opened):
    """
    Returns the max. pressure release possible by starting at <node>, when we have
    <remaining_time> minutes remaining and the valves in the tuple <valves_opened>
    have already been opened.
    """
    # Recursion ends at 0, 1 or 2 minutes remaining.
    if remaining_time in [0, 1]:
        return 0  # Can't obtain any pressure release in 0 or 1 minute.
    if remaining_time == 2:
        # Only option is to open the local valve if it hasn't been used yet.
        if node not in valves_opened:
            return flow[node]
        else:
            return 0

    # Check all neighbors of node and compare the pressure obtained by opening the local valve or not.
    maximum_pressure = 0
    for neigh in graph[node]:
        # Option: Don't open local valve. Only obtains pressure from recursion.
        neigh_pressure_not_opened = max_pressure_release(neigh, remaining_time - 1, valves_opened)

        # Option: Open local valve (if possible). This only helps if the valve has flow value > 0.
        # Obtains pressure from recursion and the local valve.
        neigh_pressure_opened = 0
        if node not in valves_opened and flow[node] > 0:
            neigh_pressure_opened = max_pressure_release(neigh, remaining_time - 2, valves_opened + (node,))
            neigh_pressure_opened += flow[node] * (remaining_time - 1)  # Total pressure obtained by opening valve now.

        # Compare options to find the one with the highest pressure release.
        maximum_pressure = max(maximum_pressure, neigh_pressure_not_opened, neigh_pressure_opened)

    return maximum_pressure


print(f'The maximum pressure that can be released after {TOTAL_TIME} minutes '
      f'is: {max_pressure_release(START_NODE, TOTAL_TIME, ())}')
