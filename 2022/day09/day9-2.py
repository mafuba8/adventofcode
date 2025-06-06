#!/usr/bin/python3
# Advent of Code 2022 - Day 9, Part 2
# Benedikt Otto

# input_file = '../examples/example_9-larger.txt'
input_file = '../inputs/input_9.txt'

# Parse input into list of commands ('X', 0):
motion_list = []
with open(input_file) as file:
    for line in file.readlines()[:]:
        m = line.strip().split(' ')
        direction, steps = tuple(m)
        motion_list.append((direction, int(steps)))


def dist(p1, p2):
    """Distance function (Uniform norm)."""
    return max(abs(p1[0] - p2[0]), abs(p1[1] - p2[1]))


def move_head(head_pos, direction):
    """Moves the head according to the direction.
    Returns the new position of the head."""
    x, y = head_pos
    match direction:
        case 'U': x -= 1
        case 'D': x += 1
        case 'L': y -= 1
        case 'R': y += 1
    # print(f'> Head: {head_pos} -> {(x, y)}')
    return x, y


def move_tail(head_pos, tail_pos):
    """Moves the tail according to its relation to the head.
    Returns the new position of the tail."""
    # Check if we need to move T at all:
    if dist(head_pos, tail_pos) <= 1:
        # print(f'> Tail: does not move.')
        return tail_pos

    # H can now move diagonally, so we need to account for that.
    hx, hy = head_pos
    tx, ty = tail_pos
    if hx - tx == 2:
        if hy - ty == 2: return tx+1, ty+1
        elif hy - ty == -2: return tx+1, ty-1
    elif hx - tx == -2:
        if hy - ty == 2: return tx-1, ty+1
        elif hy - ty == -2: return tx-1, ty-1

    # The tail always moves to the unique neighbor which is
    # a straight neighbor (horizontally or vertically adjacent)
    # to the head.

    # Eight adjacent points of tail.
    tail_neigh = [(tail_pos[0] + k, tail_pos[1] + l) for k in (-1, 0, 1) for l in (-1, 0, 1)]
    tail_neigh.remove(tail_pos)  # remove the point itself.

    # The four straight neighbors of head.
    head_neigh_straight = [(head_pos[0] + 1, head_pos[1]), (head_pos[0] - 1, head_pos[1]),
                           (head_pos[0], head_pos[1] + 1), (head_pos[0], head_pos[1] - 1)]

    # Find the straight neighbor of head that is also a neighbor of tail.
    new_tail_pos = tail_pos
    for tile in head_neigh_straight:
        if tile in tail_neigh:
            new_tail_pos = tile

    # print(f'> Tail: {tail_pos} -> {new_tail_pos}')
    return new_tail_pos


# Set up a rope of ten knots. head = rope[0], tail = rope[9].
rope = [(0, 0) for k in range(10)]

# Run through the motions.
visited_tiles = {rope[9]}
for motion in motion_list:
    direction = motion[0]
    steps = motion[1]
    # print(f'Move Head {steps}x {direction}:')

    for step in range(steps):
        rope[0] = move_head(rope[0], direction)
        for k in range(1, 10):
            rope[k] = move_tail(rope[k-1], rope[k])
        visited_tiles.add(rope[9])

print('Tiles visited by tail:')
print(visited_tiles)
print(f'Number of tiles visited: {len(visited_tiles)}')
