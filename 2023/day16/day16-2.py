#!/usr/bin/python3
# Advent of Code 2023 - Day 16, Part 2
# Benedikt Otto

# Open puzzle file.
lines = []
# with open('example_16.txt') as file:
with open('../inputs/input_16.txt') as file:
    for line in file.readlines():
        lines.append(line.strip())

layout_height = len(lines)
layout_width = len(lines[0])

# Parse file into dictionary.
# layout = dict(key=(x, y), val=symbol)
layout = {}
for row_num, line in enumerate(lines):
    for col_num, char in enumerate(line):
        layout.setdefault((row_num, col_num), char)


def beam_step(beam):
    """Simulates one step for one beam. Returns a list of beams."""
    new_beam_list = []
    beam_x, beam_y, direction = beam
    # Calculate coordinates of next tile and check if it exists.
    match direction:
        case 'u':
            next_x = beam_x - 1
            next_y = beam_y
        case 'd':
            next_x = beam_x + 1
            next_y = beam_y
        case 'l':
            next_x = beam_x
            next_y = beam_y - 1
        case 'r':
            next_x = beam_x
            next_y = beam_y + 1

    if next_x < 0 or next_y < 0 or next_x >= layout_width or next_y >= layout_height:
        return []

    # Create next beam(s) and add them to the result list.
    next_symbol = layout[(next_x, next_y)]
    match next_symbol:
        case '.':
            new_beam_list.append((next_x, next_y, direction))
        case '|':
            if direction == 'u' or direction == 'd':
                new_beam_list.append((next_x, next_y, direction))
            else:
                new_beam_list.append((next_x, next_y, 'u'))
                new_beam_list.append((next_x, next_y, 'd'))
        case '-':
            if direction == 'l' or direction == 'r':
                new_beam_list.append((next_x, next_y, direction))
            else:
                new_beam_list.append((next_x, next_y, 'l'))
                new_beam_list.append((next_x, next_y, 'r'))
        case '\\':
            match direction:
                case 'u':
                    new_beam_list.append((next_x, next_y, 'l'))
                case 'd':
                    new_beam_list.append((next_x, next_y, 'r'))
                case 'l':
                    new_beam_list.append((next_x, next_y, 'u'))
                case 'r':
                    new_beam_list.append((next_x, next_y, 'd'))
        case '/':
            match direction:
                case 'u':
                    new_beam_list.append((next_x, next_y, 'r'))
                case 'd':
                    new_beam_list.append((next_x, next_y, 'l'))
                case 'l':
                    new_beam_list.append((next_x, next_y, 'd'))
                case 'r':
                    new_beam_list.append((next_x, next_y, 'u'))
    return new_beam_list


def count_energized(start_beam):
    """Counts the number of energized tiles if the starting beam is this."""
    beam_list = beam_step(start_beam)  # Calculate the first set of beams made by the start_beam.
    visited_tiles = set()  # Set of visited tiles with direction
    energized_tiles = set()  # Set of visited tiles without direction

    while len(beam_list) > 0:
        new_beam_list = []

        for beam in beam_list:
            energized_tiles.add((beam[0], beam[1]))
            if beam in visited_tiles:
                continue
            new_beam_list += beam_step(beam)
            visited_tiles.add(beam)

        beam_list = new_beam_list

    return len(energized_tiles)


# A beam is a triple (x, y, direction) where direction is one of 'u', 'd', 'l', 'r'.
# Try out all starting positions of the lasers and get the maximum number of energized tiles.
# We start with an imaginary beam coming from outside
maximum = 0
for row_num in range(layout_height):
    maximum = max(maximum, count_energized((row_num, -1, 'r')))
    maximum = max(maximum, count_energized((row_num, layout_width, 'l')))

for col_num in range(layout_width):
    maximum = max(maximum, count_energized((-1, col_num, 'd')))
    maximum = max(maximum, count_energized((layout_height, col_num, 'u')))

print(f'Maximum number of energized tiles: {maximum}')
