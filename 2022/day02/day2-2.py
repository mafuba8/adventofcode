#!/usr/bin/python3
# Advent of Code 2022 - Day 2, Part 2
# Benedikt Otto

# input_file = '../examples/example_2.txt'
input_file = '../inputs/input_2.txt'

# Parse file into lists of matchups.
strategy_guide = []
with open(input_file) as file:
        for line in file.readlines():
            strategy_guide.append(line.strip().replace(' ',''))

# A: Rock, B: Paper, C: Scissors.
# Points rewarded for win/loss/draw.
outcome = {'AA': 3, 'AB': 6, 'AC': 0,
           'BA': 0, 'BB': 3, 'BC': 6,
           'CA': 6, 'CB': 0, 'CC': 3}

shape_score = {'A': 1, 'B': 2, 'C': 3}

my_pick = {'AX': 'C', 'AY': 'A', 'AZ': 'B',
           'BX': 'A', 'BY': 'B', 'BZ': 'C',
           'CX': 'B', 'CY': 'C', 'CZ': 'A'}

# Pick the right figure and get scores.
total_score = 0
for matchup in strategy_guide:
    pick = my_pick[matchup]
    score = outcome[matchup[0] + pick] + shape_score[pick]
    total_score += score
    print(f'Matchup: {matchup} - Pick: {pick} - Score: {score}')

print(f'Total score: {total_score}')
