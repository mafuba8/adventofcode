#!/usr/bin/python3
# Advent of Code 2024 - Day 4, Part 1
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


def get_adjacent_tiles(base_tile):
    """Finds all adjacent tiles of base_tile within the word search."""
    possible_adj_tiles = [(base_tile[0] + x, base_tile[1] + y) for x in [-1, 0, 1] for y in [-1, 0, 1]]
    possible_adj_tiles.remove(base_tile)  # above list comprehension adds base_tile itself.

    adjacent_tiles = [t for t in possible_adj_tiles if t in word_search.keys()]
    return adjacent_tiles


# Start at tiles with 'X', then look for adjacent tiles with 'M'.
xmas_count = 0
starting_tiles = [t for t in word_search if word_search[t] == 'X']
for start_tile in starting_tiles:
    for t in get_adjacent_tiles(start_tile):
        if word_search[t] == 'M':
            # Take 4-length strings in the direction of 'XM' and check if they are 'XMAS'.
            direction = (t[0] - start_tile[0], t[1] - start_tile[1])
            string = ''
            for k in range(4):
                tk = (start_tile[0] + k * direction[0], start_tile[1] + k * direction[1])
                string += word_search.get(tk, '')
            if string == 'XMAS':
                print(f'XMAS pattern starting at {start_tile}.')
                xmas_count += 1

print(f'Total number that XMAS appears in the word search: {xmas_count}')
