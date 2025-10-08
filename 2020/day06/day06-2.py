#!/usr/bin/python3
# Advent of Code 2020 - Day 6, Part 2
# Benedikt Otto
#

# input_file = '../examples/example_6.txt'
input_file = '../inputs/input_6.txt'


# Parse input into list of lists.
group_list = []
with open(input_file) as file:
    group = []
    for line in file.readlines():
        if line == '\n':
            group_list.append(group)
            group = []
        else:
            group.append(line.strip())
    group_list.append(group)


# Count questions that appear in all persons.
total_count = 0
for group in group_list:
    questions = set(group[0])
    for person in group[1:]:
        questions = questions.intersection(set(person))
    print(questions, len(questions))
    total_count += len(questions)

print(f'Count of shared questions: {total_count}')
