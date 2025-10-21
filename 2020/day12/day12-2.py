#!/usr/bin/python3
# Advent of Code 2020 - Day 12, Part 2
# Benedikt Otto
#

# input_file = '../examples/example_12.txt'
input_file = '../inputs/input_12.txt'

# Parse input into a list of tuples (char, int).
instruction_list = []
with open(input_file) as file:
    for line in file.readlines():
        i_action = line[0]
        i_value = int(line[1:])
        instruction_list.append((i_action, i_value))


# A state is given by the xy-coords of the ship and the vector of the waypoint. Holding the waypoint
# as a vector makes it easy to rotate it, we just need to consider it relative to the ship xy.

def move_wp(wp, action, value):
    """Moves the waypoint vector according to the action."""
    match action:
        case 'N':
            wp = (wp[0] - value, wp[1])
        case 'S':
            wp = (wp[0] + value, wp[1])
        case 'W':
            wp = (wp[0], wp[1] - value)
        case 'E':
            wp = (wp[0], wp[1] + value)
        case 'R':
            match value:
                case 90:
                    wp = (wp[1], -wp[0])
                case 180:
                    wp = (-wp[0], -wp[1])
                case 270:
                    wp = (-wp[1], wp[0])
        case 'L':
            match value:
                case 90:
                    wp = (-wp[1], wp[0])
                case 180:
                    wp = (-wp[0], -wp[1])
                case 270:
                    wp = (wp[1], -wp[0])
    return wp


def do_action(state, instruction):
    """Changes the ship state according to the given move instruction."""
    xy_ship, wp = state
    action, value = instruction

    if action in ('N', 'S', 'W', 'E', 'L', 'R'):
        wp = move_wp(wp, action, value)
    elif action == 'F':
        # Move ship in direction of the waypoint.
        xy_ship = (xy_ship[0] + value * wp[0], xy_ship[1] + value * wp[1])

    new_state = xy_ship, wp
    return new_state


def print_state(state):
    """Prints the state according to the example."""
    xy, wp = state
    x, y = xy
    string = ''
    if y > 0:
        string += f'East {abs(y)}, '
    else:
        string += f'West {abs(y)}, '

    if x > 0:
        string += f'South {abs(x)}'
    else:
        string += f'North {abs(x)}'

    string += f' (WP: {wp})'
    print(string)


# Move ship according to the instruction.
ship_state = ((0, 0), (-1, 10))
for move_instruction in instruction_list:
    ship_state = do_action(ship_state, move_instruction)
    print(f'{move_instruction}')
    print_state(ship_state)

print()

# Calculate Manhattan distance.
dist = abs(ship_state[0][0]) + abs(ship_state[0][1])
print(f'Manhattan distance: {dist}.')
