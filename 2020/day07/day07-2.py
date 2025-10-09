#!/usr/bin/python3
# Advent of Code 2020 - Day 7, Part 2
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


def count_sub_bags(bag_name: str) -> int:
    """Counts how many bags are inside the given bag."""
    # Recursion end.
    content_list = bag_rules[bag_name]

    sub_bag_count = 0
    if content_list:
        sub_bag_count = 0
        for content in content_list:
            count, bag = content
            sub_bag_count += count + count * count_sub_bags(bag)
    return sub_bag_count


# Check how many bags are inside the shiny gold bag.
print(f'Total number of bags inside a single shiny gold bag: {count_sub_bags('shiny gold')}')
