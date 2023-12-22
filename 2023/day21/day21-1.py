#!/usr/bin/python3
# Advent of Code 2023 - Day 21, Part 1
import functools

# Open puzzle file and parse it.
map_dict = {}
start = (0, 0)
map_width = 0
map_height = 0
#with open('example_21.txt') as file:
with open('input_21.txt') as file:
    lines = file.readlines()
    map_height = len(lines)
    for row_num, row in enumerate(lines):
        map_width = len(row) - 1
        for col_num, char in enumerate(row.strip()):
            map_dict.setdefault((row_num, col_num), char)
            if char == 'S':
                start = (row_num, col_num)


@functools.cache
def reachable_plots(start_row, start_col, steps):
    """Returns a set of all plots that are reachable from (start_row, start_col)
    with the given amount of steps."""

    # Recursion end.
    if steps == 0:
        return {(start_row, start_col)}

    plot_north = (start_row - 1, start_col)
    plot_south = (start_row + 1, start_col)
    plot_west = (start_row, start_col - 1)
    plot_east = (start_row, start_col + 1)
    neighbors = [plot_north, plot_south, plot_west, plot_east]

    plot_set = set()

    for plot in neighbors:
        if 0 <= plot[0] < map_height and 0 <= plot[1] < map_width and map_dict[plot] != '#':
            plot_set = plot_set.union(reachable_plots(plot[0], plot[1], steps - 1))

    return plot_set


result = reachable_plots(start[0], start[1], 64)
print(f'Number of reachable plots: {len(result)}')
