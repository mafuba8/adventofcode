#!/usr/bin/python3
# Advent of Code 2020 - Day 15, Part 2
# Benedikt Otto
#

# input_file = '../examples/example_15.txt'
input_file = '../inputs/input_15.txt'

# Parse input into a list of integers.
with open(input_file) as file:
    starting_numbers = [int(s) for s in file.readline().split(',')]


def memory_game(initial_numbers: list[int], turn_count: int):
    """Simulates the memory game for turn_count rounds and returns the last number spoken."""
    num = 0

    # Remember the last two turns where the number has been spoken.
    memory_1 = {}  # last time it was spoken.
    memory_2 = {}  # second to last time it was spoken.

    # Do the memory game for the given number of turns.
    last_num = 0
    for turn in range(turn_count):
        if turn < len(initial_numbers):
            # First few turns according to the initial numbers.
            num = initial_numbers[turn]

        elif last_num not in memory_2:
            # First time that the number has been spoken.
            num = 0
        else:
            # Number has been spoken before.
            num = memory_1[last_num] - memory_2[last_num]

        # Remember the turn numbers.
        if num in memory_1:
            memory_2[num] = memory_1[num]
        memory_1[num] = turn

        # Remember number for next round.
        last_num = num

    return num

print(f'Starting numbers: {starting_numbers}.')
print(f'The 30 millionth number spoken will be {memory_game(starting_numbers, 30_000_000)}.')
