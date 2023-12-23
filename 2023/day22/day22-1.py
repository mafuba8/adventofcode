#!/usr/bin/python3
# Advent of Code 2023 - Day 22, Part 1

# Open puzzle file and parse it.
brick_list = []
maximum = {'x': 0, 'y': 0, 'z': 1}
#with open('example_22.txt') as file:
with open('input_22.txt') as file:
    for line in file.readlines():
        l1 = line.strip().split('~')
        (left_x, left_y, left_z) = l1[0].split(',')
        (right_x, right_y, right_z) = l1[1].split(',')
        (left_x, left_y, left_z) = (int(left_x), int(left_y), int(left_z))
        (right_x, right_y, right_z) = (int(right_x), int(right_y), int(right_z))
        brick_list.append([left_x, right_x, left_y, right_y, left_z, right_z])
        maximum['x'] = max(maximum['x'], left_x, right_x)
        maximum['y'] = max(maximum['y'], left_y, right_y)
        maximum['z'] = max(maximum['z'], left_z, right_z)

print(f'Max: {maximum["x"]}, {maximum["y"]}, {maximum["z"]}')


def list_below(brick):
    """Lists all the squares that are directly below the given brick."""
    [left_x, right_x, left_y, right_y, left_z, right_z] = brick
    below = []
    if min(left_z, right_z) <= 1:
        return []
    if left_z == right_z:  # Horizontal brick.
        for x in range(min(left_x, right_x), max(left_x, right_x) + 1):
            for y in range(min(left_y, right_y), max(left_y, right_y) + 1):
                below.append((x, y, left_z - 1))
    else:  # Vertical brick.
        z = min(left_z, right_z) - 1
        below.append((left_x, left_y, z))
    return below


def get_brick(x, y, z):
    """Returns the brick that occupies the given block, or none if there is no brick."""
    for brick in brick_list:
        [left_x, right_x, left_y, right_y, left_z, right_z] = brick
        if x in range(min(left_x, right_x), max(left_x, right_x) + 1):
            if y in range(min(left_y, right_y), max(left_y, right_y) + 1):
                if z in range(min(left_z, right_z), max(left_z, right_z) + 1):
                    return brick
    return None


def can_fall(brick):
    """Checks if the given brick can fall down."""
    if min(brick[4], brick[5]) == 1:
        return False
    below = list_below(brick)
    for (x, y, z) in below:
        if get_brick(x, y, z) is not None:
            return False
    return True


# Simulate falling of blocks.
for height in range(2, maximum['z'] + 1):
    for brick in [brick for brick in brick_list if min(brick[4], brick[5]) == height]:
        while can_fall(brick):
            brick[4] -= 1
            brick[5] -= 1


# Build dict that assigns every brick a list of all bricks supporting it.
support_dict = {}
for brick in brick_list:
    supp_set = set()
    below = list_below(brick)
    for (x, y, z) in below:
        supp_brick = get_brick(x, y, z)
        if supp_brick is not None:
            supp_set.add(tuple(supp_brick))
    support_dict.setdefault(tuple(brick), supp_set)

# Get non-removable bricks, which are those that are the only support of a brick.
non_removable = set()
for brick in brick_list:
    s = support_dict[tuple(brick)]
    if len(s) == 1:
        non_removable.update(s)

# The removable bricks are just the bricks not in non_removable.
disintegrate_count = 0
for brick in brick_list:
    if tuple(brick) not in non_removable:
        print(f'Brick {brick} can be removed.')
        disintegrate_count += 1
print(f'Total number of bricks that can be disintegrated: {disintegrate_count}')
