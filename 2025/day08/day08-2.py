#!/usr/bin/python3
# Advent of Code 2025 - Day 8, Part 2
# Benedikt Otto
#

# INPUT_FILE = '../examples/example_08.txt'
INPUT_FILE = '../inputs/input_08.txt'

# Parse input into list of tuples.
junction_boxes = []
with open(INPUT_FILE) as file:
    for line in file.readlines():
        j = line.strip().split(',')
        j = tuple(map(int, j))
        junction_boxes.append(j)


def distance(p1, p2):
    """Calculates the square of the Euclidean distance of the two xyz points."""
    return (p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2 + (p2[2] - p1[2]) ** 2


# To prevent re-calculation at each step, save the distances between pairs as a list.
pair_distances = []
for idx, j1 in enumerate(junction_boxes):
    for j2 in junction_boxes[idx:]:
        if j1 != j2:
            # Insert in the right spot of the pre-sorted list.
            dist = distance(j1, j2)
            pair_distances.append((dist, j1, j2))

# Sort the list by distance in descending order.
pair_distances.sort(key=lambda t: t[0], reverse=True)


# Add pairs to circuits until we have a single circuit.
circuit_list = []
while True:
    # List is sorted, so this gives the pair with the shortest distance.
    d, j1, j2 = pair_distances.pop()

    # Add the pair to the circuits.
    c_left, c_right = {j1}, {j2}
    # Find circuit with j1 in it and remove it from the list.
    for c in circuit_list:
        if j1 in c:
            c_left = c_left.union(c)
            circuit_list.remove(c)
    # Find circuit with j2 in it and remove it from the list.
    for c in circuit_list:
        if j2 in c:
            c_right = c_right.union(c)
            circuit_list.remove(c)
    # Add the circuit with the merged circuits to the list.
    circuit_list.append(c_left.union(c_right))

    # Print status.
    circuit_sizes = [len(s) for s in circuit_list]
    circuit_sizes.sort(reverse=True)
    print(f'Circuits: {circuit_sizes}')

    # Stop if only a single circuit is left.
    if circuit_sizes[0] == len(junction_boxes):
        result = j1[0] * j2[0]
        break

# Multiply the first coordinate of the last added pair together to find the solution.
print(f'The result is: {result}.')
