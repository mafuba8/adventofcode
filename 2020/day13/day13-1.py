#!/usr/bin/python3
# Advent of Code 2020 - Day 13, Part 1
# Benedikt Otto
#

# input_file = '../examples/example_13.txt'
input_file = '../inputs/input_13.txt'

# Parse input.
bus_list = []
with open(input_file) as file:
    earliest_timestamp = int(file.readline())
    for e in file.readline().strip().split(','):
        if e != 'x':
            bus_list.append(int(e))

print(earliest_timestamp)
print(bus_list)


def check_for_bus(time):
    global bus_list
    for bus in bus_list:
        if time % bus == 0:
            return bus
    return None

timestamp = earliest_timestamp
while True:
    bus = check_for_bus(timestamp)
    if bus is not None:
        time_diff = timestamp - earliest_timestamp
        result = time_diff * bus
        print(f'Bus {bus} works for {timestamp} (diff: {time_diff}).')
        print(f'Result: {result}.')
        break
    timestamp += 1
