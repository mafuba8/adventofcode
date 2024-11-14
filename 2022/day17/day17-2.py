#!/usr/bin/python3
# Advent of Code 2022 - Day 17, Part 2
# Benedikt Otto
#
# Since it is not feasible to run billions of simulation steps, we use the fact that this
# problem only contains a finite amount of combinations. In particular, the 'state' defined by
#  - current rock number (0 - 4)
#  - current jet number (0 - len(input))
#  - relative position of the highest occupied row of each column (7-tuple where one element is always 0).
# does repeat after a certain amount of steps (cycle).
#
# Since we get the same height increase within a cycle, we can just calculate how many cycles
# the simulation repeats to determine the total tower height.
#

# input_file = '../examples/example_17.txt'
input_file = '../inputs/input_17.txt'

#NUM_ROCKS = 2022
NUM_ROCKS = 1_000_000_000_000

with open(input_file) as file:
    jet_pattern = file.readline().strip()

# Global area with pixels, as a dict(key=xy, val=pixel).
area = {}

class Rock:
    def __init__(self, base_pixels, offset_col):
        self.pixels = []
        for p in base_pixels:
            self.pixels.append((3 + p[0] + offset_col, 2 + p[1]))

    def jet_push(self, direction):
        """Modifies the <self.pixels> values according to the direction.
        If the push results in it hitting something, no values are changed."""
        y_dir = 0
        match direction:
            case '>':
                y_dir = 1
            case '<':
                y_dir = -1

        # Determine pixel positions when pushed by the jet.
        new_pixels = []
        for p in self.pixels:
            new_pos = (p[0], p[1] + y_dir)
            new_pixels.append(new_pos)

        # Check if the new position would hit the wall or another rock.
        movable = True
        for p in new_pixels:
            if p[1] < 0 or p[1] > 6 or p in area:
                movable = False
                break
        if movable:
            self.pixels = new_pixels

    def move_down(self):
        """Moves all pixels of the rock down once, returning True if it worked. If the move results in it
        hitting something, no values are changed, returns False instead."""
        # Determine pixel positions when moved one pixel down.
        new_pixels = []
        for p in self.pixels:
            new_pos = (p[0] - 1, p[1])
            new_pixels.append(new_pos)

        # Check if the new position would hit the wall or another rock.
        movable = True
        for p in new_pixels:
            if p[0] < 0 or p in area:
                movable = False
        if movable:
            self.pixels = new_pixels
            return True
        else:
            return False


# Types of rocks, points relative to bottom-left pixel.
rock_row = [(0,0), (0,1), (0,2), (0,3)]
rock_plus = [(0,1), (1,0), (1,1), (1,2), (2,1)]
rock_corner = [(0,0), (0,1), (0,2), (1,2), (2,2)]
rock_col = [(0,0), (1,0), (2,0), (3,0)]
rock_square = [(0,0), (0,1), (1,0), (1,1)]
base_rock_tiles = [rock_row, rock_plus, rock_corner, rock_col, rock_square]

# Remember the different states and offsets (heights).
state_list = []
offset_list = []
highest_columns = [-1 for n in range(7)]

# Offset defines the highest row with a block in it. Then the Floor is -1.
offset = -1
jet_num = 0
# Run simulation with enough rocks to find a cycle.
for rock_num in range(2000):
    # New rock starts falling.
    rock = Rock(base_rock_tiles[rock_num % 5], offset + 1)

    # Simulate the falling rock.
    movable = True
    while movable:
        # Rock gets pushed by the next jet.
        jet = jet_pattern[jet_num]
        rock.jet_push(jet)
        jet_num = (jet_num + 1) % len(jet_pattern)

        # Rock falls down one row.
        movable = movable and rock.move_down()

    # Rock stopped falling and its pixels get saved to the area dict.
    for p in rock.pixels:
        area.setdefault(p, '#')

    # Save the highest occupied row as new offset.
    for p in area.keys():
        offset = max(offset, p[0])

    # Remember the offset (height).
    offset_list.append(offset)
    # Determine the highest pixel of each column.
    for col in range(7):
        for row in range(highest_columns[col], offset+1):
            if (row, col) in area:
                highest_columns[col] = row
    # To get a tuple of relative heights, we norm highest_column to the lowest value.
    col_min = min(highest_columns)
    normed_columns = [c - col_min for c in highest_columns]

    # Record the state and see if it repeats (which means that we found a cycle).
    state = (normed_columns, rock_num % 5, jet_num % len(jet_pattern))
    if state in state_list:
        # Here we have found the cycle.
        index_cycle_begin = state_list.index(state)
        index_cycle_end = rock_num
        cycle_length = index_cycle_end - index_cycle_begin

        offset_pre_cycle = offset_list[index_cycle_begin]
        offset_post_cycle = offset
        height_diff_cycle = offset_post_cycle - offset_pre_cycle

        print(f'Found repeat of the full state at rock {rock_num}.')
        print(f' Cycle index: {index_cycle_begin} -> {index_cycle_end}.')
        print(f' => Cycle length: {cycle_length}')
        print(f' Heights at cycle begin and end: {offset_pre_cycle} -> {offset_post_cycle}')
        print(f' => Height gained within one cycle: {height_diff_cycle}')
        print()
        break
    else:
        # Here we haven't found the cycle yet, record the state and continue with the simulation.
        state_list.append(state)


# Calculate the height at NUM_ROCKS by counting how many cycles we pass.
num_cycles = (NUM_ROCKS - 1 - index_cycle_begin) // cycle_length
remainder = (NUM_ROCKS - 1 - index_cycle_begin) % cycle_length

# Total height is determined from the height gain in one cycle plus the initial offset.
# Keeping in mind that height = offset + 1.
total_height = num_cycles * height_diff_cycle + offset_list[index_cycle_begin + remainder] + 1
print(f'Height of Tower after {NUM_ROCKS} rocks have fallen: {total_height}')
