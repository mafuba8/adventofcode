#!/usr/bin/python3
# Advent of Code 2022 - Day 19, Part 1
# Benedikt Otto
#
# Materials, blueprint costs and bot count are always saved as tuples (ore, clay, obsidian, geodes).
import re
import functools
import math

# input_file = '../examples/example_19.txt'
input_file = '../inputs/input_19.txt'

# Parse input into list of blueprints (tuples).
bp_list = []
re_orebot = re.compile(r'ore\srobot\scosts\s(\d+)\sore')
re_claybot = re.compile(r'clay\srobot\scosts\s(\d+)\sore')
re_obsbot = re.compile(r'obsidian\srobot\scosts\s(\d+)\sore\sand\s(\d+)\sclay')
re_geodebot = re.compile(r'geode\srobot\scosts\s(\d+)\sore\sand\s(\d+)\sobsidian')
with open(input_file) as file:
    for line in file.readlines():
        # Bots of one type are always made from the same material types.
        orebot = (int(re_orebot.search(line).group(1)), 0, 0, 0)
        claybot = (int(re_claybot.search(line).group(1)), 0, 0, 0)
        obsbot = (int(re_obsbot.search(line).group(1)), int(re_obsbot.search(line).group(2)), 0, 0)
        geodebot = (int(re_geodebot.search(line).group(1)), 0, int(re_geodebot.search(line).group(2)), 0)
        bp_list.append((orebot, claybot, obsbot, geodebot))


def minutes_required(resources, bots, bot_blueprint):
    """Returns the number of minutes that we need to wait to build a certain bot."""
    # Building a bot always takes 1 minute.
    if all([resources[k] >= bot_blueprint[k] for k in range(4)]):
        return 1  # We have enough resources to start building it immediately.
    else:
        return max([math.ceil((bot_blueprint[k] - resources[k]) / bots[k]) for k in range(4) if bots[k] != 0]) + 1


@functools.cache
def find_max_geodes(resources, bots, time_remaining, blueprint):
    """Finds the maximum number of geodes that can be crafted in the given time
    using the blueprint with the given starting resources and starting bot count."""
    # Recursion end. (no need to craft any more bots).
    if time_remaining in {0, 1}:
        return resources[3] + time_remaining * bots[3]

    # We never need more bots than we can use up resources in one minute.
    ore_max = max([bp[0] for bp in blueprint])
    clay_max = max([bp[1] for bp in blueprint])
    obs_max = max([bp[2] for bp in blueprint])

    max_geodes = 0
    # We distinguish by which robot to build next.
    # Option: Build an ore robot next.
    if bots[0] > 0 and bots[0] < ore_max:  # Need at least 1 ore bot.
        bp = blueprint[0]
        # Find out how long we need to wait to build an ore bot.
        minutes = minutes_required(resources, bots, bp)
        new_time = time_remaining - minutes
        if new_time > 0:
            # Run recursion with new values, in particular with the resources accrued in the meantime.
            new_bots = (bots[0] + 1, bots[1], bots[2], bots[3])
            new_resources = (resources[0] + minutes * bots[0] - bp[0],
                             resources[1] + minutes * bots[1],
                             resources[2] + minutes * bots[2],
                             resources[3] + minutes * bots[3])
            g = find_max_geodes(new_resources, new_bots, new_time, blueprint)
            max_geodes = max(max_geodes, g)

    # Option: Build a clay robot next.
    if bots[0] > 0 and bots[1] < clay_max:  # Need at least 1 ore bot.
        bp = blueprint[1]
        # Find out how long we need to wait to build a clay bot.
        minutes = minutes_required(resources, bots, bp)
        new_time = time_remaining - minutes
        if new_time > 0:
            # Run recursion with new values, in particular with the resources accrued in the meantime.
            new_bots = (bots[0], bots[1] + 1, bots[2], bots[3])
            new_resources = (resources[0] + minutes * bots[0] - bp[0],
                             resources[1] + minutes * bots[1],
                             resources[2] + minutes * bots[2],
                             resources[3] + minutes * bots[3])
            g = find_max_geodes(new_resources, new_bots, new_time, blueprint)
            max_geodes = max(max_geodes, g)

    # Option: Build an obsidian robot next.
    if bots[0] > 0 and bots[1] > 0 and bots[2] < obs_max:  # Need at least 1 ore and 1 clay bot.
        bp = blueprint[2]
        # Find out how long we need to wait to build an obsidian bot.
        minutes = minutes_required(resources, bots, bp)
        new_time = time_remaining - minutes
        if new_time > 0:
            # Run recursion with new values, in particular with the resources accrued in the meantime.
            new_bots = (bots[0], bots[1], bots[2] + 1, bots[3])
            new_resources = (resources[0] + minutes * bots[0] - bp[0],
                             resources[1] + minutes * bots[1] - bp[1],
                             resources[2] + minutes * bots[2],
                             resources[3] + minutes * bots[3])
            g = find_max_geodes(new_resources, new_bots, new_time, blueprint)
            max_geodes = max(max_geodes, g)

    # Option: Build a geode robot next.
    if bots[0] > 0 and bots[2] > 0:  # Need at least 1 ore and 1 obsidian bot.
        bp = blueprint[3]
        # Find out how long we need to wait to build a geode bot.
        minutes = minutes_required(resources, bots, bp)
        new_time = time_remaining - minutes
        if new_time > 0:
            # Run recursion with new values, in particular with the resources accrued in the meantime.
            new_bots = (bots[0], bots[1], bots[2], bots[3] + 1)
            new_resources = (resources[0] + minutes * bots[0] - bp[0],
                             resources[1] + minutes * bots[1],
                             resources[2] + minutes * bots[2] - bp[2],
                             resources[3] + minutes * bots[3])
            g = find_max_geodes(new_resources, new_bots, new_time, blueprint)
            max_geodes = max(max_geodes, g)

    # Option to build no additional bot.
    max_geodes = max(max_geodes, resources[3] + time_remaining * bots[3])

    return max_geodes


# Run through all blueprints and figure out how many geodes they produce and their quality level.
quality_level_sum = 0
for bp_num, blueprint in enumerate(bp_list):
    g = find_max_geodes((0, 0, 0, 0), (1, 0, 0, 0), 24, blueprint)
    quality_level = (bp_num + 1) * g
    quality_level_sum += quality_level
    print(f'Blueprint {bp_num+1}: Max {g} geodes (Quality level {quality_level}).')

print(f'Sum of all quality levels: {quality_level_sum}')
