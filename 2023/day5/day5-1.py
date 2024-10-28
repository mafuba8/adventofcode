#!/usr/bin/python3
# Advent of Code 2023 - Day 5, Part 1
# Benedikt Otto
import re

# Open puzzle file.
with open('../examples/example_5.txt') as file:
#with open('input_5.txt') as file:
    lines = file.readlines()


# Get seed list.
seed_list = []
top_line = lines[0].split(':')
for seed in top_line[1].strip().split(' '):
    seed_list.append(int(seed))

# Dictionaries for the maps.
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



# Get the location numbers of all the seeds by translating it through the dicts.
location_list = []
for seed in seed_list:
    soil = translate(seed, seed_to_soil)
    fert = translate(soil, soil_to_fert)
    water = translate(fert, fert_to_water)
    light = translate(water, water_to_light)
    temp = translate(light, light_to_temp)
    humid = translate(temp, temp_to_humid)
    location = translate(humid, humid_to_location)

    location_list.append(location)
    print(f'Seed {seed} - Soil {soil} - Fert {fert} - Water {water} - Light {light}'
          f' - Temp {temp} - Humid {humid} - Location: {location}')

# Minimum of all location numbers
min_location = min(location_list)
print(f'Minimum location number: {min_location}')

