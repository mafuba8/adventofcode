#!/usr/bin/python3
# Advent of Code 2025 - Day 10, Part 1
# Benedikt Otto
#
import math

# INPUT_FILE = '../examples/example_10.txt'
INPUT_FILE = '../inputs/input_10.txt'

# Parse input into list of machines.
machine_list = []
with open(INPUT_FILE) as file:
    for line in file.readlines():
        # Split in '[.##.' and '(3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}'
        part_ind_lights, part_button_jolt = line.strip().split('] ')
        # Split in '(3) (1,3) (2) (2,3) (0,2) (0,1)' and '3,5,4,7}'
        part_buttons, part_joltage = part_button_jolt.split(' {')

        # Parse buttons (as list of integers).
        buttons = []
        for x in part_buttons.split(' '):
            x = x.replace('(', '')
            x = x.replace(')', '')
            button = tuple(int(char) for char in x.split(','))
            buttons.append(button)

        # Indicator lights as a string.
        ind_lights = part_ind_lights[1:]

        # Joltage as list of integers.
        joltage = [int(x) for x in part_joltage[:-1].split(',')]

        machine_list.append((ind_lights, buttons, joltage))


def change_indicator_lights(lights: str, button: tuple):
    new_lights = []
    for idx, s in enumerate(lights):
        if idx in button:
            if s == '#':
                new_lights.append('.')
            else:
                new_lights.append('#')
        else:
            new_lights.append(s)
    return ''.join(new_lights)

def get_neighbours(vertex: str, b_schematics: list[tuple]):
    return [change_indicator_lights(vertex, b) for b in b_schematics]


def shortest_button_combinations(il_diagram: str, button_schematics: list[tuple]) -> int:
    # Biggest (manhattan-) distance we can cover with one button press.
    """Calculates the shortest button combination needed to configure the il_diagram."""

    # We build a graph where vertices = indicator light state and edges = button pushes,
    # and look for shortest distances using Dijkstra.

    # All indicator lights start in off position.
    start_vertex = il_diagram.replace('#', '.')

    # DIJKSTRA ALGORITHM.
    non_visited = [start_vertex]
    dist = {start_vertex: 0}
    prev = {}

    # Instead of prepping all vertices, we gradually add them to our vertex list as we discover more.
    vertices_added = {start_vertex}

    while len(non_visited) > 0:
        # Get a vertex with minimum known distance.
        minimum = math.inf
        for v in non_visited:
            if v in dist and dist[v] < minimum:
                minimum = dist[v]
                min_vertex = v

        # Shortcut because we are only interested in the shortest path to end.
        if min_vertex == il_diagram:
            break

        non_visited.remove(min_vertex)
        # Work through all neighbours of min_vertex.
        for n_vertex in get_neighbours(min_vertex, button_schematics):
            alt = dist[min_vertex] + 1
            if alt < dist.get(n_vertex, math.inf):
                dist[n_vertex] = alt
                prev[n_vertex] = min_vertex

            # Add newly discovered neighbours to our list of vertices.
            if n_vertex not in vertices_added:
                non_visited.append(n_vertex)
                vertices_added.add(n_vertex)

    return dist[il_diagram]


# Run through all machines and sum up the shortest button presses.
fewest_button_presses = 0
for machine in machine_list:
    indicator_lights, buttons, joltage = machine
    fewest_button_presses += shortest_button_combinations(indicator_lights, buttons)

print(f'Fewest button presses required to configure all machines: {fewest_button_presses}.')
