#!/usr/bin/python3
# Advent of Code 2020 - Day 17, Part 2
# Benedikt Otto
#

# input_file = '../examples/example_17.txt'
input_file = '../inputs/input_17.txt'

# We save the state as a list of active cubes (only).
cube_state = []
with open(input_file) as file:
    for row_num, row in enumerate(file.readlines()):
        for col_num, c in enumerate(row.strip()):
            if c == '#':
                cube_state.append((row_num, col_num, 0, 0))

print(cube_state)

def print_state(state: list) -> None:
    """Prints the given state similar to the examples."""
    x_min = min([x for x,_,_,_ in state]); x_max = max([x for x,_,_,_ in state])
    y_min = min([y for _,y,_,_ in state]); y_max = max([y for _,y,_,_ in state])
    z_min = min([z for _,_,z,_ in state]); z_max = max([z for _,_,z,_ in state])
    w_min = min([w for _,_,_,w in state]); w_max = max([w for _,_,_,w in state])

    for w in range(w_min, w_max +1):
        for z in range(z_min, z_max +1):
            print(f'z = {z}, w = {w}:')
            for x in range(x_min, x_max +1):
                for y in range(y_min, y_max +1):
                    if (x, y, z, w) in state:
                        print('#', end='')
                    else:
                        print('.', end='')
                print()
            print()


def count_active_neighbours(xyzw: tuple[int, int, int, int], state: list) -> int:
    """Counts the number of active neighbouring cubes."""
    # Run through all 80 neighbours (not counting the cube itself).
    count = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            for dz in [-1, 0, 1]:
                for dw in [-1, 0, 1]:
                    n = (xyzw[0] + dx, xyzw[1] + dy, xyzw[2] + dz, xyzw[3] + dw)
                    if n != xyzw and n in state:
                        count += 1
    return count


def do_cycle(state: list) -> list:
    """Simulates a single cycle and returns the list of the new state."""
    new_state = []
    x_min = min([x for x,_,_,_ in state]); x_max = max([x for x,_,_,_ in state])
    y_min = min([y for _,y,_,_ in state]); y_max = max([y for _,y,_,_ in state])
    z_min = min([z for _,_,z,_ in state]); z_max = max([z for _,_,z,_ in state])
    w_min = min([w for _,_,_,w in state]); w_max = max([w for _,_,_,w in state])

    # Only cubes that are neighbours of an active cube can potentially become active.
    for x in range(x_min - 1, x_max + 1 +1):
        for y in range(y_min - 1, y_max + 1 +1):
            for z in range(z_min - 1, z_max + 1 +1):
                for w in range(w_min - 1, w_max + 1 +1):
                    xyzw = (x, y, z, w)
                    count_neigh = count_active_neighbours(xyzw, state)
                    # Active cubes with 2 or 3 neighbours stay active.
                    if xyzw in state and count_neigh in {2, 3}:
                        new_state.append(xyzw)
                    # Inactive cubes with exactly 3 neighbours will become active.
                    if xyzw not in state and count_neigh == 3:
                        new_state.append(xyzw)

    return new_state

# Simulate six cycles.
NUM_CYCLES = 6
for cycle in range(NUM_CYCLES):
    cube_state = do_cycle(cube_state)
    print(f'Cycle {cycle + 1}: {len(cube_state)} active.')

print(f'Number of active cubes after {NUM_CYCLES} cycles: {len(cube_state)}.')
