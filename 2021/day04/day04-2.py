#!/usr/bin/python3
# Advent of Code 2021 - Day 4, Part 2
# Benedikt Otto
#
import re

# input_file = '../examples/example_4.txt'
input_file = '../inputs/input_4.txt'

# Parse input into lists.
regex = re.compile(r'^\s*(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)$')
board_list = []
with open(input_file) as file:
    lines = file.readlines()
    # Very first row is the list of drawn numbers.
    drawn_numbers = [int(k) for k in lines[0].split(',')]

    # Parse boards into lists.
    board = []
    for line in lines[2:]:
        if line == '\n':
            board_list.append(board)
            board = []
        else:
            search = regex.search(line)
            board.append([int(k) for k in search.groups()])

# Append last board.
board_list.append(board)


def check_bingo(board, num_list):
    """Checks if the given board has a bingo."""
    # Check rows.
    for row in board:
        if all([k in num_list for k in row]):
            return True

    # Check columns.
    for col_num in range(5):
        column = [board[row_num][col_num] for row_num in range(5)]
        if all([k in num_list for k in column]):
            return True

    return False


def sum_unmarked(board, num_list):
    """Returns the sum of all unmarked numbers on the board."""
    unmarked_sum = 0
    for row in board:
        for k in row:
            if k not in num_list:
                unmarked_sum += k
    return unmarked_sum


# Add numbers and remember the boards that had a bingo.
bingo_boards = []
number_list = []
while len(bingo_boards) < len(board_list):
    num = drawn_numbers.pop(0)
    number_list.append(num)
    print(f'Drawn numbers: {number_list}')

    for board_num, board in enumerate(board_list):
        if board not in bingo_boards:
            if check_bingo(board, number_list):
                bingo_boards.append(board)
                print(f' Bingo in board #{board_num + 1}.')

                # Check if this is the last board to have a bingo.
                if len(bingo_boards) == len(board_list):
                    print(f'All boards now have a bingo.')
                    all_bingos = True
                    final_board = board.copy()
                    final_number_list = number_list.copy()

                    print(f' Last board with a bingo: #{board_num + 1}')
                    s = sum_unmarked(board, number_list)
                    print(f' Sum of unmarked numbers: {s}')
                    print(f' Final score: {s * num}')

