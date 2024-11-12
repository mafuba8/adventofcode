#!/usr/bin/python3
# Advent of Code 2022 - Day 15, Part 2
# Benedikt Otto
import re

# input_file = '../examples/example_15.txt'
input_file = '../inputs/input_15.txt'

# Max. coordinates for the search area.
# SEARCH_AREA_MAX = 20
SEARCH_AREA_MAX = 4_000_000

# Parse input into dict(key=(sensor_x, sensor_y), val=(beacon_x, beacon_y))
sensor_dict = {}
regex = re.compile(r'^.*x=(-?\d+),\sy=(-?\d+):.*x=(-?\d+),\sy=(-?\d+)$')
with open(input_file) as file:
    for line in file.readlines():
        search = regex.search(line)
        sensor_pos = (int(search.group(1)), int(search.group(2)))
        closest_beacon = (int(search.group(3)), int(search.group(4)))
        sensor_dict.setdefault(sensor_pos, closest_beacon)


# For each sensor, we find the tiles that directly border its sensor range (distance + 1).
possible_tiles = set()
for sensor in sensor_dict:
    beacon = sensor_dict[sensor]
    # Distance of tiles that border the search area.
    dist_border = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1]) + 1

    # Find the tiles within the search area that are exactly distance+1 away from the sensor.
    possible_tiles_sensor = set()
    x0, y0 = sensor
    for x in range(dist_border + 1):
        y = dist_border - x
        for pos in [(x0+x, y0+y), (x0-x, y0+y), (x0+x, y0-y), (x0-x, y0-y)]:
            if 0 <= pos[0] <= SEARCH_AREA_MAX and 0 <= pos[1] <= SEARCH_AREA_MAX:
                if pos not in sensor_dict.values():
                    possible_tiles_sensor.add(pos)
    possible_tiles = possible_tiles.union(possible_tiles_sensor)

# Out of these possible tiles, find the one outside the scanning range of _all_ sensors.
distress_beacon_pos = (0, 0)
for tile in possible_tiles:
    count = 0
    for sensor in sensor_dict:
        beacon = sensor_dict[sensor]
        dist = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
        if abs(sensor[0] - tile[0]) + abs(sensor[1] - tile[1]) > dist:
            count += 1

    # See if we found a (the) point that is outside all sensor ranges.
    if count == len(sensor_dict):
        distress_beacon_pos = tile
        break

print(f'The distress beacon ist at {distress_beacon_pos}.')
print(f'Tuning Frequency: {distress_beacon_pos[0] * 4_000_000 + distress_beacon_pos[1]}')
