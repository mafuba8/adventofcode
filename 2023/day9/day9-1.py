#!/usr/bin/python3
# Advent of Code 2023 - Day 9, Part 1
# Benedikt Otto

# Open puzzle file.
#with open('example_9.txt') as file:
with open('input_9.txt') as file:
    lines = file.readlines()

# Parse input into list of lists.
sequences = []
for line in lines:
    seq = []
    for s in line.split(' '):
        seq.append(int(s))
    sequences.append(seq)


def continue_sequence_right(seq):
    """Continue the sequence to the right by recursively calculating the differences."""
    differences = []
    for k in range(len(seq) - 1):
        differences.append(seq[k + 1] - seq[k])

    # check if all differences are zero
    if all([k == 0 for k in differences]):
        # All elements are the same, so just add a copy of one to the right.
        seq.append(seq[0])
        return seq
    else:
        # Recursively continue the sequence of differences.
        diff_seq = continue_sequence_right(differences)
        # Add the last element of seq and the last element of diff_seq
        new_elem = seq[-1] + diff_seq[-1]
        seq.append(new_elem)
        return seq


# Calculate the next value for each sequence and add the new values together.
total_sum = 0
for seq in sequences:
    print(seq)
    new_seq = continue_sequence_right(seq)
    print(new_seq[-1])
    total_sum += new_seq[-1]

print('')
print(f'Total sum of extrapolated values: {total_sum}')

