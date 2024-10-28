#!/usr/bin/python3
# Advent of Code 2023 - Day 6, Part 2
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

# Combine the digits into one single number
the_time = ""
the_dist = ""
for k in range(len(list_time)):
    the_time += list_time[k]
    the_dist += list_dist[k]

# Determine how many combinations there are to win the race.
the_time = int(the_time)
the_dist = int(the_dist)
win_count = 0
# button_time can't be 0 or time.
for button_time in range(1, the_time):
    speed = button_time
    travel_time = the_time - button_time
    race_dist = speed * travel_time
    if race_dist > the_dist:
        win_count += 1

print(f'Win count: {win_count}')
