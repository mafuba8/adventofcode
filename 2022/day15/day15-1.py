#!/usr/bin/python3
# Advent of Code 2022 - Day 15, Part 1
# Benedikt Otto
import re

# input_file = '../examples/example_15.txt'
input_file = '../inputs/input_15.txt'

# Row that is checked for empty spots.
# QUESTION_ROW = 10
QUESTION_ROW = 2_000_000

# Parse input into dict(key=(sensor_x,sensor_y), val=(beacon_x,beacon_y))
sensor_dict = {}
regex = re.compile(r'^.*x=(-?\d+),\sy=(-?\d+):.*x=(-?\d+),\sy=(-?\d+)$')
with open(input_file) as file:
    for line in file.readlines():
        search = regex.search(line)
        sensor_pos = (int(search.group(1)), int(search.group(2)))
        closest_beacon = (int(search.group(3)), int(search.group(4)))
        sensor_dict.setdefault(sensor_pos, closest_beacon)


# For some reason this exercise uses x as columns and y as rows...
empty_spots = set()
for sensor in sensor_dict:
    beacon = sensor_dict[sensor]
    # Distance of the sensor to the closest beacon.
    distance = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
    # Distance to the sensor column within question_row.
    distance_in_row = distance - abs(sensor[1] - QUESTION_ROW)

    if distance_in_row > 0:
        # In this case there are actually 
        for k in range(sensor[0] - distance_in_row, sensor[0] + distance_in_row + 1):
            pos = (k, QUESTION_ROW)
            if pos not in sensor_dict.values():
                empty_spots.add(pos)

print(f"Number of spots in row {QUESTION_ROW} where we know that there is no beacon: {len(empty_spots)}")
