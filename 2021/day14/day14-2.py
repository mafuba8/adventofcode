#!/usr/bin/python3
# Advent of Code 2021 - Day 14, Part 2
# Benedikt Otto
#
import functools

# input_file = '../examples/example_14.txt'
input_file = '../inputs/input_14.txt'

# Parse input.
poly_template = []
insertion_rules = {}
with open(input_file) as file:
    first_part = True
    for line in file.readlines():
        if first_part:
            # Polymer template.
            if line == '\n':
                first_part = False
            else:
                poly_template = list(line.strip())
        else:
            # Pair insertion rules.
            req, ins = line.strip().split(' -> ')
            insertion_rules.setdefault(req, ins)


@functools.cache
def tally_element(pair, element, recursion_count):
    """Returns how many times the given element is contained in the end polymer,
    if we start with the given pair and run the recursion for recursion_count steps."""
    e1, e2, = pair

    # Recursion end.
    if recursion_count == 0:
        return [e1, e2].count(element)

    # Find the middle element and run the recursion for both pairs.
    m = insertion_rules[''.join(pair)]
    total_count =  (tally_element((e1, m), element, recursion_count - 1) +
                    tally_element((m, e2), element, recursion_count - 1))

    # Adjust for double-counting the middle element.
    if m == element:
        total_count -= 1
    return total_count


# Create dict with all the elements found in the insertion rules.
tally = {}
for key in insertion_rules.keys():
    for c in key:
        tally.setdefault(c, 0)

NUM_STEPS = 40
# Run through all the pairs of elements and count how many times it appears
# after NUM_STEPS steps.
for idx in range(len(poly_template) - 1):
    p = (poly_template[idx], poly_template[idx+1])

    # Count for each element.
    for e in tally:
        tally[e] += tally_element(p, e, NUM_STEPS)

    # Account for double-counting the middle element.
    tally[poly_template[idx+1]] -= 1

# The very last element does not count as middle element.
tally[poly_template[-1]] += 1

print(f'Tally of elements after {NUM_STEPS} steps:')
print(tally)
print(f'Difference count between most common and least common element: '
      f'{max(tally.values()) - min(tally.values())}')
