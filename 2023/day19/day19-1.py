#!/usr/bin/python3
# Advent of Code 2023 - Day 19, Part 1
# Benedikt Otto
import re

# Open puzzle file and parse it.
#with open('example_19.txt') as file:
with open('input_19.txt') as file:
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


def build_workflow_function(workflow_rule):
    """Returns a function that does the simple comparison flow
    dictated by the given workflow rule."""
    case_list = workflow_rule.split(',')

    def _func(part):
        (x, m, a, s) = part
        for case in case_list:
            if ':' in case:
                c = case.split(':')
                stm = c[0]
                ret = c[1]
                if eval(stm):
                    return ret
            else:
                ret = case
                return ret
    return _func


# Create workflow as dictionary of functions.
workflows = {}
regex_workflow = re.compile(r'(\w*){(.*)}')
for word in input_workflow:
    search = regex_workflow.search(word)
    workflow_name = search.group(1)
    workflow_rule = search.group(2)

    workflows.setdefault(workflow_name, build_workflow_function(workflow_rule))


# Run each part through the workflows and sort them into A/R lists.
parts_accepted = []
parts_rejected = []
for part in parts:
    workflow_name = 'in'  # First workflow is always the one named 'in'.
    while True:
        workflow = workflows[workflow_name]
        ret = workflow(part)
        match ret:
            case 'A':
                parts_accepted.append(part)
                break
            case 'R':
                parts_rejected.append(part)
                break
            case _:
                workflow_name = ret


# Adding all the numbers of the accepted parts.
total_sum = 0
for part in parts_accepted:
    total_sum += sum(part)

print(f'Total rating of all the accepted parts: {total_sum}.')
