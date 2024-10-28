#!/usr/bin/python3
# Advent of Code 2023 - Day 4, Part 1
# Benedikt Otto
import re

# Open puzzle file.
#with open('example_4.txt') as file:
with open('../inputs/input_4.txt') as file:
    lines = file.readlines()


# Parse file into a dictionary
# card_dict = dict( key= Card name, val= tuple(win_nums, have_nums) )
card_dict = {}
re_wspace = re.compile(r'\s+')
for line in lines:
    # Split card name
    card = line.split(':')
    card_name = card[0]
    card_nums = card[1].split('|')

    # Replace several whitespaces with only one.
    card_nums[0] = re_wspace.sub(' ', card_nums[0])
    card_nums[1] = re_wspace.sub(' ', card_nums[1])

    # Split winning and having numbers and put them into the dict.
    win_nums = card_nums[0].strip().split(' ')
    have_nums = card_nums[1].strip().split(' ')
    card_dict.setdefault(card_name, (win_nums, have_nums))


# Determine card_points for each card:
total_points = 0
for card_name in card_dict:
    print(card_name)
    nums = card_dict[card_name]
    have_nums = nums[0]
    win_nums = nums[1]

    win_count = 0
    for num in win_nums:
        if num in have_nums:
            print(f'{num} is a winning number!')
            win_count += 1

    # Each winning number doubles the value of the card, starting at 1.
    if win_count < 1:
        card_points = 0
    else:
        card_points = 2 ** (win_count - 1)

    total_points += card_points
    print(f'{card_name} is worth {card_points} points.')


print('')
print(f'Total card worth: {total_points}')
