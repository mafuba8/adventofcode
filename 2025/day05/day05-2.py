#!/usr/bin/python3
# Advent of Code 2025 - Day 5, Part 2
# Benedikt Otto
#

# INPUT_FILE = '../examples/example_05.txt'
INPUT_FILE = '../inputs/input_05.txt'

# Parse fresh ingredient ranges into a list of tuples. (ignore the second part).
fresh_ingredient_ranges = []
with open(INPUT_FILE) as file:
    first_part = True
    for line in file.readlines():
        if line == '\n':
            break
        else:
            fresh_from, fresh_to = line.strip().split('-')
            t = (int(fresh_from), int(fresh_to))
            fresh_ingredient_ranges.append(t)


def intersect(range_a: tuple[int, int], range_b: tuple[int, int]) -> tuple[int, int]|None:
    """Returns the intersection of the two given intervals, or None if there is no intersection."""
    ra_min, ra_max = range_a
    rb_min, rb_max = range_b

    i_min = max(ra_min, rb_min)
    i_max = min(ra_max, rb_max)

    if i_min <= i_max:
        return i_min, i_max
    else:
        return None

def ingredient_count(range_a: tuple[int, int]) -> int:
    """Returns the number of ingredients in the given interval."""
    ra_min, ra_max = range_a
    # These ranges are inclusive!
    return ra_max - ra_min + 1


# Get the size of the union of all fresh ingredient intervals by inclusion-exclusion principle.
positive_intervals = []  # Their sizes are added to the total.
negative_intervals = []  # Their sizes are subtracted from the total.
for fresh_interval in fresh_ingredient_ranges:
    new_pos_intervals = [fresh_interval]
    new_neg_intervals = []

    # Add intersections with all positive intervals to negatives to avoid overcounting.
    for interval in positive_intervals:
        i = intersect(interval, fresh_interval)
        if i is not None:
            new_neg_intervals.append(i)
    # Add intersections with all negative intervals to positives to avoid undercounting.
    for interval in negative_intervals:
        i = intersect(interval, fresh_interval)
        if i is not None:
            new_pos_intervals.append(i)

    positive_intervals += new_pos_intervals
    negative_intervals += new_neg_intervals

# Count the ingredients in the union.
total_fresh_count = 0
for interval in positive_intervals:
    total_fresh_count += ingredient_count(interval)
for interval in negative_intervals:
    total_fresh_count -= ingredient_count(interval)

print(f'A total of {total_fresh_count} ingredient IDs are considered to be fresh.')
