#!/usr/bin/python3
# Advent of Code 2021 - Day 18, Part 1
# Benedikt Otto
#
# The problem is accessing the 'left' and 'right' number on the 'explode' operation.
# So we could try to implement these pairs with their depth.
# Depth can be found by counting brackets [ ]
#
import math

# input_file = '../examples/example_18.txt'
input_file = '../inputs/input_18.txt'

def parse_snailfish_number(string):
    """Parses the given string into our representation of a snailfish number,
    which is a list of tuples (number, depth)."""
    snailfish = []
    # Depth can be found by counting brackets (outer bracket = depth 0).
    depth = -1
    for c in string:
        match c:
            case '[':
                depth += 1
            case ']':
                depth -= 1
            case ',':
                continue
            case _:  # this should always be a digit.
                p = (int(c), depth)
                snailfish.append(p)
    return snailfish


# Parse input into list of snailfish numbers.
sf_list = []
with open(input_file) as file:
    for line in file.readlines():
        sf = parse_snailfish_number(line.strip())
        sf_list.append(sf)


def add(snailfish1, snailfish2):
    result = []
    for p in snailfish1:
        result.append((p[0], p[1] + 1))
    for p in snailfish2:
        result.append((p[0], p[1] + 1))
    return result


def explode(snailfish):
    """Explodes the given snailfish number in-place. Returns if any pair has been exploded."""
    length = len(snailfish) - 1
    for idx in range(length):
        val1, depth1 = snailfish[idx]
        val2, depth2 = snailfish[idx+1]
        if depth1 >= 4 and depth2 >= 4:
            # Explode pair.
            if idx > 0:
                left = snailfish[idx-1]
                new_left = (left[0] + val1, left[1])
                snailfish[idx-1] = new_left

            # Remove the left part of the pair and put in the resulting 0.
            snailfish[idx] = (0, 3)

            if idx < length - 1:
                right = snailfish[idx+2]
                new_right = (right[0] + val2, right[1])
                snailfish[idx+2] = new_right
            del snailfish[idx+1]
            return True  # only explode leftmost pair.
    return False


def split(snailfish):
    """Splits the given snailfish number in-place. Returns if any number has been split."""
    for idx in range(len(snailfish)):
        val, depth = snailfish[idx]
        if val > 9:
            num_left = (math.floor(val / 2), depth + 1)
            num_right = (math.ceil(val / 2), depth + 1)
            del snailfish[idx]
            snailfish.insert(idx, num_right)
            snailfish.insert(idx, num_left)
            return True  # only split leftmost number.
    return False


def reduce(snailfish):
    """Reduces the given snailfish number and returns the new number."""
    sf = snailfish.copy()
    while explode(sf) or split(sf):
        pass
    return sf


def magnitude(snailfish):
    """Calculates the magnitude of a given snailfish number."""
    # To calculate the magnitude, we convert it into a tree (recursive 2-element list).
    def flat2tree(flat):
        d = flat.copy()
        def grab(depth):
            if d[0][1] == depth:
                return d.pop(0)[0]
            else:
                return [grab(depth + 1), grab(depth + 1)]
        return grab(depth=-1)

    def mag(tree):
        if isinstance(tree, int):
            return tree
        else:
            return 3 * mag(tree[0]) + 2 * mag(tree[1])

    return mag(flat2tree(snailfish))


# Add up all the snailfish numbers.
result = sf_list[0]
for sf in sf_list[1:]:
    result = add(result, sf)
    result = reduce(result)


print('Reduced sum of all the snailfish numbers:')
print(result)
print(f'Magnitude: {magnitude(result)}')
