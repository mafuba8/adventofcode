#!/usr/bin/python3
# Advent of Code 2025 - Day 8, Part 1
# Benedikt Otto
#
# Slow solution, needs some better ideas.

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


# Sorted list of pairs (distance, p1, p2).
shortest_pairs = []

# List of circuits (sets of junctions).
circuit_list = []

def add_to_shortest_pairs(d, p1, p2):
    """Inserts the given pair at the right sport of the sorted list shortest_pairs."""
    global shortest_pairs

    # Always add on empty list.
    if len(shortest_pairs) == 0:
        shortest_pairs.append((d, p1, p2))
    else:
        # Insert in the right spot of the pre-sorted list.
        inserted = False
        for idx, t in enumerate(shortest_pairs):
            if d < t[0] and (d, p2, p1) not in shortest_pairs:
                shortest_pairs.insert(idx, (d, p1, p2))
                inserted = True
                break
        # Insert at the end.
        if not inserted:
            shortest_pairs.append((d, p1, p2))


def add_to_circuits(pair):
    """Adds the given pair to the circuits."""
    global circuit_list
    j1, j2 = pair

    c_left, c_right = {j1}, {j2}
    for c in circuit_list:
        if j1 in c:
            c_left = c_left.union(c)
            circuit_list.remove(c)

    for c in circuit_list:
        if j2 in c:
            c_right = c_right.union(c)
            circuit_list.remove(c)

    circuit_list.append(c_left.union(c_right))


def get_shortest_pair():
    global junction_boxes, shortest_pairs
    shortest = None
    min_dist = 1_000_000_000
    for j1 in junction_boxes:
        for j2 in junction_boxes:
            if j1 != j2:
                dist = distance(j1, j2)
                if dist < min_dist and (dist, j1, j2) not in shortest_pairs and (dist, j2, j1) not in shortest_pairs:
                    shortest = (j1, j2)
                    min_dist = dist
    return shortest, min_dist


# Find the shortest pairs and add them until we have a single circuit.
while True:
    sp, sd = get_shortest_pair()

    print(f'Inserting {sp}')
    add_to_shortest_pairs(sd, sp[0], sp[1])
    add_to_circuits(sp)

    circuit_sizes = [len(s) for s in circuit_list]
    circuit_sizes.sort(reverse=True)
    print(f'  Sizes: {circuit_sizes}')
    if len(circuit_list[0]) == len(junction_boxes):
        break

# Multiply the first coordinate of the last added pair together to find the solution.
result = sp[0][0] * sp[1][0]
print(f'The result is: {result}.')
