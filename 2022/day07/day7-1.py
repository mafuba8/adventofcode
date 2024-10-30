#!/usr/bin/python3
# Advent of Code 2022 - Day 7, Part 1
# Benedikt Otto
import re

# input_file = '../examples/example_7.txt'
input_file = '../inputs/input_7.txt'

# Helper functions for building directory paths.
def previous_dir(_current_dir):
    if _current_dir == '/':
        return '/'
    l = _current_dir.split('/')
    if len(l) == 2:
        return '/'
    return '/'.join(l[:-1])

def next_dir(_current_dir, _new_dir):
    if _new_dir[0] == '/':
        return _new_dir  # absolute path
    if _current_dir == '/':
        return '/' + _new_dir  # special case for root dir
    return _current_dir + '/' + _new_dir  # normal relative path


# For parsing the directory contents.
re_files = re.compile(r'^(\d*|dir)\s(.*)$')

# Parse into dictionary of directories:
# ex.: {'/': [('/a', 'dir'), ('/b.txt', '1234'), ('/c.dat', '12345'), ('/d', 'dir')]}
directory_dict = {}
with open(input_file) as file:
    current_dir = ''
    for line in file.readlines():
        line = line.strip()
        if line[0] == '$':
            # Command (only '$ cd' relevant for us).
            if line[0:4] == '$ cd':
                new_dir = line[5:]
                if new_dir == '..':
                    current_dir = previous_dir(current_dir)
                else:
                    current_dir = next_dir(current_dir, new_dir)
        else:
            # Directory listing after '$ ls'.
            files_scan = re_files.search(line)
            obj_attr = files_scan.group(1)  # Object attribute
            obj_name = files_scan.group(2)  # Object name
            object_path = next_dir(current_dir, obj_name)

            # Add object or append to listing of an existing object.
            if current_dir in directory_dict:
                directory_dict[current_dir].append((object_path, obj_attr))
            else:
                directory_dict.setdefault(current_dir, [(object_path, obj_attr)])


def dir_size(_dir_name):
    """Returns the total size of a directory."""
    _size = 0
    for obj in directory_dict[_dir_name]:
        _obj_name, _obj_attr = obj
        if _obj_attr == 'dir':
            # subdirectory
            _size += dir_size(_obj_name)
        else:
            # file.
            _size += int(_obj_attr)
    return _size

# Calculate the total size of all directories that
# have at most 100000 size.
total_size_limited = 0
for dir_name in directory_dict:
    size = dir_size(dir_name)
    if size <= 100000:
        total_size_limited += size

print(f'Sum of total sizes of all directories with most 100000: {total_size_limited}')
