#!/usr/bin/python3
# Advent of Code 2021 - Day 11, Part 2
# Benedikt Otto
#

# input_file = '../examples/example_11.txt'
input_file = '../inputs/input_11.txt'

# Parse input into dict(key=xy, val=int).
energy_levels = {}
with open(input_file) as file:
    for row_num, row in enumerate(file.readlines()):
        for col_num, c in enumerate(row.strip()):
            energy_levels.setdefault((row_num, col_num), int(c))


def print_energy_levels():
    """Prints the grid of energy levels as in the example."""
    global energy_levels
    x_max = max([x for (x,_) in energy_levels.keys()])
    y_max = max([y for (_, y) in energy_levels.keys()])
    for x in range(x_max + 1):
        for y in range(y_max + 1):
            print(energy_levels[(x, y)], end='')
        print()


# Simulate the steps.
flash_count = 0
step = 1
while True:
    # All octopuses gain one level of energy.
    for xy in energy_levels:
        energy_levels[xy] += 1

    # Flood-fill like algorithm to handle flashes.
    flash_stack = [xy for xy in energy_levels if energy_levels[xy] > 9]
    has_flashed = set()
    while len(flash_stack) > 0:
        xy = flash_stack.pop()

        # Octopus at xy flashes.
        has_flashed.add(xy)
        # All surrounding octopuses gain energy.
        x, y = xy
        for xy_surround in [(x-1, y-1), (x-1, y), (x-1, y+1), (x, y-1), (x, y+1), (x+1, y-1), (x+1, y), (x+1, y+1)]:
            if xy_surround in energy_levels and not xy_surround in has_flashed:
                energy_levels[xy_surround] += 1
                if energy_levels[xy_surround] > 9 and not xy_surround in flash_stack:
                    flash_stack.append(xy_surround)

    # Zero out all octopuses that have flashed.
    for xy in has_flashed:
        energy_levels[xy] = 0
        flash_count += 1

    # Check if all octopuses flash at the same time.
    if all([energy_levels[xy] == 0 for xy in energy_levels]):
        print(f'All octopuses have flashed at the same time at step {step}.')
        break

    print(f'Step {step}: Flash count {flash_count}')
    step += 1
