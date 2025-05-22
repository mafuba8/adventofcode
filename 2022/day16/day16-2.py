#!/usr/bin/python3
# Advent of Code 2022 - Day 16, Part 2
# Benedikt Otto
#
# Since activating the same valve twice is a waste of time, we can split all the nonzero valves
# between us and the elephant, and then run a 26-minute simulation twice - each with the other's valves
# assumed to be open at the start.
# The problem then gets reduced to finding the partition of nonzero valves where the sum of both simulation
# gives the maximum pressure release.
#
import functools
import itertools
import re

# input_file = '../examples/example_16.txt'
input_file = '../inputs/input_16.txt'

# Start node and total available time.
START_NODE = 'AA'
TOTAL_TIME = 26

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


# First we reduce the size of the graph by removing all nodes that have flow 0 (except the START_NODE).
# But this means that we have edges with traversal time > 1, so we need to introduce weights.
weights = {}
for v1 in graph:
    for v2 in graph[v1]:
        weights.setdefault((v1, v2), 1)

# Remove all non-start nodes that have flow 0 and adjust the weights.
removable_nodes = [v for v in graph if flow[v] == 0 and v != START_NODE]
for node in removable_nodes:
    print(f'Removing node {node}.')
    for n0 in graph[node]:
        for n in graph[node]:
            if n != n0:
                graph[n0].append(n)
                graph[n0].remove(node)
                w = weights.get((n0, node))
                w += weights.get((node, n))
                weights.setdefault((n0, n), w)
    del graph[node]
    del flow[node]


@functools.cache
def max_pressure_release(node, remaining_time, valves_opened):
    """
    Returns the max. pressure release possible by starting at <node>, when we have
    <remaining_time> minutes remaining and the valves in the tuple <valves_opened>
    have already been opened.
    """
    # Recursion ends at 0, 1 or 2 minutes remaining.
    if remaining_time <= 1:
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
        neigh_pressure_not_opened = max_pressure_release(neigh, remaining_time - weights[(node, neigh)],
                                                         valves_opened)

        # Option: Open local valve (if possible). This only helps if the valve has flow value > 0.
        # Obtains pressure from recursion and the local valve.
        neigh_pressure_opened = 0
        if node not in valves_opened and flow[node] > 0:
            # Since order is irrelevant for nodes_visited, we sort the tuples to increase cache hit rate.
            x = list(valves_opened + (node, ))
            x.sort()
            neigh_pressure_opened = max_pressure_release(neigh, remaining_time - 1 - weights[(node, neigh)],
                                                         tuple(x))
            neigh_pressure_opened += flow[node] * (remaining_time - 1)  # Total pressure obtained by opening valve now.

        # Compare options to find the one with the highest pressure release.
        maximum_pressure = max(maximum_pressure, neigh_pressure_not_opened, neigh_pressure_opened)

    return maximum_pressure


maximum_pressure_duo = 0
# Split work into valves that are opened by me and valves that are opened by the elephant,
# then run both simulations with the other's valves already open and sum up the pressure gained.
valves_with_flow = [v for v in graph if flow[v] != 0]
for k in range(1, len(valves_with_flow)):
    valves_combinations_list = list(itertools.combinations(valves_with_flow, k))
    print(f'{k} valves: {len(valves_combinations_list)} partitions.')

    for valves_opened_human in valves_combinations_list:
        # Run simulation twice, once with the given valves open and once with the opposite valves open.
        valves_opened_elephant = tuple((v for v in graph if v not in valves_opened_human))
        pressure_human = max_pressure_release(START_NODE, TOTAL_TIME, valves_opened_human)
        pressure_elephant = max_pressure_release(START_NODE, TOTAL_TIME, valves_opened_elephant)
        maximum_pressure_duo = max(maximum_pressure_duo, pressure_human + pressure_elephant)

print(f'The maximum pressure that can be released after {TOTAL_TIME} minutes '
      f'when we work together with an elephant is: {maximum_pressure_duo}.')
