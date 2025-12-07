#!/usr/bin/python3
# Advent of Code 2025 - Day 7, Part 2
# Benedikt Otto
#
import functools

# INPUT_FILE = '../examples/example_07.txt'
INPUT_FILE = '../inputs/input_07.txt'

# Parse input into a dict of characters. Remember the coords of the starting tile.
tachyon_manifold = {}
start_tile = ()
with open(INPUT_FILE) as file:
    for row_num, line in enumerate(file.readlines()):
        for col_num, char in enumerate(line.strip()):
            tachyon_manifold[(row_num, col_num)] = char
            if char == 'S':
                start_tile = (row_num, col_num)


@functools.cache
def count_timelines(particle: tuple[int, int]) -> int:
    """Counts the number of timelines in which the given particle will end up."""
    global tachyon_manifold
    timeline_count = 0

    if particle not in tachyon_manifold:
        return 1
    else:
        particle_x, particle_y = particle
        match tachyon_manifold[particle]:
            case '.' | 'S':
                return count_timelines((particle_x + 1, particle_y))
            case '^':
                return (count_timelines((particle_x + 1, particle_y - 1))
                        + count_timelines((particle_x + 1, particle_y + 1)))
            case _:  # Should not happen.
                return 0

print(f'A single tachyon particle would end up in {count_timelines(start_tile)} different timelines.')
