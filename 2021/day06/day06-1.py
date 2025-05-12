#!/usr/bin/python3
# Advent of Code 2021 - Day 6, Part 1
# Benedikt Otto
#

# input_file = '../examples/example_6.txt'
input_file = '../inputs/input_6.txt'

# Parse input into a list.
intitial_state = []
with open(input_file) as file:
    intitial_state = [int(s) for s in file.readline().strip().split(',')]


# Simulate how the fish multiply.
NUM_DAYS = 80
state = intitial_state[:]
for time in range(1, NUM_DAYS+1):
    new_state = []
    new_fish = []
    for x in state:
        if x > 0:
            new_state.append(x-1)
        else:
            new_state.append(6)  # reset old laternfish timer to 6.
            new_fish.append(8)   # new laternfish with timer of 8.

    # The example appends all the new fish at the end.
    state = new_state + new_fish

    #print(f'After {time} days: {state}')

print(f'Number of fish after {NUM_DAYS} days: {len(state)}')
