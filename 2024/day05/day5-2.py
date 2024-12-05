#!/usr/bin/python3
# Advent of Code 2024 - Day 5, Part 2
# Benedikt Otto
#

# input_file = '../examples/example_5.txt'
input_file = '../inputs/input_5.txt'

# Parse input into
#  rule dicts: key=page, val=[pages before/after]
#  list of updates (list of pages)
#
rule_before = {}
rule_after = {}
update_list = []
with open(input_file) as file:
    for line in file.readlines():
        if line == '\n':
            continue
        if '|' in line:
            # Rule section.
            x, y = line.strip().split('|')
            rule_after.setdefault(x, [])
            rule_after[x].append(y)
            rule_before.setdefault(y, [])
            rule_before[y].append(x)
        else:
            # Updates (pages).
            update_list.append(line.strip().split(','))


def find_inversions(update):
    """Checks the pages of the given update, returning a list of their inversions."""
    inversion_list = []
    for page_id, page in enumerate(update):
        pages_before = update[:page_id]
        pages_after = update[page_id + 1:]
        for p in pages_before:
            if p not in rule_before.get(page, []):
                inversion_list.append((p, page))
        for p in pages_after:
            if p not in rule_after.get(page, []):
                inversion_list.append((p, page))
    return inversion_list


# Get list of incorrectly ordered updates.
incorrect_update_list = [u for u in update_list if len(find_inversions(u)) > 0]

# Re-arrange incorrectly ordered updates by removing inversions.
for update in incorrect_update_list:
    while len(find_inversions(update)) > 0:
        # Remove the first inversion by swapping their elements.
        x, y = find_inversions(update)[0]
        i, j = update.index(x), update.index(y)
        update[i], update[j] = update[j], update[i]


# Sum up the middle page numbers of the re-ordered updates.
middle_page_sum = 0
for update in incorrect_update_list:
    i = len(update) // 2
    middle_page_sum += int(update[i])

print(f'Total middle sum of re-arranged updates: {middle_page_sum}')
