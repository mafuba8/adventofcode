#!/usr/bin/python3
# Advent of Code 2023 - Day 7, Part 2
# Benedikt Otto
import itertools
from operator import itemgetter
from functools import cmp_to_key

# Dictionary with values of cards.
value_dict = {'T': 10, 'Q': 12, 'K': 13, 'A': 14, 'J': 1}
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
    and the highest involved card value.
    """
    # Sort hand descending by values:
    values = sorted(hand, reverse=True)

    # Count multiples of the same card.
    triples = []
    pairs = []
    for card, group in itertools.groupby(values):
        count = sum(1 for p in group)
        if count == 5:
            return 6, card  # Five of a kind
        elif count == 4:
            return 5, card  # Four of a kind
        elif count == 2:
            pairs.append(card)
        elif count == 3:
            triples.append(card)

    if triples:
        if pairs:
            return 4, max(pairs[0], triples[0])  # Full house
        else:
            return 3, triples[0]  # Three of a kind

    if pairs:
        if len(pairs) >= 2:
            return 2, max(pairs[0], pairs[1])  # Two pairs
        else:
            return 1, pairs[0]  # One pair

    return 0, max(values)  # High card


def compare_draws(draw1, draw2):
    """Comparison function for two draws with the same evaluation.
    Returns
        -1 if draw1 < draw2
        0  if draw1 = draw2
        +1 if draw1 > draw2
    """
    # Note that the original cards (draw[0]) are compared,
    # and NOT the replaced cards (draw[1])!
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
    return compare_draws((cards1[1:], draw1[1], draw1[2], draw1[3]), (cards2[1:], draw2[1], draw2[2], draw2[3]))


# Evaluate each draw - ignoring the Joker's special role for now,
# but remembering the highest involved card
eval_list = []
for draw in draws:
    cards, bid = draw
    eval, high_card = eval_hand(cards)
    eval_list.append((cards, eval, high_card, bid))


# Replace the Joker with the best suited card.
replaced = []
for cards, eval, high_card, bid in eval_list:
    repl_cards = []
    for c in cards:
        if c != 1:
            # Non-Jokers stay the same
            repl_cards.append(c)
        else:
            if high_card == 1:
                # If the highest involving card itself is a Joker, then we
                # need to replace it with the highest occurring card.
                repl_cards.append(max(cards))
            else:
                # If the highest involving card is not a Joker, then
                # just replace the Joker with the high_card.
                repl_cards.append(high_card)

    replaced.append((cards, repl_cards, eval, high_card, bid))


# Evaluate cards again with Jokers accounted for.
eval_list_replaced = []
for cards, repl_cards, eval, high_card, bid in replaced:
    ranking2, high_card2 = eval_hand(repl_cards)
    eval_list_replaced.append((cards, repl_cards, bid, ranking2))


# Sort & group by rank and tiebreakers.
result_list = []
eval_list_replaced = sorted(eval_list_replaced, key=itemgetter(3), reverse=True)
for eval, group in itertools.groupby(eval_list_replaced, key=itemgetter(3)):
    print(f'Ranking {eval}:')

    # Sort hands within the same rank using the comparison function.
    # Note that the original cards are compared for tiebreakers, NOT the replaced cards!
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
for hand, repl_hand, bid, eval in result_list:
    print(f'Rank {rank}: {hand} ({bid})')
    winnings = rank * bid
    total_winnings += winnings
    rank += 1

print(f'Total winnings: {total_winnings}')
