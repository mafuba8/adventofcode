#!/usr/bin/python3
# Advent of Code 2024 - Day 2, Part 1
# Benedikt Otto
#

# input_file = '../examples/example_2.txt'
input_file = '../inputs/input_2.txt'

# Parse input into list of reports (lists):
report_list = []
with open(input_file) as file:
    for line in file.readlines():
        l = [int(s) for s in line.strip().split(' ')]
        report_list.append(l)


# Count number of safe reports.
safe_report_count = 0
for report in report_list:
    is_increasing = True
    is_decreasing = True
    # Check for all pairs of consecutive numbers.
    for k in range(len(report) - 1):
        diff = report[k] - report[k + 1]
        if diff <= 0 or diff > 3:
            is_decreasing = False
        if diff > -1 or diff < -3:
            is_increasing = False

    if is_increasing:
        print(f'{report} is safely increasing.')
        safe_report_count += 1
    if is_decreasing:
        print(f'{report} is safely decreasing.')
        safe_report_count += 1

print(f'Number of safe reports: {safe_report_count}')
