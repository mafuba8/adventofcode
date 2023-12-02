#!/usr/bin/python3
# Advent of Code 2023 - Day 2, Part 1
# Benedikt Otto

# Open puzzle file
#with open('example_2.txt') as file:
with open('input_2.txt') as file:
    lines = file.readlines()

# Parse input file into lists of games
game_list = []
for line in lines:
    game = line.split(':')
    game_name = game[0]
    game_details = game[1]

    # Game = list of rounds
    round_list = []
    for count, game_round in enumerate(game_details.split(';')):
        # round = list of draws
        draw_dict = {'red': 0, 'green': 0, 'blue': 0}
        for draw in game_round.split(','):
            # draw = dict(key=colour, val=count)
            draw_details = draw.strip().split(' ')
            draw_count = draw_details[0]
            draw_colour = draw_details[1]
            # Missing counts stay at 0 because they won't get overwritten.
            draw_dict[draw_colour] = int(draw_count)

        round_list.append(draw_dict)

    game_list.append(round_list)


# Find the games that are possible if the bag contained a certain amount of cubes
POSSIBLE_RED = 12
POSSIBLE_GREEN = 13
POSSIBLE_BLUE = 14

possible_game_list = []
for game_index, game in enumerate(game_list):
    game_is_possible = True
    for draw in game:
        if draw['red'] > POSSIBLE_RED or draw['green'] > POSSIBLE_GREEN or draw['blue'] > POSSIBLE_BLUE:
            game_is_possible = False

    if game_is_possible:
        # Game numbers start at 1
        possible_game_list.append(game_index + 1)


print('Possible games:')
print(possible_game_list)

total_number = 0
for number in possible_game_list:
    total_number += number

print('')
print(f'Sum of possible game numbers: {total_number}')

