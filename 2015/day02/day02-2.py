#!/usr/bin/python3
# Advent of Code 2015 - Day 2, Part 2
# Benedikt Otto
#

INPUT_FILE = '../inputs/input_02.txt'

# Parse into a list of tuples (l, w, h).
box_list = []
with open(INPUT_FILE) as file:
    for line in file.readlines():
        b = line.strip().split('x')
        b = tuple(map(int, b))
        box_list.append(b)


def paper_area(box):
    """Calculate the area of paper needed to wrap a box."""
    l, w, h = box
    # Surface area of the box.
    paper = 2*l*w + 2*w*h + 2*h*l
    # Additional paper as slack.
    paper += min(l*w, w*h, h*l)
    return paper


def ribbon_length(box):
    """Calculates the length of ribbon needed to wrap a box."""
    l, w, h = box
    # Find the two shortest side lengths.
    tmp = [l, w, h]
    tmp.sort()
    ribbon = 2 * tmp[0] + 2 * tmp[1]
    # Calculate the length of the bow.
    ribbon += l * w * h
    return ribbon


# Add up all the paper needed.
total_paper = 0
total_ribbon = 0
for b in box_list:
    total_paper += paper_area(b)
    total_ribbon += ribbon_length(b)

print(f'Total wrapping paper needed: {total_paper} square feet.')
print(f'Total ribbon needed: {total_ribbon} feet.')
