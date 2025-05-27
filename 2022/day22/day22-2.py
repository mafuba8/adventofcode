#!/usr/bin/python3
# Advent of Code 2022 - Day 22, Part 2
# Benedikt Otto
#
# I don't know if there is a better way to implement all the different edge wrappings rules than
# just writing down all the fourteen transformation rules.

# input_file = '../examples/example_22.txt'
input_file = '../inputs/input_22.txt'

# Parse input into dict(key=xy, val=char) and the path string.
map_dict = {}
path = ''
with open(input_file) as file:
    is_map_input = True
    for row_num, line in enumerate(file.readlines()):
        if line == '\n':
            is_map_input = False
        else:
            if is_map_input:
                for col_num, c in enumerate(line):
                    if c != '\n':
                        map_dict.setdefault((row_num, col_num), c)
            else:
                path = line.strip()

# Parse the path string into list of moves.
move_list = []
string = ''
for c in path:
    if c == 'R':
        move = (int(string), 'R')
        move_list.append(move)
        string = ''
    elif c == 'L':
        move = (int(string), 'L')
        move_list.append(move)
        string = ''
    else:
        string += c
# Last element doesn't have a direction.
move_list.append((int(string), 'N'))

# Edge mapping rule:
#   ((ax, ay), (bx, by), dir1, (cx, cy), (dx, dy), dir2
# means that if we are on a tile between (ax, ay) and (bx, by) and have the direction dir1,
# then a step in that direction puts us on a point between (cx, cy) and (dx, dy) with direction
# dir2.
#
# We do need to pay attention to the direction before/after, AND the order of the points.

# Mapping rules for the example cube net.
edge_mapping_rules = [((( 0,  8), ( 0, 11), '^'), (( 4,  3), ( 4,  0), 'v')),  # face 1 -> face 2
                      ((( 0,  8), ( 3,  8), '<'), (( 4,  4), ( 4,  7), 'v')),  # face 1 -> face 3
                      ((( 0, 11), ( 3, 11), '>'), ((11, 15), ( 8, 15), '<')),  # face 1 -> face 6
                      ((( 4,  0), ( 4,  3), '^'), (( 0, 11), ( 0,  8), 'v')),  # face 2 -> face 1
                      ((( 7,  0), ( 7,  3), 'v'), ((11, 11), (11,  8), '^')),  # face 2 -> face 5
                      ((( 4,  0), ( 7,  0), '<'), ((11, 15), (11, 12), '^')),  # face 2 -> face 6
                      ((( 4,  4), ( 4,  7), '^'), (( 0,  8), ( 3,  8), '>')),  # face 3 -> face 1
                      ((( 7,  4), ( 7,  7), 'v'), ((11,  8), ( 8,  8), '>')),  # face 3 -> face 5
                      ((( 4, 11), ( 7, 11), '>'), (( 8, 15), ( 8, 12), 'v')),  # face 4 -> face 6
                      (((11,  8), (11, 11), 'v'), (( 7,  3), ( 7,  0), '^')),  # face 5 -> face 2
                      ((( 8,  8), (11,  8), '<'), (( 7,  7), ( 7,  3), '^')),  # face 5 -> face 3
                      ((( 8, 15), (11, 15), '>'), (( 3, 11), ( 0, 11), '>')),  # face 6 -> face 1
                      (((11, 12), (11, 15), 'v'), (( 4,  3), ( 4,  0), '<')),  # face 6 -> face 2
                      ((( 8, 12), ( 8, 15), '<'), (( 7, 11), ( 4, 11), '^')),  # face 6 -> face 4
                      ]

# Mapping rules for the input cube net. (Obtained from a real-life paper cube net).
edge_mapping_rules = [(((  0,  50), (  0,  99), '^'), ((150,   0), (199,   0), '>')),
                      (((  0,  50), ( 49,  50), '<'), ((149,   0), (100,   0), '>')),
                      (((  0, 100), (  0, 149), '^'), ((199,   0), (199,  49), '^')),
                      (((  0, 149), ( 49, 149), '>'), ((149,  99), (100,  99), '<')),
                      ((( 49, 100), ( 49, 149), 'v'), (( 50,  99), ( 99,  99), '<')),
                      ((( 50,  50), ( 99,  50), '<'), ((100,   0), (100,  49), 'v')),
                      ((( 50,  99), ( 99,  99), '>'), (( 49, 100), ( 49, 149), '^')),
                      (((100,   0), (100,  49), '^'), (( 50,  50), ( 99,  50), '>')),
                      (((100,   0), (149,   0), '<'), (( 49,  50), (  0,  50), '>')),
                      (((100,  99), (149,  99), '>'), (( 49, 149), (  0, 149), '<')),
                      (((149,  50), (149,  99), 'v'), ((150,  49), (199,  49), '<')),
                      (((150,   0), (199,   0), '<'), ((  0,  50), (  0,  99), 'v')),
                      (((199,   0), (199,  49), 'v'), ((  0, 100), (  0, 149), 'v')),
                      (((150,  49), (199,  49), '>'), ((149,  50), (149,  99), '^'))
                      ]


