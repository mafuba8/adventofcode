#!/usr/bin/python3
# Advent of Code 2024 - Day 9, Part 2
# Benedikt Otto
#

#input_file = '../examples/example_9.txt'
input_file = '../inputs/input_9.txt'

# Parse input into list of dicts.
filesystem = []
file_lengths = {}
with open(input_file) as file:
    is_file = True
    file_id = 0
    for char in file.readline().strip():
        length = int(char)
        if is_file:
            f = {'type': 'file', 'file_id': file_id, 'file_length': length}
            file_lengths.setdefault(file_id, length)
            filesystem.append(f)
            file_id += 1
        if not is_file and length > 0:
            f = {'type': 'free', 'free_length': length}
            filesystem.append(f)

        is_file = not is_file

# Remember the highest file id.
max_file_id = file_id - 1


# Build list of blocks. Block = '.' or id of a file.
blocks_list = []
for f in filesystem:
    match f['type']:
        case 'file':
            for k in range(f['file_length']):
                blocks_list.append(str(f['file_id']))
        case 'free':
            for k in range(f['free_length']):
                blocks_list.append('.')


# The actual process of de-fragmenting. For each file we try to find set of
# contiguous free blocks with adequate size.
for file_id in range(max_file_id + 1).__reversed__():
    print(f' trying to move file {file_id}/{max_file_id}')
    search_length = file_lengths[file_id]

    # We are only allowed to move the blocks towards the front.
    idx = blocks_list.index(str(file_id))
    for k in range(idx):
        # Sliding search window to find a block of '.' with length >= search_length.
        search_window = ''.join(blocks_list[k:k+search_length])
        if search_window == '.' * search_length:
            # Here we have found a strip of '....' with enough length.
            # Replace all old blocks with file_id with '.'.
            for i in range(len(blocks_list)):
                if blocks_list[i] == str(file_id):
                    blocks_list[i] = '.'

            # Write the file blocks at the new position.
            for i in range(search_length):
                blocks_list[k + i] = str(file_id)

            break


# Calculate filesystem checksum.
checksum = 0
for k in range(len(blocks_list)):
    if blocks_list[k] != '.':
        checksum += k * int(blocks_list[k])

print(f'Filesystem checksum after de-fragmenting: {checksum}')
