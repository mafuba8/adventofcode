#!/usr/bin/python3
# Advent of Code 2025 - Day 10, Part 2
# Benedikt Otto
#
# My version of the excellent solution by tenthmascot from
#   https://old.reddit.com/r/adventofcode/comments/1pk87hl/2025_day_10_part_2_bifurcate_your_way_to_victory/
#
from itertools import combinations
from dataclasses import dataclass
from functools import cache

# INPUT_FILE = '../examples/example_10.txt'
INPUT_FILE = '../inputs/input_10.txt'

# Parse input into list of machines.
@dataclass
class Machine:
    lights: str
    buttons: tuple[tuple[int, ...]]
    joltage: tuple[int, ...]

machine_list = []
with open(INPUT_FILE) as file:
    for line in file.readlines():
        # Split in '[.##.' and '(3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}'
        part_ind_lights, part_button_jolt = line.strip().split('] ')
        # Split in '(3) (1,3) (2) (2,3) (0,2) (0,1)' and '3,5,4,7}'
        part_buttons, part_joltage = part_button_jolt.split(' {')

        # Parse buttons (as tuple of integer tuples).
        buttons = []
        for x in part_buttons.split(' '):
            x = x.replace('(', '')
            x = x.replace(')', '')
            button = tuple(int(char) for char in x.split(','))
            buttons.append(button)
        buttons = tuple(buttons)

        # Indicator lights as a string.
        ind_lights = part_ind_lights[1:]

        # Joltage as tuple of integers.
        joltage = tuple(int(x) for x in part_joltage[:-1].split(','))

        m = Machine(ind_lights, buttons, joltage)
        machine_list.append(m)


@cache
def get_patterns(m_buttons: tuple[int, ...],
                 num_joltages: int) -> dict[tuple[int, ...], int]:
    """Returns a dict of patterns and the smallest number of buttons pressed to reach it.
    A pattern is a tuple of integers that is obtained from the (0,...,0) state
    after pressing a certain set of buttons."""
    pattern_dict = {}
    button_count = len(m_buttons)
    # Run through all button press combinations.
    for num_buttons_pressed in range(button_count + 1):
        for button_combination in combinations(range(button_count), num_buttons_pressed):
            # Calculate the vector of differences they create.
            pattern = [0,] * num_joltages
            for button_idx in button_combination:
                for k in m_buttons[button_idx]:
                    pattern[k] += 1
            pattern = tuple(pattern)

            # Save the patterns along with the smallest known button combination that lead to it.
            if pattern not in pattern_dict:
                pattern_dict[pattern] = num_buttons_pressed
            elif num_buttons_pressed < pattern_dict[pattern]:
                pattern_dict[pattern] = num_buttons_pressed
    return pattern_dict


@cache
def minimum_joltage_button_presses(target_joltage: tuple[int, ...],
                                   m_buttons: tuple[int, ...]) -> int:
    """Returns the minimum number of button presses necessary to reach the target joltage."""
    # Recursion end.
    if all([j == 0 for j in target_joltage]):
        return 0

    # Get dict of patterns and their shortest number of button presses.
    num_joltages = len(target_joltage)
    patterns = get_patterns(m_buttons, num_joltages)

    # Run through all patterns to find the shortest distances.
    presses = []
    for pattern in patterns:
        # Subtract the pattern, effectively undoing the button presses involved in the pattern.
        new_joltage = tuple(target_joltage[k] - pattern[k] for k in range(num_joltages))

        # If this pattern actually appears, subtracting it leads to all entries being positive and even.
        if all(j >= 0 and j % 2 == 0 for j in new_joltage):
            # In this case we can halve each joltage, obtaining a smaller set of joltages.
            new_joltage = tuple(j // 2 for j in new_joltage)

            # Number of presses in the pattern, plus 2 times the presses from the recursion.
            count = patterns[pattern] + 2 * minimum_joltage_button_presses(new_joltage, m_buttons)
            presses.append(count)

    # Return the minimum of the possible presses.
    if presses:
        return min(presses)
    return 1_000_000


# Run through all machines and sum up the shortest button presses.
fewest_button_presses = 0
for m in machine_list:
    print(m)
    mbp = minimum_joltage_button_presses(m.joltage, m.buttons)
    fewest_button_presses += mbp
    print(f'  fewest presses: {mbp}')

print(f'Fewest button presses required to configure the joltage of all machines: {fewest_button_presses}.')
