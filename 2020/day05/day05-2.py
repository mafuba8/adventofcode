#!/usr/bin/python3
# Advent of Code 2020 - Day 5, Part 2
# Benedikt Otto
#

# input_file = '../examples/example_5.txt'
input_file = '../inputs/input_5.txt'

# Parse input into a list of strings.
boarding_pass_list = []
with open(input_file) as file:
    for line in file.readlines():
        boarding_pass_list.append(line.strip())


def find_row(boarding_string):
    lower_limit = 0
    upper_limit = 127
    for c in boarding_string:
        middle = (lower_limit + upper_limit + 1) // 2
        match c:
            case 'F':
                upper_limit = middle
            case 'B':
                lower_limit = middle
        if lower_limit == upper_limit + 1:
            break
    return lower_limit


def find_col(boarding_string):
    lower_limit = 0
    upper_limit = 7
    for c in boarding_string:
        middle = (lower_limit + upper_limit + 1) // 2
        match c:
            case 'R':
                lower_limit = middle
            case 'L':
                upper_limit = middle
        if lower_limit == upper_limit + 1:
            break
    return lower_limit


# Compute all the seat ids and find the highest one.
max_seat_id = 0
seat_id_list = []
for boarding_pass in boarding_pass_list:
    row = find_row(boarding_pass[:7])
    col = find_col(boarding_pass[7:])
    seat_id = row * 8 + col

    max_seat_id = max(seat_id, max_seat_id)
    seat_id_list.append(seat_id)
    print(f'{boarding_pass}: row {row}, col {col}, seat ID {seat_id}')

# Run through all the seat IDs and find the missing one that has existing neighbours.
for seat_id in range(max_seat_id + 1):
    if (seat_id not in seat_id_list
            and seat_id - 1 in seat_id_list
            and seat_id + 1 in seat_id_list):
        print(f'Seat found: {seat_id}')
        break
