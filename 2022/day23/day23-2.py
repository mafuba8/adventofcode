#!/usr/bin/python3
# Advent of Code 2022 - Day 23, Part 2
# Benedikt Otto
#

# input_file = '../examples/example_23a.txt'
# input_file = '../examples/example_23b.txt'
input_file = '../inputs/input_23.txt'

# Parse input into dict(key=xy, val=char).
map_dict = {}
with open(input_file) as file:
    for row_num, line in enumerate(file.readlines()):
        for col_num, c in enumerate(line.strip()):
            map_dict[(row_num, col_num)] = c


def print_map(m):
    """Prints the map as in the example."""
    x_min = min([xy[0] for xy in m])
    x_max = max([xy[0] for xy in m])
    y_min = min([xy[1] for xy in m])
    y_max = max([xy[1] for xy in m])

    for x in range(x_min, x_max + 1):
        for y in range(y_min, y_max + 1):
            if (x, y) in m:
                print(m[(x, y)], end='')
            else:
                print('.', end='')
        print('')
    print()


def check_positions(xy_list, m):
    """Checks if all the given positions are free."""
    global map_dict
    return all([xy not in m or m[xy] == '.' for xy in xy_list])


def propose_direction(elf, order, m):
    """Determines which direction the elf proposes."""
    x, y = elf
    # If no other elves are around, the elf does not propose a direction.
    if check_positions([(x-1, y-1), (x-1, y), (x-1, y+1), (x, y-1),
                        (x, y+1), (x+1, y-1), (x+1, y), (x+1, y+1)], m):
        return None
    # Elf needs to propose a direction.
    for direction in order:
        match direction:
            case 'N':
                if check_positions([(x-1, y-1), (x-1, y), (x-1, y+1)], m):
                    return 'N'
            case 'S':
                if check_positions([(x+1, y-1), (x+1, y), (x+1, y+1)], m):
                    return 'S'
            case 'W':
                if check_positions([(x-1, y-1), (x, y-1), (x+1, y-1)], m):
                    return 'W'
            case 'E':
                if check_positions([(x-1, y+1), (x, y+1), (x+1, y+1)], m):
                    return 'E'
    return None


def proposed_coord(elf, order, m):
    """Determines which coordinate the given elf proposes."""
    x, y = elf
    proposed_direction = propose_direction(elf, order, m)
    match proposed_direction:
        case 'N':
            return x-1, y
        case 'S':
            return x+1, y
        case 'W':
            return x, y-1
        case 'E':
            return x, y+1
    # No proposed direction = returns none
    return None


def do_round(m, direction_order):
    """Simulates a full round and returns the new map dict, and whether any elf moved at all."""
    proposed_positions = {}
    for elf in [xy for xy in m if m[xy] == '#']:
        proposed_positions[elf] = proposed_coord(elf, direction_order, m)

    # Build a new map dict.
    new_map = {}
    is_movement = False
    l = list(proposed_positions.values())
    for elf in proposed_positions:
        xy = proposed_positions[elf]
        if xy is None:
            # No proposed direction = elf stays in his spot.
            new_map[elf] = '#'
        else:
            # Check if this elf is the only one proposing this coordinate.
            if l.count(xy) == 1:
                new_map[xy] = '#'
                is_movement = True
            else:
                new_map[elf] = '#'
    return new_map, is_movement


# Initial direction order.
direction_order = ['N', 'S', 'W', 'E']

# Run the simulation until there was no movement.
movement = True
round = 1
while movement:
    map_dict, movement = do_round(map_dict, direction_order)
    print(f'Round {round}: Movement: {movement}')

    # Rotate list of directions.
    direction_order = direction_order[1:] + list(direction_order[0])
    round += 1

print(f'First round where no Elf moves: {round - 1}')
