#!/usr/bin/python3
# Advent of Code 2023 - Day 19, Part 2
# Benedikt Otto
import re

# Open puzzle file and parse it.
#with open('example_19.txt') as file:
with open('../inputs/input_19.txt') as file:
    input = file.read().split('\n\n')
    input_workflow = input[0].strip().split('\n')
    input_parts = input[1].strip().split('\n')


# Create parts set where each part is a tuple (x, m, a, s):
parts = set()
regex_parts = re.compile(r'{x=(\d+),m=(\d+),a=(\d+),s=(\d+)}')
for word in input_parts:
    search = regex_parts.search(word)
    x_val = int(search.group(1))
    m_val = int(search.group(2))
    a_val = int(search.group(3))
    s_val = int(search.group(4))
    parts.add((x_val, m_val, a_val, s_val))


# Create dictionary of workflows indexed by their name.
workflows = {}
regex_workflow = re.compile(r'(\w*){(.*)}')
regex_rule = re.compile(r'([xmas])([<>])(\d+):(\w+)')
for word in input_workflow:
    search = regex_workflow.search(word)
    workflow_name = search.group(1)
    workflow_rule = search.group(2)

    # Here a workflow is a list of tuples (var, symbol, limit, ret), that represent
    # each rule, e.g.
    # 'a<2006:qkq' => ('a', '<', 2006, 'qkq')
    workflow = []
    case_list = workflow_rule.split(',')
    for case in case_list:
        if ':' in case:
            s = regex_rule.search(case)
            var = s.group(1)
            symbol = s.group(2)
            limit = int(s.group(3))
            ret = s.group(4)
        else:
            # Default case at the end of each set of rules.
            var = None
            symbol = None
            limit = None
            ret = case
        workflow.append((var, symbol, limit, ret))
    workflows.setdefault(workflow_name, workflow)


# We represent intervals as tuples (lower, higher). Intervals are thought as inclusive
# so the interval [2, 5] contains the four numbers 2, 3, 4 and 5.
def partition(interval, symbol, limit):
    """Divides the interval into two smaller intervals where the first interval
     int_good fulfills the condition <symbol> <limit> and the second interval
     int_bad doesn't fulfill the condition, e.g.
        partition((1, 4000), '<', 1351) == (1, 1350), (1351, 4000).
    Empty intervals are returned as None.
    """
    (int_lower, int_upper) = interval
    if int_lower <= limit <= int_upper:  #
        if symbol == '<':
            int_good = (min(int_lower, limit), min(limit - 1, int_upper))
            int_bad = (max(int_lower, limit), max(limit, int_upper))
        if symbol == '>':
            int_good = (max(int_lower, limit + 1), max(limit, int_upper))
            int_bad = (min(int_lower, limit), min(limit, int_upper))

        # Cases with boundary points produce things like (2001, 2000). Return None instead.
        if int_bad[0] > int_bad[1]:
            int_bad = None
        if int_good[0] > int_good[1]:
            int_good = None

    else:
        # Cases where limit is outside of interval. Here one resulting interval is always empty.
        if limit > int_upper:
            if symbol == '<':
                int_good = interval
                int_bad = None
            if symbol == '>':
                int_good = None
                int_bad = interval
        if limit < int_lower:
            if symbol == '<':
                int_good = None
                int_bad = interval
            if symbol == '>':
                int_good = interval
                int_bad = None

    return int_good, int_bad


# A 'part range' is a tuple containing intervals for all four variables x/m/a/s.
# e.g. ((1, 4000), (1, 4000), (1, 4000), (1, 4000)).
def find_accepted(x_range, m_range, a_range, s_range, workflow_name):
    """Returns a list of all possible ranges of parts that end up getting accepted ('A') when
    the first applied workflow to it is workflow_name."""
    list_accepted = []
    # End of the recursion.
    if workflow_name == 'A':
        return [(x_range, m_range, a_range, s_range)]
    if workflow_name == 'R':
        return []

    # Apply the rules of the given workflow and partition the sets in those, which fulfill the
    # rule and those which don't fulfill them. Then recursively find the accepted list of each part.
    workflow = workflows[workflow_name]
    for rule in workflow:
        (var, symbol, limit, ret) = rule
        match var:  # Only partition the interval at x/m/a/s and copy the rest of the ranges.
            case 'x':
                int_good, int_bad = partition(x_range, symbol, limit)
                list_accepted += find_accepted(int_good, m_range, a_range, s_range, ret)
                x_range = int_bad
            case 'm':
                int_good, int_bad = partition(m_range, symbol, limit)
                list_accepted += find_accepted(x_range, int_good, a_range, s_range, ret)
                m_range = int_bad
            case 'a':
                int_good, int_bad = partition(a_range, symbol, limit)
                list_accepted += find_accepted(x_range, m_range, int_good, s_range, ret)
                a_range = int_bad
            case 's':
                int_good, int_bad = partition(s_range, symbol, limit)
                list_accepted += find_accepted(x_range, m_range, a_range, int_good, ret)
                s_range = int_bad
            case None:  # Default case of the workflow, which is always the last rule.
                list_accepted += (find_accepted(x_range, m_range, a_range, s_range, ret))
    return list_accepted


# Find list of all accepted ranges with starting workflow 'in' and count them.
accepted_ranges = find_accepted((1, 4000), (1, 4000), (1, 4000), (1, 4000), 'in')
total_count = 0
for accepted_range in accepted_ranges:
    count = 1
    # Since partition produces disjoint sets, we can just multiply their numbers.
    for range in accepted_range:
        count *= range[1] - range[0] + 1
    total_count += count

print(f'Total count of distinct combinations that will be accepted: {total_count}')
