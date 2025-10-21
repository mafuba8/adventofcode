#!/usr/bin/python3
# Advent of Code 2020 - Day 12, Part 1
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


# Ship state = Tuple(xy-coordinates, direction)
#   direction = {'N', 'S', 'E', 'W'}
#   N: x-1, S: x+1, W: y-1, E: y+1

def rotate(direction, action, value):
    # Set array for cyclic rotations.
    if action == 'R':
        arr = ('N', 'E', 'S', 'W')
    elif action == 'L':
        arr = ('N', 'W', 'S', 'E')
    idx = arr.index(direction)
    idx = (idx + value // 90) % 4
    return arr[idx]


def do_action(state, instruction):
    xy, direction = state
    new_x, new_y = xy
    action, value = instruction
    match action:
        case 'N':
            new_x = xy[0] - value
        case 'S':
            new_x = xy[0] + value
        case 'W':
            new_y = xy[1] - value
        case 'E':
            new_y = xy[1] + value
        case 'L':
            direction = rotate(direction, 'L', value)
        case 'R':
            direction = rotate(direction, 'R', value)
        case 'F':
            match direction:
                case 'N':
                    new_x = xy[0] - value
                case 'S':
                    new_x = xy[0] + value
                case 'W':
                    new_y = xy[1] - value
                case 'E':
                    new_y = xy[1] + value
    return (new_x, new_y), direction


def print_state(state):
    """Prints the state according to the example."""
    xy, direction = state
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

    string += f' ({direction})'
    print(string)


# Move ship according to the instruction.
state = ((0, 0), 'E')
for instruction in instruction_list:
    state = do_action(state, instruction)
    print(f'{instruction}')
    print_state(state)

print()

# Calculate Manhattan distance.
dist = abs(state[0][0]) + abs(state[0][1])
print(f'Manhattan distance: {dist}.')
