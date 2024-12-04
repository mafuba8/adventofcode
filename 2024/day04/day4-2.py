#!/usr/bin/python3
# Advent of Code 2024 - Day 4, Part 2
# Benedikt Otto
#

# input_file = '../examples/example_4.txt'
input_file = '../inputs/input_4.txt'

# Parse into dict(key=xy, val=char).
word_search = {}
with open(input_file) as file:
    for row_num, row in enumerate(file.readlines()):
        for col_num, char in enumerate(row.strip()):
            word_search.setdefault((row_num, col_num), char)


# Find all tiles with 'A', then look at the two diagonals through 'A'.
xmas_count = 0
starting_tiles = [t for t in word_search if word_search[t] == 'A']
for start_tile in starting_tiles:
    # UL . UR
    #  . A .
    # DL . DR
    UL = (start_tile[0] - 1, start_tile[1] - 1)
    UR = (start_tile[0] - 1, start_tile[1] + 1)
    DL = (start_tile[0] + 1, start_tile[1] - 1)
    DR = (start_tile[0] + 1, start_tile[1] + 1)
    diagonal1 = word_search.get(UL, '') + 'A' + word_search.get(DR, '')
    diagonal2 = word_search.get(UR, '') + 'A' + word_search.get(DL, '')

    # Check if both diagonals have a 'MAS' pattern.
    if diagonal1 in ['MAS', 'SAM'] and diagonal2 in ['MAS', 'SAM']:
        print(f'X-MAS pattern around {start_tile}.')
        xmas_count += 1

print(f'Total number of X-MAS patterns: {xmas_count}')
