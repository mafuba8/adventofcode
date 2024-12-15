#!/usr/bin/python3
# Advent of Code 2024 - Day 15, Part 1
# Benedikt Otto
#

# input_file = '../examples/example_15.txt'
input_file = '../inputs/input_15.txt'

# Parse input into
#   warehouse_map: dict(key=xy, val=char).
#   moves_list: list of moves '^' / 'v' / '>' / '<'.
warehouse_map = {}
moves_list = []
with open(input_file) as file:
    map_input = True
    for row_num, row in enumerate(file.readlines()):
        if row == '\n':
            # One empty row means that we have entered the input part with the moves.
            map_input = False
            continue
        for col_num, char in enumerate(row.strip()):
            if map_input:
                warehouse_map.setdefault((row_num, col_num), char)
            else:
                moves_list.append(char)


def print_warehouse():
    """Prints the layout of the warehouse similar to the examples given."""
    global warehouse_map
    x_max = max([x for (x,_) in warehouse_map])
    y_max = max([y for (_,y) in warehouse_map])
    for x in range(x_max + 1):
        for y in range(y_max + 1):
            print(warehouse_map[(x, y)], end='')
        print('')
    print('')


def move_object(xy, move_dir):
    """Tries to move the object at coordinate xy in the given direction.
    Returns True if it could be moved, and False if it could not be moved. """
    next_xy = xy
    match move_dir:
        case '<':
            next_xy = (xy[0], xy[1] - 1)
        case '>':
            next_xy = (xy[0], xy[1] + 1)
        case '^':
            next_xy = (xy[0] - 1, xy[1])
        case 'v':
            next_xy = (xy[0] + 1, xy[1])

    # Check if we can move the current object to the new spot.
    match warehouse_map[next_xy]:
        case '.':
            # New spot is empty.
            warehouse_map[next_xy] = warehouse_map[xy]
            warehouse_map[xy] = '.'
            return True
        case '#':
            # New spot is a wall.
            return False
        case 'O':
            # New spot is a box, so recursively check if that one can be moved.
            was_movable = move_object(next_xy, move_dir)
            if was_movable:
                # The box could be moved, so move the current object too.
                warehouse_map[next_xy] = warehouse_map[xy]
                warehouse_map[xy] = '.'
                return True
            else:
                # The box could not be moved, so neither move the current object.
                return False


print("Starting warehouse layout:")
print_warehouse()

# Execute all moves in order.
for move in moves_list:
    # Get current position of the bot.
    bot_pos = [xy for xy in warehouse_map if warehouse_map[xy] == '@'][0]
    print(f'Move {bot_pos}: {move}')

    # Move the bot if possible.
    move_object(bot_pos, move)

print()
print("Final warehouse layout:")
print_warehouse()


# Determine the GPS coordinates of the boxes.
gps_coord_sum = 0
for xy in warehouse_map:
    if warehouse_map[xy] == 'O':
        gps_coord = 100 * xy[0] + xy[1]
        gps_coord_sum += gps_coord

print(f"Sum of all boxes' GPS coordinates: {gps_coord_sum}.")
