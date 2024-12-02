#!/usr/bin/python3
# Advent of Code 2024 - Day 2, Part 2
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


def safely_decreasing(rep):
    """Checks if the levels are safely decreasing."""
    is_decreasing = True
    for num in range(len(rep) - 1):
        diff = rep[num] - rep[num + 1]
        if diff <= 0 or diff > 3:
            is_decreasing = False
    return is_decreasing


def safely_increasing(rep):
    """Checks if the levels are safely increasing."""
    is_increasing = True
    for num in range(len(rep) - 1):
        diff = rep[num] - rep[num + 1]
        if diff > -1 or diff < -3:
            is_increasing = False
    return is_increasing


safe_report_count = 0
for report in report_list:
    if safely_decreasing(report):
        print(f'{report} is safely decreasing.')
        safe_report_count += 1
    else:
        # Check if the removal of one number makes it safely decreasing.
        for k in range(len(report)):
            report_modified = report.copy()
            del report_modified[k]
            if safely_decreasing(report_modified):
                print(f'after removal of {report[k]}, {report} is safely decreasing.')
                safe_report_count += 1
                break

    if safely_increasing(report):
        print(f'{report} is safely increasing.')
        safe_report_count += 1
    else:
        # Check if the removal of one number makes it safely increasing.
        for k in range(len(report)):
            report_modified = report.copy()
            del report_modified[k]
            if safely_increasing(report_modified):
                print(f'after removal of {report[k]}, {report} is safely increasing')
                safe_report_count += 1
                break

print(f'Number of safe reports: {safe_report_count}')
