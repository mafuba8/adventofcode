#!/usr/bin/python3
# Advent of Code 2021 - Day 17, Part 1
# Benedikt Otto
#
import re

# input_file = '../examples/example_17.txt'
input_file = '../inputs/input_17.txt'

regex = re.compile(r'^.*x=(-?\d+)\.\.(-?\d+),\sy=(-?\d+)\.\.(-?\d+)$')
with open(input_file) as file:
    for line in file.readlines():
        s = regex.search(line)
        target_area = {'x_min': int(s.group(1)), 'x_max': int(s.group(2)),
                       'y_min': int(s.group(3)), 'y_max': int(s.group(4))}


def is_within_target(start_velocity):
    """Simulates the throw of the probe from (0, 0) with the given starting velocity.
    Returns (is_within:bool, max_height:int)."""
    velocity = start_velocity
    position = (0, 0)

    max_height = 0
    while True:
        # Simulate one step.
        position = (position[0] + velocity[0], position[1] + velocity[1])

        # Account for drag and gravity.
        vx = 0
        if velocity[0] > 0:
            vx = velocity[0] - 1
        elif velocity[0] < 0:
            vx = velocity[0] + 1
        velocity = (vx, velocity[1] - 1)

        # Check for new maximum height.
        max_height = max(max_height, position[1])

        # Check if probe is within the area.
        if (target_area['x_min'] <= position[0] <= target_area['x_max']
                and target_area['y_min'] <= position[1] <= target_area['y_max']):
            return True, max_height

        # Check if it is already past the area.
        if position[1] < target_area['y_min']:
            return False, max_height



# X and Y are independent of each other.
# With the starting Y-speed high enough, X-speed will reach 0, so finding an initial X speed is easy to find.
posx = 0
initial_speed_x = 1
while not target_area['x_min'] <= posx <= target_area['x_max']:
    posx += initial_speed_x
    initial_speed_x += 1

# Since y decreases by 1 each step due to gravity, a starting speed of n means that
#   - the peak is reached after t=n steps (where v-speed is 0)
#   - at t=2n steps the probe will reach the coordinate y=0 with speed -n
#   - the step after that will be with speed -(n+1) from coordinate y=0 to coordinate y=-(n+1).
# The maximum possible speed will be when there is only one step from y=0 to the lowest point of the
# target area, which will be with speed target_area['y_min'] - 1.
max_initial_speed_y = - target_area['y_min'] - 1

# This makes the following initial velocity.
max_initial_velocity = (initial_speed_x, max_initial_speed_y)

# Calculate the height with this initial speed.
max_height = 0
for t in range(max_initial_speed_y + 1):
    max_height += t

# Sanity check.
assert is_within_target(max_initial_velocity)[0]

print(f'The maximum achievable height is {max_height}')
print(f'for example via starting velocity {max_initial_velocity}')
