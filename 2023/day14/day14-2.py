#!/usr/bin/python3
# Advent of Code 2023 - Day 14, Part 2
# Benedikt Otto

# Open puzzle file.
lines = []
#with open('example_14.txt') as file:
with open('../inputs/input_14.txt') as file:
    for line in file:
        lines.append(line.strip())


def transpose(p):
    """Transpose the pattern, swapping rows and columns."""
    # Assuming we get a rectangular pattern.
    t_col_count = len(p)
    t_row_count = len(p[0])

    t_pattern = []
    for i in range(t_row_count):
        t_row = ""
        for j in range(t_col_count):
            t_row += p[j][i]
        t_pattern.append(t_row)
    return t_pattern


def move_left(li):
    """Moves all rounded rocks 'O' left until they hit a square rock '#' or the border."""
    while True:
        # Repeatedly replace '.O' with 'O.' until nothing changes anymore.
        new = li.replace('.O', 'O.')
        if new != li:
            li = new
        else:
            break
    return li


def move_right(li):
    """Moves all rounded rocks 'O' right until they hit a square rock '#' or the border."""
    while True:
        # Repeatedly replace 'O.' with '.O' until nothing changes anymore.
        new = li.replace('O.', '.O')
        if new != li:
            li = new
        else:
            break
    return li


def tilt_west(p):
    """Returns the pattern that you get after tilting p west."""
    new_p = []
    for li in p:
        new_p.append(move_left(li))
    return new_p


def tilt_east(p):
    """Returns the pattern that you get after tilting p east."""
    new_p = []
    for li in pattern:
        new_p.append(move_right(li))
    return new_p


def tilt_north(p):
    """Returns the pattern that you get after tilting p north."""
    new_p = []
    # We use the right/left methods on the transposed pattern.
    for li in transpose(p):
        new_p.append(move_left(li))
    return transpose(new_p)


def tilt_south(p):
    """Returns the pattern that you get after tilting p south."""
    new_p = []
    # We use the right/left methods on the transposed pattern.
    for line in transpose(p):
        new_p.append(move_right(line))
    return transpose(new_p)


cycles = 1_000_000_000
# Run the pattern through the cycles, remembering the previous results to find the point where it repeats.
cache = []
repeat_num = 0
num_patterns = 0
pattern = lines
for k in range(1, cycles + 1):
    # One whole cycle.
    pattern = tilt_north(pattern)
    pattern = tilt_west(pattern)
    pattern = tilt_south(pattern)
    pattern = tilt_east(pattern)
    p = pattern
    if p in cache:
        # Total number of different patterns.
        num_patterns = k
        # Pattern number, after which it starts repeating.
        repeat_num = cache.index(p) + 1
        break
    cache.append(p)

# Since it starts repeating after repeat_num cycles, we can calculate the
pattern_cycle_length = num_patterns - repeat_num
print(f'Total num of patterns: {num_patterns}')
print(f'Number of cycles before it starts repeating: {repeat_num}')
print(f'Cycle length: {pattern_cycle_length}')

# Since it starts repeating after repeat_num cycles, we can calculate which cycle the
# billionth cycle is equal to and calculate its load.
#
# Since the cycle starts after repeat_num cycles, we need to subtract it first, then
# calculate modulo cycle length and then re-add the repeat_num translation.
pattern_spot = ((cycles - repeat_num) % pattern_cycle_length) + repeat_num
print(f'The pattern at cycle {cycles} should be the same as pattern at cycle {pattern_spot}.')

# And we already computed that one, so it is in the cache at position - 1.
result = cache[pattern_spot - 1]

# Count the load of result.
total_load = 0
for row_num, row in enumerate(result):
    row_load = 0
    for col_num, char in enumerate(row):
        if char == 'O':
            row_load += len(result) - row_num
    total_load += row_load
    print(f'{row_num}: {row_load}')

print(f'Total load: {total_load}')
