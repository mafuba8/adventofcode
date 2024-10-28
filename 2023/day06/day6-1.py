#!/usr/bin/python3
# Advent of Code 2023 - Day 6, Part 1
# Benedikt Otto
import re

# Open puzzle file.
#with open('example_6.txt') as file:
with open('../inputs/input_6.txt') as file:
    lines = file.readlines()

# Put values into respective lists
re_wspace = re.compile(r'\s+')
list_time = re_wspace.sub(' ', lines[0]).strip().split(' ')
list_dist = re_wspace.sub(' ', lines[1]).strip().split(' ')

# Skip first column because it only has the field name.
list_time = list_time[1:]
list_dist = list_dist[1:]

# Determine how many combinations there are to win the race.
win_list = []
for race_num in range(len(list_time)):
    time = int(list_time[race_num])
    dist = int(list_dist[race_num])

    win_count = 0
    # button_time can't be 0 or time.
    for button_time in range(1, time):
        speed = button_time
        travel_time = time - button_time
        race_dist = speed * travel_time
        if race_dist > dist:
            win_count += 1

    win_list.append(win_count)
    print(f'Race {race_num}: Win Count: {win_count}')

# Print result.
win_multiplied = 1
for j in win_list:
    win_multiplied *= j

print(f'Win count multiplied: {win_multiplied}')
