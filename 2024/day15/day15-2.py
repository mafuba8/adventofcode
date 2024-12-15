#!/usr/bin/python3
# Advent of Code 2024 - Day 15, Part 2
# Benedikt Otto
#

# input_file = '../examples/example_15.txt'
input_file = '../inputs/input_15.txt'

# Parse input into:
#   warehouse_map_lines: list of strings.
#   moves_list: list of moves '^' / 'v' / '>' / '<'.
warehouse_map_list = []
moves_list = []
with open(input_file) as file:
    map_input = True
    for row in file.readlines():
        if row == '\n':
            # One empty row means that we have entered the input part with the moves.
            map_input = False
            continue
        if map_input:
            map_line = ''
            # Widening the warehouse map.
            for char in row.strip():
                match char:
                    case '#':
                        map_line += '##'
                    case 'O':
                        map_line += '[]'
                    case '.':
                        map_line += '..'
                    case '@':
                        map_line += '@.'
            warehouse_map_list.append(map_line)
        else:
            for char in row.strip():
                moves_list.append(char)

# Transfer warehouse_map_list into dict(key=xy, val=char).
warehouse_map = {}
for row_num, row in enumerate(warehouse_map_list):
    for col_num, char in enumerate(row):
        warehouse_map.setdefault((row_num, col_num), char)


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


def get_other_box_side(xy):
    """Takes the coordinate of a box side '[' / ']' and returns the coordinate
    of the other box side."""
    global warehouse_map
    match warehouse_map[xy]:
        case '[':
            return xy[0], xy[1] + 1
        case ']':
            return xy[0], xy[1] - 1
        case _:
            return xy


def is_movable(xy, move_dir):
    """Checks if the object at xy is movable in the given direction (but doesn't move anything)."""
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

    match warehouse_map[next_xy]:
        case '#':
            # New spot is a wall.
            return False
        case '.':
            # New spot is free.
            return True
        case '[' | ']':
            if move_dir in '><':
                # Horizontal movements only require us to check the next item.
                return is_movable(next_xy, move_dir)
            elif move_dir in '^v':
                # Vertical movements require both sides of the box to be movable.
                return is_movable(next_xy, move_dir) and is_movable(get_other_box_side(next_xy), move_dir)


def move_object(xy, move_dir):
    """Moves the object and all connected items in the given direction.
    Assumes that every involved object is actually movable."""
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

    match warehouse_map[next_xy]:
        case '.':
            # New spot is empty.
            warehouse_map[next_xy] = warehouse_map[xy]
            warehouse_map[xy] = '.'
        case '[' | ']':
            # New spot is a box, so we need to check if this box can be moved.
            box_other_xy = get_other_box_side(next_xy)
            if move_dir in '><':
                # Horizontal movements can be done recursively as in part 1.
                move_object(next_xy, move_dir)
                warehouse_map[next_xy] = warehouse_map[xy]
                warehouse_map[xy] = '.'
            elif move_dir in '^v':
                # For vertical movements we need to move both sides of the box.

                # Move the box side that is directly in the way, and move the current object.
                move_object(next_xy, move_dir)
                warehouse_map[next_xy] = warehouse_map[xy]
                warehouse_map[xy] = '.'

                # Move the other side of the box (the resulting spot will be free).
                move_object(box_other_xy, move_dir)


print("Starting warehouse layout:")
print_warehouse()

# Execute all moves in order.
for move_dir in moves_list:
    # Get current position of the bot.
    bot_pos = [xy for xy in warehouse_map if warehouse_map[xy] == '@'][0]
    print(f'Move {bot_pos}: {move_dir}')

    # Move the bot if possible.
    if is_movable(bot_pos, move_dir):
        move_object(bot_pos, move_dir)


print()
print("Final warehouse layout:")
print_warehouse()


# Determine the GPS coordinates of the boxes.
gps_coord_sum = 0
for xy in warehouse_map:
    if warehouse_map[xy] == '[':
        gps_coord = 100 * xy[0] + xy[1]
        gps_coord_sum += gps_coord

print(f"Sum of all boxes' GPS coordinates: {gps_coord_sum}.")
