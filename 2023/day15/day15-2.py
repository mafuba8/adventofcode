#!/usr/bin/python3
# Advent of Code 2023 - Day 15, Part 2
# Benedikt Otto

# Open and parse puzzle file.
sequence = []
#with open('example_15.txt') as file:
with open('../inputs/input_15.txt') as file:
    for line in file:
        # The input is one single line.
        sequence = line.strip().split(',')


def hash_algorithm(string):
    """Calculates the hash value of the given string."""
    val = 0
    for char in string:
        val += ord(char)
        val *= 17
        val = val % 256
    return val


def get_index(label, box):
    """Returns the index of the lens with the given label, if it
    exists. If it doesn't exist, returns None."""
    for lens in box:
        if lens[0] == label:
            return box.index(lens)
    return None


# Each box is a list of lenses.
# A lens is a tuple (label, focal_length)
boxes = []
for k in range(256):
    boxes.append([])

for step in sequence:
    if step[-1] == '-':
        # Remove a lens.
        a = step.split('-')
        label = a[0]

        box_num = hash_algorithm(label)
        #print(f'Remove lens with label {label} from box {box_num}.')
        ind = get_index(label, boxes[box_num])
        if ind is not None:
            del boxes[box_num][ind]
    else:
        # Add or replace lens.
        a = step.split('=')
        label = a[0]
        focal_length = a[1]

        box_num = hash_algorithm(label)
        lens = (label, focal_length)
        #print(f'Put {lens} into box {box_num}')
        ind = get_index(label, boxes[box_num])
        if ind is None:
            # Add lens to box with box_num.
            boxes[box_num].append(lens)
        else:
            # Replace the lens of the box in box_num at the same position.
            boxes[box_num][ind] = lens


# Print the final box/lens configuration
for box_num, box in enumerate(boxes):
    if len(box) > 0:
        print(f'{box_num} - {box}')


# Calculate the focusing power of each lens and adds it up.
total_focusing_power = 0
for box_num, box in enumerate(boxes):
    for slot_num, lens in enumerate(box):
        focusing_power = (box_num + 1) * (slot_num + 1) * int(lens[1])
        total_focusing_power += focusing_power

print(f'Total focusing power: {total_focusing_power}')
