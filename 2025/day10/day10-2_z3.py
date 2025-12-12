#!/usr/bin/python3
# Advent of Code 2025 - Day 10, Part 2
# Benedikt Otto
#
# This is a linear optimization problem, so even though I don't like to use
# external packages, the solution is substantially easier by using an SMT solver like z3.
import z3

# INPUT_FILE = '../examples/example_10.txt'
INPUT_FILE = '../inputs/input_10.txt'

# Parse input into list of machines.
machine_list = []
with open(INPUT_FILE) as file:
    for line in file.readlines():
        # Split in '[.##.' and '(3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}'
        part_ind_lights, part_button_jolt = line.strip().split('] ')
        # Split in '(3) (1,3) (2) (2,3) (0,2) (0,1)' and '3,5,4,7}'
        part_buttons, part_joltage = part_button_jolt.split(' {')

        # Parse buttons (as list of integers).
        buttons = []
        for x in part_buttons.split(' '):
            x = x.replace('(', '')
            x = x.replace(')', '')
            button = tuple(int(char) for char in x.split(','))
            buttons.append(button)

        # Indicator lights as a string.
        ind_lights = part_ind_lights[1:]

        # Joltage as list of integers.
        joltage = [int(x) for x in part_joltage[:-1].split(',')]

        machine_list.append((ind_lights, buttons, joltage))


# Run through all machines and sum up the shortest button presses.
fewest_button_presses = 0
for machine in machine_list:
    indicator_lights, buttons, target_joltage = machine
    print(machine)

    # Solve using the optimization solver.
    solver = z3.Optimize()

    # Build variables for the solver and add them to the left side of the equation.
    variables = []
    equation_left = [None] * len(target_joltage)
    for idx, button in enumerate(buttons):
        var = z3.Int(f'button_{idx}_presses')
        variables.append(var)

        # Constraint for positive variables.
        solver.add(var >= 0)

        # Each button adds var many button presses to the joltage at each button entry.
        for button_entry in button:
            if equation_left[button_entry] is None:
                equation_left[button_entry] = var
            else:
                equation_left[button_entry] = equation_left[button_entry] + var


    # Build the equation left_side == target_joltage.
    for jolt_idx, joltage in enumerate(target_joltage):
        if equation_left[jolt_idx] is not None:
            solver.add(equation_left[jolt_idx] == joltage)

    # Let the solver minimize the sum of all button presses.
    min_presses = solver.minimize(sum(variables))

    # Add to the solution.
    if solver.check() == z3.sat:
        x = min_presses.value().as_long()
        fewest_button_presses += x
        print(f'  Fewest button presses: {x}')
    else:
        raise Exception('Solution is not satisfiable.')


print()
print(f'Fewest button presses required to set all joltage levels: {fewest_button_presses}')
