#!/usr/bin/python3
# Advent of Code 2024 - Day 9, Part 1
# Benedikt Otto
#

#input_file = '../examples/example_9.txt'
input_file = '../inputs/input_9.txt'

# Parse input into list of dicts.
filesystem = []
with open(input_file) as file:
    is_file = True
    file_id = 0
    for char in file.readline().strip():
        length = int(char)
        if is_file:
            f = {'type': 'file', 'file_id': file_id, 'file_length': length}
            filesystem.append(f)
            file_id += 1
        if not is_file:
            f = {'type': 'free', 'free_length': length}
            filesystem.append(f)

        is_file = not is_file


# Build list of blocks. Block = '.' or id of a file.
blocks_list = []
for f in filesystem:
    match f['type']:
        case 'file':
            for k in range(f['file_length']):
                blocks_list.append(f['file_id'])
        case 'free':
            for k in range(f['free_length']):
                blocks_list.append('.')


# Re-order blocks.
while '.' in blocks_list:
    # Remove trailing free space.
    if blocks_list[-1] == '.':
        del blocks_list[-1]
        continue

    # Move the last non-free block to the first free spot.
    i = blocks_list.index('.')
    blocks_list[i] = blocks_list[-1]
    blocks_list[-1] = '.'


# Calculate filesystem checksum.
checksum = 0
for k in range(len(blocks_list)):
    checksum += k * blocks_list[k]

print(f'Filesystem checksum after re-ordering blocks: {checksum}')
