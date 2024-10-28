#!/usr/bin/python3
# Advent of Code 2023 - Day 7, Part 1
# Benedikt Otto
import itertools
from operator import itemgetter
from functools import cmp_to_key

# Dictionary with values of cards.
value_dict = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14, }
value_dict.update((str(x), x) for x in range(2, 10))

# Open puzzle file.
#with open('example_7.txt') as file:
with open('../inputs/input_7.txt') as file:
    lines = file.readlines()

# Build list of draws and convert card letters to their values.
# draws = list[ tuples(cards, bid) ]
draws = []
for line in lines:
    t = line.split(' ')
    # cards = list[ints]
    cards = [value_dict[c] for c in t[0]]
    bid = int(t[1].strip())
    draws.append((cards, bid))


def eval_hand(hand):
    """Return evaluation of a hand:
    0 - High card
    1 - One pair
    2 - Two pair
    3 - Three of a kind
    4 - Full House
    5 - Four of a kind
    6 - Five of a kind
    """
    # Sort hand descending by values:
    values = sorted(hand, reverse=True)

    # Count multiples of the same card.
    triples = []
    pairs = []
    for card, group in itertools.groupby(values):
        count = sum(1 for p in group)
        if count == 5:
            return 6  # Five of a kind
        elif count == 4:
            return 5  # Four of a kind
        elif count == 2:
            pairs.append(card)
        elif count == 3:
            triples.append(card)

    if triples:
        if pairs:
            return 4  # Full house
        else:
            return 3  # Three of a kind

    if pairs:
        if len(pairs) >= 2:
            return 2  # Two pairs
        else:
            return 1  # One pair

    return 0  # High card


def compare_draws(draw1, draw2):
    """Comparison function for two draws with the same evaluation.
    Returns
        -1 if draw1 < draw2
        0  if draw1 = draw2
        +1 if draw1 > draw2.
    """
    cards1 = draw1[0]
    cards2 = draw2[0]
    if len(cards1) == 0:
        return 0  # Empty hands have the same rank

    # Compare the first card.
    if cards1[0] > cards2[0]:
        return 1
    elif cards1[0] < cards2[0]:
        return -1

    # If the first card is the same, recursively compare the remaining cards.
    return compare_draws((cards1[1:], draw1[1], draw1[2]), (cards2[1:], draw2[1], draw2[2]))


# Evaluate each draw.
eval_list = []
for draw in draws:
    cards, bid = draw
    eval = eval_hand(cards)
    eval_list.append((cards, bid, eval))


# Sort & group by rank and tiebreakers.
result_list = []
eval_list = sorted(eval_list, key=itemgetter(2), reverse=True)
for eval, group in itertools.groupby(eval_list, key=itemgetter(2)):
    print(f'Evaluation {eval}:')

    # Sort hands within the same rank using the comparison function:
    sorted_same_rank = sorted(group, key=cmp_to_key(compare_draws), reverse=True)
    print(sorted_same_rank)

    result_list += sorted_same_rank


# Reverse result list it so that the lowest rank is at the top.
result_list.reverse()

# Calculate winnings from ranks and bids:
print('---')
print('Results: (Higher rank = better)')
rank = 1
total_winnings = 0
for hand, bid, eval in result_list:
    print(f'Rank {rank}: {hand} (Bid: {bid})')
    winnings = rank * bid
    total_winnings += winnings
    rank += 1

print(f'Total winnings: {total_winnings}')
