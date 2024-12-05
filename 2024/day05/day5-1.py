#!/usr/bin/python3
# Advent of Code 2024 - Day 5, Part 1
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


# Find the correctly ordered updates and sum up their middle page numbers.
middle_page_sum = 0
for update in update_list:
    in_right_order = True
    # Check the rules for each page.
    for page_id, page in enumerate(update):
        pages_before = update[:page_id]
        for p in pages_before:
            if p not in rule_before.get(page, []):
                in_right_order = False
        pages_after = update[page_id + 1:]
        for p in pages_after:
            if p not in rule_after.get(page, []):
                in_right_order = False

    if in_right_order:
        i = len(update) // 2
        middle_page_sum += int(update[i])

print(f'Total middle sum of correctly ordered updates: {middle_page_sum}')
