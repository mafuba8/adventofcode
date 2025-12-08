#!/usr/bin/python3
# Advent of Code 2025 - Day 8, Part 1
# Benedikt Otto
#

# INPUT_FILE = '../examples/example_08.txt'
INPUT_FILE = '../inputs/input_08.txt'

# NUM_SHORTEST_PAIRS = 10
NUM_SHORTEST_PAIRS = 1000

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


# Sorted list of pairs (distance, p1, p2).
shortest_pairs = []

def add_to_shortest_pairs(p1, p2, d):
    """Inserts the given pair at the right sport of the sorted list shortest_pairs."""
    global shortest_pairs

    # Always add on empty list.
    if len(shortest_pairs) == 0:
        shortest_pairs.append((d, p1, p2))
    else:
        # Insert in the right spot of the pre-sorted list.
        for idx, t in enumerate(shortest_pairs):
            if d < t[0] and (d, p2, p1) not in shortest_pairs:
                shortest_pairs.insert(idx, (d, p1, p2))
                break

    # Make sure that the list is not longer than NUM_SHORTEST_PAIRS.
    if len(shortest_pairs) > NUM_SHORTEST_PAIRS:
        shortest_pairs = shortest_pairs[:NUM_SHORTEST_PAIRS]


# Run through all pairs and add them to the list of shortest pairs.
for j1 in junction_boxes:
    for j2 in junction_boxes:
        if j1 != j2:
            dist = distance(j1, j2)
            add_to_shortest_pairs(j1, j2, dist)

# Build list of circuits (sets of junction boxes).
circuit_list = []
for dist, j1, j2 in shortest_pairs:
    print(f'  {dist} ({j1} <> {j2})')

    c_left, c_right = {j1}, {j2}
    for c in circuit_list:
        if j1 in c:
            c_left = c_left.union(c)
        if j2 in c:
            c_right = c_right.union(c)

        if j1 in c or j2 in c:
            circuit_list.remove(c)

    circuit_list.append(c_left.union(c_right))


# Create sorted list of circuit sizes.
circuit_sizes = [len(s) for s in circuit_list]
circuit_sizes.sort(reverse=True)

result = circuit_sizes[0] * circuit_sizes[1] * circuit_sizes[2]
print(f'The three largest circuit sizes multiplied: {result}.')
