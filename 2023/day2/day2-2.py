#!/usr/bin/python3
# Advent of Code 2023 - Day 2, Part 2
# Benedikt Otto

# Open puzzle file
#with open('example_2.txt') as file:
with open('../inputs/input_2.txt') as file:
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


# For each game, find the fewest number of cubes that need to be in the bag
# to make the game possible.
power_list = []
for game in game_list:
    red_list = [draw['red'] for draw in game]
    green_list = [draw['green'] for draw in game]
    blue_list = [draw['blue'] for draw in game]

    # Minimum needed numbers of cubes is the maximum of the respective count drawn.
    min_reds = max(red_list)
    min_greens = max(green_list)
    min_blues = max(blue_list)

    # The power of this game is just all minimum values multiplied together.
    power = min_reds * min_greens * min_blues
    power_list.append(power)

print('Power Tower (gnihihi):')
print(power_list)

# Total power is all powers added together.
total_power = 0
for power in power_list:
    total_power += power

print('')
print(f'Total power: {total_power}')

