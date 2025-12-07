#!/usr/bin/python3
# Advent of Code 2025 - Day 7, Part 1
# Benedikt Otto
#

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

# A beam is given by the xy-coords of its current location. Since all beams will point downwards, we omit the direction.

def beam_step(beam_set):
    """Simulates what happens with the given beams in the next step. Returns a new set of beams created by them."""
    global tachyon_manifold
    new_beams = set()
    split_count = 0

    # For each beam, simulate one step.
    for beam in beam_set:
        beam_x, beam_y = beam
        match tachyon_manifold.get((beam_x + 1, beam_y), ' '):
            case '.':  # Beam does not hit a splitter.
                xy = (beam_x + 1, beam_y)
                if xy in tachyon_manifold:
                    new_beams.add(xy)
            case '^':  # Beam hits a splitter, creating two new beams.
                for xy in [(beam_x + 1, beam_y - 1), (beam_x + 1, beam_y + 1)]:
                    if xy in tachyon_manifold:
                        new_beams.add(xy)
                split_count += 1
    return new_beams, split_count


# A single beams starts at the 'S' tile.
beams = {start_tile}

# Simulate the splitting until all beams are out of the manifold.
total_split_count = 0
while len(beams) > 0:
    beams, count = beam_step(beams)
    total_split_count += count

print(f'Total number of splits: {total_split_count}.')
