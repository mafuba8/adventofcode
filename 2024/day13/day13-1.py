#!/usr/bin/python3
# Advent of Code 2024 - Day 13, Part 1
# Benedikt Otto
#
import re
import numpy as np

# input_file = '../examples/example_13.txt'
input_file = '../inputs/input_13.txt'

# Parse input into list of claw machines.
claw_machines = []
re_button_a = re.compile(r'^Button\sA:\sX\+(\d+),\sY\+(\d+)$')
re_button_b = re.compile(r'^Button\sB:\sX\+(\d+),\sY\+(\d+)$')
re_prize = re.compile(r'^Prize:\sX=(\d+),\sY=(\d+)$')
with open(input_file) as file:
    for line in file.readlines():
        if line[:8] == 'Button A':
            search = re_button_a.search(line)
            a_x = search.group(1)
            a_y = search.group(2)
        elif line[:8] == 'Button B':
            search = re_button_b.search(line)
            b_x = search.group(1)
            b_y = search.group(2)
        elif line[:5] == 'Prize':
            search = re_prize.search(line)
            prize_x = search.group(1)
            prize_y = search.group(2)
        elif line == '\n':
            claw_machine = {'a_x': int(a_x), 'a_y': int(a_y),
                            'b_x': int(b_x), 'b_y': int(b_y),
                            'pr_x': int(prize_x), 'pr_y': int(prize_y)}
            claw_machines.append(claw_machine)

# Remember last claw machine.
claw_machine = {'a_x': int(a_x), 'a_y': int(a_y),
                'b_x': int(b_x), 'b_y': int(b_y),
                'pr_x': int(prize_x), 'pr_y': int(prize_y)}
claw_machines.append(claw_machine)


# Find out the number of tokens needed.
num_tokens = 0
for cm_num, cm in enumerate(claw_machines):
    print(f'Claw Machine #{cm_num}')
    M = np.array([[cm['a_x'], cm['b_x']],
                  [cm['a_y'], cm['b_y']]], np.int32)
    p = np.array([cm['pr_x'], cm['pr_y']], np.int32)
    try:
        # Solve linear equation M * solution == p.
        solution = np.linalg.solve(M, p)
        s_a, s_b = solution

        # Results are floating-point numbers and we want integer solutions.
        # So we round and verify them.
        s_a, s_b = round(s_a), round(s_b)
        cx = s_a * cm['a_x'] + s_b * cm['b_x']
        cy = s_a * cm['a_y'] + s_b * cm['b_y']
        if cx == cm['pr_x'] and cy == cm['pr_y']:
            print(f' Solution found: {s_a, s_b} - Tokens: {3 * s_a + s_b}')
            num_tokens += 3 * s_a + s_b

    except np.linalg.LinAlgError:
        print(f' Matrix is singular.')

print(f'Fewest tokens needed to win all possible prizes: {num_tokens}')
