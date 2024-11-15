#!/usr/bin/python3
# Advent of Code 2022 - Day 18, Part 1
# Benedikt Otto

# input_file = '../examples/example_18.txt'
input_file = '../inputs/input_18.txt'

# Class definition for a side, defined through its four corner coordinates.
class Side:
    def __init__(self, c1, c2, c3, c4):
        self.corners = {c1, c2, c3, c4}

    def __eq__(self, other):
        return self.corners == other.corners

# Class definition for a cube, defined through its base coordinate.
class Cube:
    def __init__(self, x, y, z):
        self.coords = (x, y, z)

    def get_sides(self):
        x, y, z = self.coords
        s1 = Side((x,y,z), (x,y+1,z), (x,y,z+1), (x,y+1,z+1))
        s2 = Side((x,y,z), (x,y,z+1), (x+1,y,z), (x+1,y,z+1))
        s3 = Side((x,y,z), (x,y+1,z), (x+1,y,z), (x+1,y+1,z))
        s4 = Side((x+1,y,z), (x+1,y+1,z), (x+1,y,z+1), (x+1,y+1,z+1))
        s5 = Side((x,y+1,z), (x,y+1,z+1), (x+1,y+1,z), (x+1,y+1,z+1))
        s6 = Side((x,y,z+1), (x,y+1,z+1), (x+1,y,z+1), (x+1,y+1,z+1))
        return s1, s2, s3, s4, s5, s6


# Parse input into list of Cubes.
cube_list = []
with open(input_file) as file:
    for line in file.readlines():
        x, y, z = tuple([int(s) for s in line.strip().split(',')])
        cube_list.append(Cube(x, y, z))


# Create list of exposed sides.
# If another cube with an already exposed side gets added,
# we remove this side from the exposed list.
exposed_sides = []
for cube in cube_list:
    for side in cube.get_sides():
        if side in exposed_sides:
            exposed_sides.remove(side)
        else:
            exposed_sides.append(side)

print(f'Total surface area: {len(exposed_sides)}')
