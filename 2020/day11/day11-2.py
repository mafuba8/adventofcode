#!/usr/bin/python3
# Advent of Code 2020 - Day 11, Part 2
# Benedikt Otto
#

# input_file = '../examples/example_11.txt'
input_file = '../inputs/input_11.txt'

# Parse input into a dict of chars.
seat_state = {}
with open(input_file) as file:
    for row_num, row in enumerate(file.readlines()):
        for col_num, c in enumerate(row.strip()):
            seat_state[(row_num, col_num)] = c


def print_state(seat_dir):
    """Prints a diagram of the seat state as in the examples."""
    max_row = max(xy[0] for xy in seat_dir)
    max_col = max(xy[1] for xy in seat_dir)

    for x in range(max_row + 1):
        for y in range(max_col + 1):
            print(seat_dir[(x, y)], end='')
        print()
    print()


def check_direction(xy, d, seat_dir):
    """Checks if an occupied seat is visible at xy in the given direction."""
    is_occupied = False
    z = xy

    # Follow the ray in direction d until it hits a seat or is outside the dictionary.
    z = (z[0] + d[0], z[1] + d[1])
    while z in seat_dir:
        match seat_dir.get(z):
            case '#':
                return True
            case 'L':
                return False
        z = (z[0] + d[0], z[1] + d[1])
    return False


def new_seat_state(xy, seat_dir):
    """Determines the next state of seat xy in seat_dir.
    Returns the new seat state and whether it has changed."""
    # Count occupied seats in the eight directions.
    x, y = xy
    num_occupied = 0
    for d in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
        if check_direction(xy, d, seat_dir):
            num_occupied += 1

    # Determine seat state at xy according to the rules.
    match seat_dir[xy]:
        case 'L':
            if num_occupied == 0:
                return '#', True
            else:
                return 'L', False
        case '#':
            if num_occupied >= 5:
                return 'L', True
            else:
                return '#', False
    return '.', False


# Do seat switching rounds until it stabilizes.
state_changed = True
while state_changed:
    state_changed = False
    # Build new seat state.
    new_state = {}
    for xy in seat_state:
        new_state[xy], seat_changed = new_seat_state(xy, seat_state)
        state_changed = state_changed or seat_changed
    seat_state = new_state

print('Final seat layout:')
print_state(seat_state)

# Count occupied seats.
occupied_seats = ([xy for xy in seat_state if seat_state[xy] == '#'])
print(f'Occupied seats after people stop moving around: {len(occupied_seats)}.')
