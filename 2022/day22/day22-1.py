#!/usr/bin/python3
# Advent of Code 2022 - Day 22, Part 1
# Benedikt Otto
#

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


# For each row and column, note the minimum and maximum indices where there are traversable tiles.
row_min = {}
row_max = {}
col_min = {}
col_max = {}
for xy in map_dict:
    x, y = xy
    if map_dict[xy] != ' ':
        row_min[x] = min(row_min.get(x, 1000), y)
        row_max[x] = max(row_max.get(x, 0), y)
        col_min[y] = min(col_min.get(y, 1000), x)
        col_max[y] = max(col_max.get(y, 0), x)


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


def walk_straight(pos, num_steps):
    """Returns the new position after walking num_steps steps in the current direction."""
    global map_dict
    x, y, d = pos
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

    for k in range(num_steps):
        new_x, new_y = x + dx, y + dy
        # Case when wrapping happens.
        if (new_x, new_y) not in map_dict or map_dict[(new_x, new_y)] == ' ':
            if dx == 0:
                # Move horizontally.
                if new_y < row_min[new_x]:
                    new_y = row_max[new_x]
                elif new_y > row_max[new_x]:
                    new_y = row_min[new_x]
            if dy == 0:
                # Move vertically.
                if new_x < col_min[new_y]:
                    new_x = col_max[new_y]
                elif new_x > col_max[new_y]:
                    new_x = col_min[new_y]

        match map_dict[(new_x, new_y)]:
            case '#':
                break
            case '.':
                x, y = new_x, new_y

    return x, y, d


# Move according to the path instructions.
position = (0, row_min[0], '>')  # Starting position.
for move in move_list:
    print(f'Move: {move}')
    num_steps, turn = move
    # Walk in the current direction.
    position = walk_straight(position, num_steps)

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
