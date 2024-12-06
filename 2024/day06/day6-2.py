#!/usr/bin/python3
# Advent of Code 2024 - Day 6, Part 2
# Benedikt Otto
#

#input_file = '../examples/example_6.txt'
input_file = '../inputs/input_6.txt'

# Parse input into dict(key=xy, val=char)
area = {}
start_pos = (0, 0)
with open(input_file) as file:
    for row_num, row in enumerate(file.readlines()):
        for col_num, char in enumerate(row.strip()):
            area.setdefault((row_num, col_num), char)
            if char == '^':
                # Remember the starting position and replace the character there with a dot.
                start_pos = (row_num, col_num)
                area[(row_num, col_num)] = '.'


def next_pos(pos, direction):
    """Returns the xy-position of the tile in the given direction."""
    match direction:
        case 'U': pos_new = (pos[0] - 1, pos[1])
        case 'D': pos_new = (pos[0] + 1, pos[1])
        case 'L': pos_new = (pos[0], pos[1] - 1)
        case 'R': pos_new = (pos[0], pos[1] + 1)
    return pos_new


def do_step(pos, direction, walk_area=area):
    """Returns the next step (xy-coords, next_direc),
    accounting for potential obstacles."""
    new_pos = next_pos(pos, direction)
    if new_pos not in walk_area.keys():
        # Next step leads outside the area.
        return None, None

    # Check if the guard hits an obstacle.
    if walk_area[new_pos] == '#':
        # Hitting an obstacle keeps the xy-position, but with a rotated direction.
        match direction:
            case 'U': direction = 'R'
            case 'D': direction = 'L'
            case 'L': direction = 'U'
            case 'R': direction = 'D'
        return pos, direction
    else:
        # No obstacle, so we can continue along this direction.
        return new_pos, direction


def print_path(path_list, walk_area=area):
    """For troubleshooting: Prints the whole area including the walked path."""
    draw_dict = {}
    for pos, direction in path_list:
        match direction:
            case 'U': c = '^'
            case 'D': c = 'v'
            case 'L': c = '<'
            case 'R': c = '>'
        draw_dict.setdefault(pos, c)

    row_max = max([x for (x,_) in area.keys()])
    col_max = max([y for (_,y) in area.keys()])
    for rnum in range(row_max + 1):
        for cnum in range(col_max + 1):
            xy = (rnum, cnum)
            if xy in draw_dict:
                print(draw_dict[xy], end='')
            else:
                print(walk_area[xy], end='')
        print('')


# Starting position and direction.
pos = start_pos
direction = 'U'

# Simulate the steps from the starting position.
visited_tiles = [(start_pos, direction)]
while True:
    pos, direction = do_step(pos, direction)
    if pos is None:
        break
    visited_tiles.append((pos, direction))


num_visited = len(set([x for (x, _) in visited_tiles]))
print(f'Number of visited tiles: {num_visited}')


# Try putting an obstacle on each tile on the path and simulate the full path
potential_obstacles = [xy for (xy,_) in visited_tiles]

obstacle_set = set()
for obstacle in potential_obstacles:
    # First occurrence of the obstacle-xy in the walked path.
    index = [xy for (xy, _) in visited_tiles].index(obstacle)
    if index == 0:
        continue  # Can't put an obstacle on the starting position.

    # To speed up things we can re-use the original path until the obstacle is reached for the first time.
    modified_path = visited_tiles[:index]
    pos_mod, dir_mod = visited_tiles[index - 1]

    # Modify area by putting in an additional obstacle.
    modified_area = area.copy()
    modified_area[obstacle] = '#'

    # Do a walk from pos with the modified area and check if we end up in a
    # position & state that has been walked already.
    #pos_mod = pos
    #dir_mod = direction
    steps = 0
    while True:
        pos_mod, dir_mod = do_step(pos_mod, dir_mod, modified_area)
        if pos_mod is None:
            break  # Here the guard ran outside the area.
        if (pos_mod, dir_mod) in modified_path:
            # Here we have found a circle.
            print(f' found circle for obstacle {obstacle} (steps: {steps})')
            obstacle_set.add(obstacle)
            break
        modified_path.append((pos_mod, dir_mod))
        steps += 1


print(f'Number of obstacles that result into a loop: {len(obstacle_set)}')
