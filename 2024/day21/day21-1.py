#!/usr/bin/python3
# Advent of Code 2024 - Day 21, Part 1
# Benedikt Otto
#

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
    """Returns a list of all sequences of buttons that can be input in the first directional keyboard
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


def directional_control(dir_button_sequence):
    """Returns a list of all sequences of buttons that need to be pressed in order to control a robot
     to press the buttons given by <dir_button_sequence>."""
    dir_button_sequence = 'A' + dir_button_sequence
    dir_button_sequence_sequence = ['']
    for k in range(len(dir_button_sequence) - 1):
        button_from = dir_button_sequence[k]
        button_to = dir_button_sequence[k+1]
        new_dir_button_sequence_sequence = []
        for path in arrow_keypad_shortest[(button_from, button_to)]:
            for s in dir_button_sequence_sequence:
                new_dir_button_sequence_sequence.append(s + path + 'A')
        dir_button_sequence_sequence = new_dir_button_sequence_sequence
    return dir_button_sequence_sequence


def shortest_human_input_sequence_length(code):
    """Finds the length of the shortest sequences that we need to input in the final
     directional keyboard so that the final robot inputs the given code."""
    # Find all shortest combination for the order of buttons on the first directional keyboard
    # that result in the numeric keyboard robot to input the desired code.
    direction_seq = find_direction_sequences(code)

    # For each button combination in direction_seq, find the order of buttons that the
    # robot on the second directional keyboard need to press.
    direction_seq_seq = []
    for seq1 in direction_seq:
        for s in directional_control(seq1):
            direction_seq_seq.append(s)

    # For each button combination in direction_seq_seq, find the order of buttons that
    # we need to press on the third (and final) directional keyboard.
    direction_seq_seq_seq = []
    for seq2 in direction_seq_seq:
        for s in directional_control(seq2):
            direction_seq_seq_seq.append(s)

    # Find the code complexity.
    min_length = 1000
    for x in direction_seq_seq_seq:
        min_length = min(min_length, len(x))

    numeric_value = int(code.replace('A', ''))
    return min_length * numeric_value


# Find the sum of all complexities.
complexity_sum = 0
for code in code_list:
    x = shortest_human_input_sequence_length(code)
    print(f'Code: {code} - Complexity: {x}')
    complexity_sum += x

print(f'Sum of all complexities: {complexity_sum}')
