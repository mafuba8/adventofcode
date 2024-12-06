#!/usr/bin/python3
# Advent of Code 2024 - Day 6, Part 1
# Benedikt Otto
#

# input_file = '../examples/example_6.txt'
input_file = '../inputs/input_6.txt'

# Parse input into dict(key=xy, val=char)
area = {}
start_pos = (0, 0)
with open(input_file) as file:
    for row_num, row in enumerate(file.readlines()):
        for col_num, char in enumerate(row.strip()):
            area.setdefault((row_num, col_num), char)
            if char == '^':
                start_pos = (row_num, col_num)


# Starting position and direction.
pos = start_pos
direction = 'U'

# Simulate the guard and remember the visited tiles.
visited_tiles = set()
while True:
    visited_tiles.add(pos)
    # Determine the next position.
    match direction:
        case 'U':
            new_pos = (pos[0] - 1, pos[1])
        case 'D':
            new_pos = (pos[0] + 1, pos[1])
        case 'L':
            new_pos = (pos[0], pos[1] - 1)
        case 'R':
            new_pos = (pos[0], pos[1] + 1)

    # Check if new pos would be outside the mapped area.
    if new_pos not in area.keys():
        break

    # Check if the guard hits an obstacle.
    if area[new_pos] == '#':
        # Turn right 90 degrees.
        match direction:
            case 'U':
                direction = 'R'
            case 'D':
                direction = 'L'
            case 'L':
                direction = 'U'
            case 'R':
                direction = 'D'
    else:
        # Do a step and repeat.
        pos = new_pos


# Get number of visited tiles.
num_visited = len(visited_tiles)
print(f'Number of visited tiles: {num_visited}')
