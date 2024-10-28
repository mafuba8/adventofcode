#!/usr/bin/python3
# Advent of Code 2023 - Day 14, Part 1
# Benedikt Otto

# Open puzzle file.
lines = []
#with open('example_14.txt') as file:
with open('../inputs/input_14.txt') as file:
    for line in file:
        lines.append(line.strip())


def transpose(pattern):
    """Transpose the pattern, swapping rows and columns."""
    # Assuming we get a rectangular pattern.
    t_col_count = len(pattern)
    t_row_count = len(pattern[0])

    t_pattern = []
    for i in range(t_row_count):
        t_row = ""
        for j in range(t_col_count):
            t_row += pattern[j][i]
        t_pattern.append(t_row)
    return t_pattern


def move(line):
    """Moves all rounded rocks 'O' left until they hit a square rock '#' or the border."""
    while True:
        # Repeatedly replace '.O' with 'O.' until nothing changes anymore.
        new = line.replace('.O', 'O.')
        if new != line:
            line = new
        else:
            break
    return line


# Move all rocks and count their load.
total_load = 0
for col in transpose(lines):
    # After transposing the rocks need to slide left instead of north.
    moved = move(col)

    # Calculate load.
    load = 0
    for row_num, char in enumerate(moved):
        if char == 'O':
            load += len(moved) - row_num  # Rows with less row_num have higher weight.
    total_load += load

print(f'Total load: {total_load}')
