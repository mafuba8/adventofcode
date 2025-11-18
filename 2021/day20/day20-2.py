#!/usr/bin/python3
# Advent of Code 2021 - Day 20, Part 2
# Benedikt Otto
#
# This exercise has a rude twist that only appears in the real input: The enhancement algorithm
# has '#' at index 0, so one enhancement replaces all the unlit pixels outside the picture
# with lit pixels. So we need to keep track whether the surrounding pixels are currently all
# unlit or lit, called the 'default pixel'.

# input_file = '../examples/example_20.txt'
input_file = '../inputs/input_20.txt'

# Parse input.
enhancement_algorithm = []
image_dict = {}
image_default = '.'
with open(input_file) as file:
    first_part = True
    for row_num, line in enumerate(file.readlines()):
        if line == '\n':
            first_part = False
        elif first_part:
            enhancement_algorithm = list(line.strip())
        else:
            # Parse image into dict.
            for col_num, c in enumerate(line.strip()):
                image_dict[(row_num - 2, col_num)] = c


def print_image(i_dict, i_default):
    """Prints the image similar to the examples."""
    x_min = min(xy[0] for xy in i_dict) - 2
    x_max = max(xy[0] for xy in i_dict) + 2
    y_min = min(xy[1] for xy in i_dict) - 2
    y_max = max(xy[1] for xy in i_dict) + 2
    for x in range(x_min, x_max + 1):
        for y in range(y_min, y_max + 1):
            print(i_dict.get((x, y), i_default), end='')
        print()


def find_output_pixel(coord, i_dict, i_default):
    """Determines the pixel state at the coordinate by checking all surrounding pixels
    and applying the enhancement algorithm."""
    x, y = coord
    global enhancement_algorithm
    # Run through all 9 pixels surrounding coord.
    enhancement_binary = ''
    for xy in [(x-1, y-1), (x-1, y), (x-1, y+1), (x, y-1), (x, y), (x, y+1), (x+1, y-1), (x+1, y), (x+1, y+1)]:
        p = i_dict.get(xy, i_default)
        if p == '#':
            enhancement_binary += '1'
        else:
            enhancement_binary += '0'
    idx = int(enhancement_binary, 2)
    return enhancement_algorithm[idx]


def enhance(i_dict, i_default):
    """Applies the enhancement algorithm to the given picture and returns the next picture."""
    new_image = {}
    x_min = min(xy[0] for xy in i_dict) - 1
    x_max = max(xy[0] for xy in i_dict) + 1
    y_min = min(xy[1] for xy in i_dict) - 1
    y_max = max(xy[1] for xy in i_dict) + 1

    # For each pixel, find the enhanced pixel.
    for x in range(x_min, x_max + 1):
        for y in range(y_min, y_max + 1):
            xy = (x, y)
            new_image[xy] = find_output_pixel(xy, i_dict, i_default)

    # Check what to do with the default value (outside the range) by creating a 3x3 grid
    # of default pixels and applying the algorithm to the middle pixel.
    default_dict = {(x, y): i_default for x in range(2) for y in range(2)}
    new_default = find_output_pixel((1, 1), default_dict, i_default)

    return new_image, new_default


# Repeatedly apply the enhancement algorithm to the picture and count the pixels in the final image.
NUM_STEPS = 50
for step in range(NUM_STEPS):
    print(f'=== Step {step + 1}:')
    image_dict, image_default = enhance(image_dict, image_default)

# Count the number of lit pixels.
lit_pixel_coords = [xy for xy in image_dict if image_dict[xy] == '#']
print()
print(f'Number of lit pixels: {len(lit_pixel_coords)}')
