#!/usr/bin/python3
# Advent of Code 2023 - Day 4, Part 2
# Benedikt Otto
import re

# Open puzzle file.
#with open('example_4.txt') as file:
with open('input_4.txt') as file:
    lines = file.readlines()


# Parse file into a list
# card_list = list of list(count, win_nums, have_nums)
card_list = []
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

    card_list.append([1, win_nums, have_nums])


# Run through all the cards and count them including their copies.
total_number_of_cards = 0
for card_number, card in enumerate(card_list):
    card_count = card[0]
    win_nums = card[1]
    have_nums = card[2]

    # Count how many winning numbers this card has.
    win_count = 0
    for num in win_nums:
        if num in have_nums:
            win_count += 1

    # The current card doesn't get copied, so just add them to the total number of cards.
    total_number_of_cards += card_count

    print(f'Card {card_number} has {win_count} matching numbers. There are {card_count} copies if it.')

    # Add one copy for each following card (if it exists) AND each copy of the current card.
    for i in range(win_count):
        copy_number = card_number + 1 + i
        if copy_number < len(card_list):
            print(f'We get {card_count} more copies of card {card_number + 1 + i}')
            card_list[card_number + 1 + i][0] += card_count


print('')
print(f'Total number of cards: {total_number_of_cards}')
