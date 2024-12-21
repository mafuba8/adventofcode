#!/usr/bin/python3
# Advent of Code 2024 - Day 21, Part 2
# Benedikt Otto
#
# The number of possible inputs grows exponentially, so it is not feasible to simulate all 25 bot recursions.
# Instead, we notice that each directional input sequence ends up as a short string of directions followed
# by the 'A' button, e.g. '<v^A'. Since every sequence starts and ends at an 'A', we can just recursively
# compute the minimum number of inputs for each component and add them together to find the minimum
# number of inputs of the whole sequence.
#
# The number of possible components is pretty limited, so we can use memoization to reuse a lot of the
# intermediary results.
#
import functools

# input_file = '../examples/example_21.txt'
input_file = '../inputs/input_21.txt'

# Parse input into list of strings.
code_list = []
with open(input_file) as file:
    for line in file.readlines():
        code_list.append(line.strip())


# Graph representing the keypad.
keypad_graph_vertices = {'A', '0', '1', '2', '3', '4',
                         '5', '6', '7', '8', '9'}

keypad_graph = {'A': ['0', '3'], '0': ['A', '2'], '1': ['2', '4'], '2': ['0', '1', '3', '5'],
                '3': ['A', '2', '6'], '4': ['1', '5', '7'], '5': ['2', '4', '6', '8'],
                '6': ['3', '5', '9'], '7': ['4', '8'], '8': ['5', '7', '9'], '9': ['6', '8']}

# Direction buttons that need to be pressed so we can get from one button to the second.
direction_buttons = {('A', '0'): '<', ('A', '3'): '^', ('0', 'A'): '>', ('0', '2'): '^',
                     ('1', '2'): '>', ('1', '4'): '^',
                     ('2', '0'): 'v', ('2', '1'): '<', ('2', '3'): '>', ('2', '5'): '^',
                     ('3', 'A'): 'v', ('3', '2'): '<', ('3', '6'): '^',
                     ('4', '1'): 'v', ('4', '5'): '>', ('4', '7'): '^',
                     ('5', '2'): 'v', ('5', '4'): '<', ('5', '6'): '>', ('5', '8'): '^',
                     ('6', '3'): 'v', ('6', '5'): '<', ('6', '9'): '^', ('7', '4'): 'v', ('7', '8'): '>',
                     ('8', '5'): 'v', ('8', '7'): '<', ('8', '9'): '>', ('9', '6'): 'v', ('9', '8'): '<'}

# Since the arrow-keypad is pretty small, we just write down the shortest button combinations.
arrow_keypad_shortest = {('A', '^'): ['<'], ('A', '>'): ['v'], ('A', 'v'): ['<v', 'v<'],
                         ('A', '<'): ['<v<', 'v<<'], ('A', 'A'): [''],
                         ('^', 'A'): ['>'], ('^', 'v'): ['v'], ('^', '>'): ['v>', '>v'],
                         ('^', '<'): ['v<'], ('^', '^'): [''],
                         ('<', 'v'): ['>'], ('<', '>'): ['>>'], ('<', '^'): ['>^'],
                         ('<', 'A'): ['>>^', '>^>'], ('<', '<'): [''],
                         ('v', '<'): ['<'], ('v', '^'): ['^'], ('v', '>'): ['>'],
                         ('v', 'A'): ['>^', '^>'], ('v', 'v'): [''],
                         ('>', 'A'): ['^'], ('>', 'v'): ['<'], ('>', '^'): ['^<', '<^'],
                         ('>', '<'): ['<<'], ('>', '>'): ['']}


def shortest_paths(to_vertex, dist_dict):
    """Given the dict of distances to start_vertex, returns list of shortest paths
     from <start_vertex> to <to_vertex>."""
    if dist_dict[to_vertex] == 0:
        return [[to_vertex]]

    to_dist = dist_dict[to_vertex]
    path_list = []
    for n in keypad_graph[to_vertex]:
        if dist_dict[n] == to_dist - 1:
            for path in shortest_paths(n, dist_dict):
                path.append(to_vertex)
                path_list.append(path)
    return path_list


def keypad_shortest_paths(button_from, button_to):
    """Builds dict with shortest distances from <button_from> to <button_to>."""
    non_visited = keypad_graph_vertices.copy()
    dist = {v: 1000 for v in keypad_graph_vertices}
    dist[button_from] = 0

    while len(non_visited) > 0:
        # Get vertex with minimum distance.
        minimum = 1000
        for v in non_visited:
            if dist[v] < minimum:
                min_vertex = v
                minimum = dist[v]

        non_visited.remove(min_vertex)
        # Work through all neighbours of min_vertex
        for n in keypad_graph[min_vertex]:
            alt = dist[min_vertex] + 1  # here all weights are 1.
            if alt < dist[n]:
                dist[n] = alt

    return shortest_paths(button_to, dist)


