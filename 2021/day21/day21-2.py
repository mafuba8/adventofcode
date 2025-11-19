#!/usr/bin/python3
# Advent of Code 2021 - Day 21, Part 2
# Benedikt Otto
#
import functools

# input_file = '../examples/example_21.txt'
input_file = '../inputs/input_21.txt'

# Parse input into the initial player positions.
p1_position, p2_position = 0, 0
with open(input_file) as file:
    for line in file.readlines():
        if 'Player 1' in line:
            p1_position = int(line.split(': ')[1])
        if 'Player 2' in line:
            p2_position = int(line.split(': ')[1])

# Score needed to win the game.
WINNING_SCORE = 21

@functools.cache
def count_universes(player: int,
                    p1_score: int, p2_score: int,
                    p1_pos: int, p2_pos: int) -> tuple[int, int]:
    """Given the current score and position of both players, determines in how many universes
    player 0 and player 1 win, when it is p_num's turn next."""
    p1_win, p2_win = 0, 0
    if player == 1:  # Player 1's turn.
        for d1_roll in [1, 2, 3]:
            for d2_roll in [1, 2, 3]:
                for d3_roll in [1, 2, 3]:
                    new_pos = (p1_pos - 1 + d1_roll + d2_roll + d3_roll) % 10 + 1
                    new_score = p1_score + new_pos
                    if new_score >= WINNING_SCORE:
                        # In this universe, player one wins.
                        u1, u2 = 1, 0
                    else:
                        # Recursively count the winning universes with the new game state.
                        u1, u2 = count_universes(2, new_score, p2_score, new_pos, p2_pos)
                    p1_win += u1
                    p2_win += u2

    else:  # Player 2's turn.
        for d1_roll in [1, 2, 3]:
            for d2_roll in [1, 2, 3]:
                for d3_roll in [1, 2, 3]:
                    new_pos = (p2_pos - 1 + d1_roll + d2_roll + d3_roll) % 10 + 1
                    new_score = p2_score + new_pos
                    if new_score >= WINNING_SCORE:
                        # In this universe, player two wins.
                        u1, u2 = 0, 1
                    else:
                        # Recursively count the winning universes with the new game state.
                        u1, u2 = count_universes(1, p1_score, new_score, p1_pos, new_pos)
                    p1_win += u1
                    p2_win += u2

    return p1_win, p2_win


# Determine which player wins in more universes.
win_count = count_universes(1, 0, 0, p1_position, p2_position)
print(f'Final universe count:')
print(f'  Player 1: {win_count[0]:,}')
print(f'  Player 2: {win_count[1]:,}')
print(f'The player with more universes wins in a total of {max(win_count)} universes.')
