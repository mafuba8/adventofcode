#!/usr/bin/python3
# Advent of Code 2023 - Day 13, Part 1
# Benedikt Otto

# Open puzzle file.
#with open('example_13.txt') as file:
with open('input_13.txt') as file:
    content = file.read()
    blocks = content.split('\n\n')

del blocks[-1]

# Parse patterns
# Pattern = dict(key=(x, y), val=symbol)
pattern_list = []
for block in blocks:
    pattern = {}
    block_rows = block.split('\n')
    for row_num, row in enumerate(block_rows):
        for col_num, char in enumerate(row):
            pattern.setdefault((row_num, col_num), char)
    pattern_list.append(pattern)


def find_vert_symmetry(pattern, col):
    """Checks if there is a vertical symmetry around the given column."""
    pattern_height = max([t[0] for t in pattern.keys()]) + 1
    pattern_width = max([t[1] for t in pattern.keys()]) + 1

    # Run through all the rows and compare the symbols left/right of it.
    for k in range(col + 1):
        for row in range(pattern_height):
            if col - k < 0 or col + k + 1 >= pattern_width:
                break

            if pattern[(row, col - k)] == pattern[(row, col + k + 1)]:
                continue
            else:
                return False
    return True


def find_horz_symmetry(pattern, row):
    """Checks if there is a horizontal symmetry around the given row."""
    pattern_height = max([t[0] for t in pattern.keys()]) + 1
    pattern_width = max([t[1] for t in pattern.keys()]) + 1

    # Run through all the columns and compare the symbols over/under it.
    for k in range(row + 1):
        for col in range(pattern_width):
            if row - k < 0 or row + k + 1 >= pattern_height:
                break

            if pattern[(row - k, col)] == pattern[(row + k + 1, col)]:
                continue
            else:
                return False
    return True


# Find symmetries and count their rows.
total_sum = 0
for pat_num, pattern in enumerate(pattern_list):
    pattern_height = max([t[0] for t in pattern.keys()]) + 1
    pattern_width = max([t[1] for t in pattern.keys()]) + 1

    print(f'Pattern number {pat_num}:')
    # Check for vertical symmetries.
    for sym_col in range(pattern_width - 1):
        if find_vert_symmetry(pattern, sym_col):
            print(f'Vertical symmetry at sym column {sym_col} ({sym_col + 1} columns left of it).')
            total_sum += sym_col + 1
            break


    # Check for horizontal symmetries:
    for sym_row in range(pattern_height - 1):
        if find_horz_symmetry(pattern, sym_row):
            print(f'Horizontal symmetry at row {sym_row} ({sym_row + 1} rows on top of it).')
            total_sum += 100 * (sym_row + 1)
            break

print(f'Total sum: {total_sum}.')
