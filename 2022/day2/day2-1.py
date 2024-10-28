#!/usr/bin/python3
# Advent of Code 2022 - Day 2, Part 1
# Benedikt Otto

# input_file = '../examples/example_2.txt'
input_file = '../inputs/input_2.txt'

# Parse file into lists of matchups.
strategy_guide = []
with open(input_file) as file:
        for line in file.readlines():
            strategy_guide.append(line.strip().replace(' ',''))

# A/X: Rock, B/Y: Paper, C/Z: Scissors.
# Points rewarded for win/loss/draw.
outcome = {'AX': 3, 'AY': 6, 'AZ': 0,
           'BX': 0, 'BY': 3, 'BZ': 6,
           'CX': 6, 'CY': 0, 'CZ': 3}

shape_score = {'X': 1, 'Y': 2, 'Z': 3}

total_score = 0
for matchup in strategy_guide:
    score = outcome[matchup] + shape_score[matchup[1]]
    print(f'Matchup: {matchup} - Score: {score}')
    total_score += score

print(f'Total Score: {total_score}')
