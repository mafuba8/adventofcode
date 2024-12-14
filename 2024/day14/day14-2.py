#!/usr/bin/python3
# Advent of Code 2024 - Day 14, Part 1
# Benedikt Otto
#
import re

# input_file = '../examples/example_14.txt'
input_file = '../inputs/input_14.txt'

# Area size and number of simulated steps.
# AREA_WIDTH = 11
# AREA_HEIGHT = 7
AREA_WIDTH = 101
AREA_HEIGHT = 103


class Robot:
    """Definition of a robot, with the move method."""
    def __init__(self, pos_x, pos_y, vel_x, vel_y):
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.pos_x = pos_x
        self.pos_y = pos_y

    def move(self):
        self.pos_x = (self.pos_x + self.vel_x) % AREA_WIDTH
        self.pos_y = (self.pos_y + self.vel_y) % AREA_HEIGHT

    def is_on(self, xy):
        return xy[0] == self.pos_x and xy[1] == self.pos_y


# Compile input into list of robots.
robots_list = []
regex = re.compile(r'p=(-?\d+),(-?\d+)\sv=(-?\d+),(-?\d+)$')
with open(input_file) as file:
    for line in file.readlines():
        regex_search = regex.search(line)
        robot = Robot(int(regex_search.group(1)), int(regex_search.group(2)),
                      int(regex_search.group(3)), int(regex_search.group(4)))
        robots_list.append(robot)


def print_state(print_tile_count=False):
    """Prints the current positions of the robots similar to the examples."""
    global robots_list
    tile_count = {}
    for bot in robots_list:
        xy = (bot.pos_x, bot.pos_y)
        tile_count.setdefault(xy, 0)
        tile_count[xy] += 1

    if print_tile_count: print(tile_count)

    for y_num in range(AREA_HEIGHT):
        for x_num in range(AREA_WIDTH):
            if (x_num, y_num) in tile_count:
                print(tile_count[(x_num, y_num)], end='')
            else:
                print('.', end='')
        print('')
    print('')


def calculate_quadrant_count():
    """Returns a 4-element list with the number of bots per quadrant."""
    global robots_list
    x_middle = AREA_WIDTH // 2
    y_middle = AREA_HEIGHT // 2

    # Quadrants:
    #  0 = top-left, 1 = top-right, 2 = bot-left, 3 = bot-right.
    quadrant_count = [0, 0, 0, 0]
    for bot in robots_list:
        bot_x, bot_y = bot.pos_x, bot.pos_y
        if bot_x < x_middle and bot_y < y_middle:
            quadrant_count[0] = quadrant_count[0] + 1
        elif bot_x > x_middle and bot_y < y_middle:
            quadrant_count[1] = quadrant_count[1] + 1
        elif bot_x < x_middle and bot_y > y_middle:
            quadrant_count[2] = quadrant_count[2] + 1
        elif bot_x > x_middle and bot_y > y_middle:
            quadrant_count[3] = quadrant_count[3] + 1
    return quadrant_count


def count_vertical_lines():
    """Checks all columns and find the column with the highest number of bots on it.
    Returns the number of bots and the number of the column."""
    max_count = 0
    max_col = 0
    for col_num in range(AREA_WIDTH):
        count = 0
        for bot in robots_list:
            if bot.pos_x == col_num:
                count += 1
        if count > max_count:
            max_col = col_num
            max_count = count
    return max_count, max_col


def all_bots_separate_tiles():
    """Checks if there are no tiles with several bots at once."""
    global robots_list
    tile_count = {}
    for bot in robots_list:
        xy = (bot.pos_x, bot.pos_y)
        tile_count.setdefault(xy, 0)
        tile_count[xy] += 1
    return len(tile_count) == len(robots_list)


# Simulates the movement of the robots.
state_list = []
NUM_STEPS = 10000  # Just need to do enough iterations to find the tree.
max_col_count = 0
for step in range(NUM_STEPS):
    # Do the normal bot movement for one step.
    for bot in robots_list:
        bot.move()

    # Count the number of bots in a
    col_count, column = count_vertical_lines()
    if col_count >= max_col_count:
        #
        print(f'Found a (new) maximum of bots ({col_count}) in a vertical row @ Step {step + 1}, Column {column}.')
        if all_bots_separate_tiles():
            # We assume that the tree must happen if we reach a maximum of bots in a row
            # at the same time when all bots are on separate tiles.
            print(f'Found the tree @ Step {step + 1}.')
            print()
            break
        max_col_count = col_count


print('Final positions:')
print_state()
print(f'At Step {step + 1}.')