def edge_order(edge_start, edge_end):
    """Generator for all the points that are between the edge_start and the edge_end
    coordinates, including the border points."""
    dfx, dfy = 0, 0
    count = 0
    if edge_start[0] == edge_end[0]:
        # Count through y. Figure out count direction.
        count = abs(edge_start[1] - edge_end[1])
        if edge_start[1] < edge_end[1]:
            dfy = 1
        elif edge_start[1] > edge_end[1]:
            dfy = -1
    elif edge_start[1] == edge_end[1]:
        # Count through x. Figure out count direction.
        count = abs(edge_start[0] - edge_end[0])
        if edge_start[0] < edge_end[0]:
            dfx = 1
        elif edge_start[0] > edge_end[0]:
            dfx = -1
    for k in range(count + 1):
        yield edge_start[0] + k * dfx, edge_start[1] + k * dfy


def create_edge_mapping(edge_rule):
    """Takes a single edge mapping rule and returns a dictionary of all position
    that are mapped through that rule."""
    edge_mapping = {}
    rule_from, rule_to = edge_rule
    edge_from_start, edge_from_end, dir_from = rule_from
    edge_to_start, edge_to_end, dir_to = rule_to

    for coord1, coord2 in zip(edge_order(edge_from_start, edge_from_end), edge_order(edge_to_start, edge_to_end)):
        x1, y1 = coord1
        x2, y2 = coord2
        edge_mapping[(x1, y1, dir_from)] = (x2, y2, dir_to)
    return edge_mapping


# Compile list of all positions that are involved when wrapping around the cube.
# All positions that are NOT in this dictionary do not involve stepping over cube edges
# and are therefore normal steps.
edge_mapping = {}
for mapping_rule in edge_mapping_rules:
    m = create_edge_mapping(mapping_rule)
    edge_mapping = {**edge_mapping, **m}


def turning(pos, turn):
    """Returns the new position after turning."""
    x, y, d = pos
    new_d = d
    if turn == 'R':
        match d:
            case '^':
                new_d = '>'
            case 'v':
                new_d = '<'
            case '<':
                new_d = '^'
            case '>':
                new_d = 'v'
    elif turn == 'L':
        match d:
            case '^':
                new_d = '<'
            case 'v':
                new_d = '>'
            case '<':
                new_d = 'v'
            case '>':
                new_d = '^'
    return x, y, new_d


def do_step(pos):
    """Does one step in the current direction and returns the new position (x, y, dir)."""
    global map_dict
    x, y, d = pos
    # Check if we are about to walk over an edge.
    if pos in edge_mapping:
        # In that case the edge_mapping gives us the new position (incl. direction).
        new_x, new_y, new_d = edge_mapping[pos]
    else:
        # No edge wrapping case, so one standard move, keeping the direction constant.
        dx, dy = 0, 0
        match d:
            case '^':
                dx, dy = -1, 0
            case 'v':
                dx, dy = 1, 0
            case '<':
                dx, dy = 0, -1
            case '>':
                dx, dy = 0, 1
        new_x, new_y = x + dx, y + dy
        new_d = d
    # Check if we can actually walk to this new position.
    if map_dict[(new_x, new_y)] == '.':
        pos = new_x, new_y, new_d
    else:
        # New spot blocked by a stone, so we don't change the position.
        pos = x, y, d
    return pos


# Starting position.
startpos_y = min([xy[1] for xy in map_dict if xy[0] == 0 and map_dict[xy] != ' '])
position = (0, startpos_y, '>')
# Run through all the moves on the path.
for move in move_list:
    print(f'Move: {move}')
    num_steps, turn = move
    # Walk in the current direction.
    for k in range(num_steps):
        position = do_step(position)
        print(position)

    # Turn left or right.
    position = turning(position, turn)
    print(f' Pos: {position}')

# Compute password.
match position[2]:
    case '>':
        facing = 0
    case 'v':
        facing = 1
    case '<':
        facing = 2
    case '^':
        facing = 3
# Rows and columns in the puzzle are 1-indexed.
password = (1000 * (position[0] + 1)
            + 4 * (position[1] + 1)
            + facing)
print(f'The final password is: {password}')
