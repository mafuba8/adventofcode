#!/usr/bin/python3
# Advent of Code 2023 - Day 12, Part 2
# Benedikt Otto
import functools
import re

# Open puzzle file.
#with open('example_12.txt') as file:
with open('../inputs/input_12.txt') as file:
    lines = file.readlines()

# Parse puzzle file.
# records = list(tuple(string, pattern))
records = []
regex = re.compile(r'([.?#]*)\s((\d+,)*\d+)')
for line in lines:
    search = regex.search(line)
    string = search.group(1)
    pattern = search.group(2).split(',')

    # Duplicate (fold) the strings and patterns 5 times.
    string = string + '?' + string + '?' + string + '?' + string + '?' + string
    pattern = pattern * 5

    records.append((string, [int(c) for c in pattern]))


@functools.cache
def count_arrangements(string, pattern_tuple):
    """Counts the number of possible arrangements that adhere to the pattern.
    In order to be cached by functools.cache, all inputs need to be hashable, so
    pattern needs to be a tuple, not a list."""
    if len(string) == 0:
        if len(pattern_tuple) > 0:
            return 0  # Empty string but remaining pattern.
        else:
            return 1  # Empty string and no remaining pattern.
    else:
        if len(pattern_tuple) == 0:
            if '#' not in string:
                return 1  # No remaining pattern and no '#' left in string.
            else:
                return 0  # No remaining pattern but '#' left in string.
        else:
            # Both strings and pattern are nonempty.
            c = string[0]
            p = pattern_tuple[0]
            match c:
                case '.':
                    # Remove the leading '.' and recursively check remainder.
                    return count_arrangements(string[1:], pattern_tuple)
                case '?':
                    # Check both cases '?' = '.' and '?' = '#' and add their counts together.
                    return (count_arrangements('.' + string[1:], pattern_tuple)
                            + count_arrangements('#' + string[1:], pattern_tuple))
                case '#':
                    if len(string) < p:
                        return 0  # Not enough characters left to fulfill the pattern.
                    else:
                        # Check the first p characters.
                        if '.' not in string[:p]:
                            rstring = string[p:]
                            # Check the remainder for additional '#'.
                            if len(rstring) > 0:
                                if rstring[0] == '#':
                                    return 0  # More '#' than allowed by the pattern.
                                else:
                                    # If the next symbol is a '?', we need to make sure that it is
                                    # interpreted as a '.', or else the pattern fails.
                                    rstring = '.' + rstring[1:]
                                    return count_arrangements(rstring, pattern_tuple[1:])
                            return count_arrangements(rstring, pattern_tuple[1:])
                        else:
                            return 0  # Not enough '#' or '?' to fulfill the pattern.


total_arrangement_count = 0
for string, pattern in records:
    # Here we need the pattern as a tuple (immutable/hashable):
    pattern_tuple = tuple(pattern)
    arrangement_count = count_arrangements(string, pattern_tuple)

    print(f'{string}, {pattern} - {arrangement_count}')
    total_arrangement_count += arrangement_count

print(f'Total sum of arrangements: {total_arrangement_count}')
