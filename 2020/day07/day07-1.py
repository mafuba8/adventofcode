#!/usr/bin/python3
# Advent of Code 2020 - Day 7, Part 1
# Benedikt Otto
#
import re

# input_file = '../examples/example_7.txt'
input_file = '../inputs/input_7.txt'

# Regular expressions for parsing the input.
regex_bag_rule = re.compile(r'^([a-z]+\s[a-z]+)\sbags\scontain\s(.+)\.$')
regex_bag_count = re.compile(r'^(\d+)\s([a-z]+\s[a-z]+)\sbags?$')

# Parse into a dict of rules. Each rule is a list of tuples (count, bag_name).
bag_rules = {}
with open(input_file) as file:
    for line in file.readlines():
        search_bag_rule = regex_bag_rule.search(line)
        rule_bag = search_bag_rule.group(1)
        rule_bag_content = search_bag_rule.group(2).split(', ')

        content_list = []
        for bag in rule_bag_content:
            if bag == 'no other bags':
                pass
            else:
                search_bag_count = regex_bag_count.search(bag)
                content_bag = (int(search_bag_count.group(1)), search_bag_count.group(2))
                content_list.append(content_bag)

        bag_rules[rule_bag] = content_list


def gold_inside(bag_name: str) -> bool:
    """Checks if a shiny gold bag can be stored inside the given bag."""
    # Check if bag itself is shiny gold.
    if bag_name == 'shiny gold':
        return True

    # Check if shiny gold can be inside the bag.
    for content in bag_rules[bag_name]:
        count, bag = content
        if gold_inside(bag):
            return True

    return False


# Run through all bag colors and check if we can store a shiny gold bag inside.
gold_content_count = 0
for bag in bag_rules:
    if gold_inside(bag):
        print(f'A {bag} bag can contain a shiny gold bag.')
        gold_content_count += 1

# Don't count the shiny gold bag itself.
print(f'Number of bag colors that can contain a shiny gold bag: {gold_content_count - 1}.')