def find_direction_sequences(code):
    """Returns a list of all sequences of buttons than can be input in the first directional keyboard
     so that the robot on the numerical keyboard inputs the given code."""
    button_sequence = 'A' + code
    direction_sequences = ['']
    for k in range(len(button_sequence) - 1):
        button_from = button_sequence[k]
        button_to = button_sequence[k+1]
        paths_append = keypad_shortest_paths(button_from, button_to)

        new_direction_sequences = []
        for seq in paths_append:
            direction_sequence = ''
            for k in range(len(seq) - 1):
                direction_sequence += direction_buttons[(seq[k], seq[k+1])]

            for d in direction_sequences:
                new_direction_sequences.append(d + direction_sequence + 'A')

        direction_sequences = new_direction_sequences
    return direction_sequences


def directional_control(target_dir_button_seq):
    """Returns a list of all sequences of buttons that need to be pressed in order to control a robot
     to press the buttons given by <needed_button_sequence>."""
    target_dir_button_seq = 'A' + target_dir_button_seq
    needed_button_sequence = ['']
    for k in range(len(target_dir_button_seq) - 1):
        button_from = target_dir_button_seq[k]
        button_to = target_dir_button_seq[k + 1]
        new_needed_button_sequence = []
        for path in arrow_keypad_shortest[(button_from, button_to)]:
            for s in needed_button_sequence:
                new_needed_button_sequence.append(s + path + 'A')
        needed_button_sequence = new_needed_button_sequence
    return needed_button_sequence


@functools.cache
def minimum_inputs(dir_button_seq, recursion_depth):
    """Returns the minimum numbers of button presses that we need to input on a directional keyboard
     so that the controlled robot inputs the given button sequence on his keyboard.
     Input sequences always end with an 'A'."""

    # Recursion depth 0 means that we are manually pressing the buttons, so the number of inputs
    # is equal to the number of buttons pressed.
    if recursion_depth == 0:
        return len(dir_button_seq)

    min_inputs_list = []
    # Figure out the directional inputs on the next keyboard and split it into '....A' components, e.g.
    # '<A' => ['<v<A>>^A', 'v<<A>>^A', '<v<A>^>A', 'v<<A>^>A'], so:
    #   '<v<A>>^A' => ['<v<A', '>>^A'] for the recursion.
    #   'v<<A>>^A' => ['v<<A', '>>^A'] for the recursion.
    #   '<v<A>^>A' => ['<v<A', '>^>A'] for the recursion.
    #   'v<<A>^>A' => ['v<<A', '>^>A'] for the recursion.
    #
    for seq2 in directional_control(dir_button_seq):
        # Split 'v>>A>>^A' -> ['v>>A', '>>^A']
        min_inputs_seq2 = 0
        for component in seq2.split('A')[:-1]:
            component = component + 'A'
            min_inputs_seq2 += minimum_inputs(component, recursion_depth - 1)
        min_inputs_list.append(min_inputs_seq2)

    return min(min_inputs_list)


def shortest_human_input_sequence_length(code, num_dir_keypad_bots):
    """Returns the length of the shortest input sequence for the given code if we have
     <num_dir_keypad_bots> robots on the directional keypads."""
    min_component_list = []
    # Get the list of possible initial directional sequence so that the keypad robots inputs the right code.
    # For each sequence find the minimum number of inputs on the final keypad and return the minimum of them.
    for first_direction_seq in find_direction_sequences(code):
        m = minimum_inputs(first_direction_seq, num_dir_keypad_bots)
        min_component_list.append(m)
    return min(min_component_list)


NUM_DIR_KEYPAD_BOTS = 25
# Find the sum of all complexities.
complexity_sum = 0
for code in code_list:
    minimum_length = shortest_human_input_sequence_length(code, NUM_DIR_KEYPAD_BOTS)

    # Calculate complexity.
    numeric_value = int(code.replace('A', ''))
    complexity = minimum_length * numeric_value

    print(f'Code: {code} - Minimum length: {minimum_length} - Complexity: {complexity}')
    complexity_sum += complexity

print(f'Sum of all complexities: {complexity_sum}')

