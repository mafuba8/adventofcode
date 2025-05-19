#!/usr/bin/python3
# Advent of Code 2021 - Day 13, Part 1
# Benedikt Otto
#

# input_file = '../examples/example_13.txt'
input_file = '../inputs/input_13.txt'

# Parse input into lists of coordinates and folding instructions.
input_paper = []
folding_instructions = []
with open(input_file) as file:
    for line in file.readlines():
        if 'fold along' in line:
            folding_instructions.append(line.strip().split('fold along ')[1])
        elif ',' in line:
            x, y = line.strip().split(',')
            input_paper.append((int(x), int(y)))


def print_paper(paper):
    """Print the paper dots as in the example."""
    x_max = max([x for (x, _) in paper])
    y_max = max([y for (_, y) in paper])
    for y in range(y_max + 1):
        for x in range(x_max + 1):
            if (x, y) in paper:
                print('#', end='')
            else:
                print('.', end='')
        print()


def fold_along_x(paper, fold_x):
    """Returns the paper folded at the vertical along fold_x as a list of dots."""
    new_paper = []
    # Assuming that the fold is always in the middle.
    y_max = max([y for (_, y) in paper])
    for x in range(fold_x):
        for y in range(y_max + 1):
            if (x, y) in paper or (2 * fold_x - x, y) in paper:
                new_paper.append((x, y))
    return new_paper


def fold_along_y(paper, fold_y):
    """Returns the paper folded at the horizontal along fold_y as a list of dots."""
    new_paper = []
    # Assuming that the fold is always in the middle.
    x_max = max([x for (x, _) in paper])
    for x in range(x_max + 1):
        for y in range(fold_y):
            if (x, y) in paper or (x, 2 * fold_y - y) in paper:
                new_paper.append((x, y))
    return new_paper


def fold_by_instruction(paper, instruction):
    """Fold according to the instruction 'x=N' or 'y=M'."""
    if 'x=' in instruction:
        fold_x = int(instruction.split('x=')[1])
        return fold_along_x(paper, fold_x)
    elif 'y=' in instruction:
        fold_y = int(instruction.split('y=')[1])
        return fold_along_y(paper, fold_y)
    return paper


# Fold according to the first instruction.
paper = input_paper
for instruction in [folding_instructions[0]]:
    paper = fold_by_instruction(paper, instruction)

# Count the number of dots.
print(f'Number of dots after the first fold: {len(paper)}')
