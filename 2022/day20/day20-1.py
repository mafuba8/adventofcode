#!/usr/bin/python3
# Advent of Code 2022 - Day 20, Part 1
# Benedikt Otto
#

# input_file = '../examples/example_20.txt'
input_file = '../inputs/input_20.txt'

# Parse input into list.
encrypted_list = []
with open(input_file) as file:
    for idx, line in enumerate(file.readlines()):
        # To distinguish duplicate numbers, we list them as tuples with their index.
        t = (idx, int(line.strip()))
        encrypted_list.append(t)


def mix_idx(l, idx):
    """Mix the element at index idx."""
    _, n = l[idx]
    new_list = l[:]

    # For the purpose of mixing, the first and last element are considered the same position, so its mod len(l)-1.
    new_idx = (n + idx) % (len(l) - 1)
    if new_idx == 0:
        # An element that ends up on index 0 will be put on the last spot instead.
        new_idx = len(l) - 1
    del new_list[idx]
    new_list.insert(new_idx, l[idx])
    return new_list


# Remember the original order.
original_order = encrypted_list[:]

# Mix by all elements in the original order to decrypt the file.
l = encrypted_list
for t in original_order:
    idx = l.index(t)
    l = mix_idx(l, idx)
decrypted_list = [t[1] for t in l]

# Find the grove coordinates.
print(f'Decrypted list: {decrypted_list}')
idx_0 = decrypted_list.index(0)
a = decrypted_list[(idx_0 + 1000) % len(l)]
b = decrypted_list[(idx_0 + 2000) % len(l)]
c = decrypted_list[(idx_0 + 3000) % len(l)]
print(f'Grove coordinates: {a} & {b} & {c}')
print(f'Sum: {a+b+c}')
