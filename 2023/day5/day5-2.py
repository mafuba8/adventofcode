#!/usr/bin/python3
# Advent of Code 2023 - Day 5, Part 2
# Benedikt Otto
#
# Mostly brute-force, not elegant...
import math
from multiprocessing import Pool

# Open puzzle file.
#with open('example_5.txt') as file:
with open('input_5.txt') as file:
    lines = file.readlines()


# Get list of seed numbers.
seed_num_list = []
top_line = lines[0].split(':')
for seed in top_line[1].strip().split(' '):
    seed_num_list.append(int(seed))

# Dict with key= seed_num and val=seed_range
seed_list = []
for k in range(0, len(seed_num_list), 2):
    seed_list.append((seed_num_list[k], seed_num_list[k + 1]))


# Dictionaries for the translation maps.
seed_to_soil = []
soil_to_fert = []
fert_to_water = []
water_to_light = []
light_to_temp = []
temp_to_humid = []
humid_to_location = []


# Parse input into dictionaries.
almanac_map = seed_to_soil
for line in lines[1:]:
    # The map header only sets the almanac_map.
    match line:
        case "\n":
            continue
        case "seed-to-soil map:\n":
            almanac_map = seed_to_soil
            continue
        case "soil-to-fertilizer map:\n":
            almanac_map = soil_to_fert
            continue
        case "fertilizer-to-water map:\n":
            almanac_map = fert_to_water
            continue
        case "water-to-light map:\n":
            almanac_map = water_to_light
            continue
        case "light-to-temperature map:\n":
            almanac_map = light_to_temp
            continue
        case "temperature-to-humidity map:\n":
            almanac_map = temp_to_humid
            continue
        case "humidity-to-location map:\n":
            almanac_map = humid_to_location
            continue

    # Extract values and put them into their respective dictionaries
    almanac_map.append(tuple([int(s) for s in line.split(' ')]))


def translate(num, translation_map):
    """Translates num corresponding to the almanac_map."""
    # Look through all rows in the translation map to see if a value fits.
    for t in translation_map:
        dest_range_start, source_range_start, range_length = t
        if num in range(source_range_start, source_range_start + range_length):
            # Destination range plus the offset
            return dest_range_start + (num - source_range_start)

    # No fitting translation entry means the translated num is the num itself.
    return num


def calc_location(k):
    """Obtain the location of the seed 'seed_num + k'.
    Used for the multiprocessing pool."""
    soil = translate(seed_num + k, seed_to_soil)
    fert = translate(soil, soil_to_fert)
    water = translate(fert, fert_to_water)
    light = translate(water, water_to_light)
    temp = translate(light, light_to_temp)
    humid = translate(temp, temp_to_humid)
    return translate(humid, humid_to_location)


# Mainly brute forcing the result. Not fun.
global_min = math.inf
for seed in seed_list:
    (seed_num, seed_range) = seed

    # Use 12 threads to find the minimum location.
    p = Pool(processes=12)
    min_list = p.map(calc_location, range(seed_range))
    min_location = min(min_list)

    print(f'Seed {seed_num}:{seed_range} - Min Location: {min_location}')
    global_min = min(global_min, min_location)

# Minimum of all location numbers
print(f'Minimum of all location numbers: {global_min}')
