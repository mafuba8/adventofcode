#!/usr/bin/python3
# Advent of Code 2022 - Day 18, Part 2
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

    def __eq__(self, other):
        return self.coords == other.coords

    def __hash__(self):
        return hash(str(self.coords))


# Parse input into list of Cubes.
cube_list = []
x_max, y_max, z_max = 0, 0, 0
x_min, y_min, z_min = 1000, 1000, 1000
with open(input_file) as file:
    for line in file.readlines():
        x, y, z = tuple([int(s) for s in line.strip().split(',')])
        cube_list.append(Cube(x, y, z))
        x_max = max(x, x_max)
        y_max = max(y, y_max)
        z_max = max(z, z_max)
        x_min = min(x, x_min)
        y_min = min(y, y_min)
        z_min = min(z, z_min)


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


# Flood-Fill from a cube outside the droplet to the whole set of 'air' cubes around it.
start = Cube(x_min-1, y_min-1, z_min-1)  # Guaranteed to be outside droplet.
environment = set()
stack = [start]
while len(stack) > 0:
    c = stack.pop()
    cx, cy, cz = c.coords
    # See if the cube is not part of the droplet but still within the search area.
    in_search_area = x_min-1 <= cx <= x_max+1 and y_min-1 <= cy <= y_max+1 and z_min-1 <= cz <= z_max+1
    if c not in cube_list and in_search_area:
        environment.add(c)
        # Check all adjacent cubes of c.
        neighb = [(cx+1, cy, cz), (cx-1, cy, cz), (cx, cy+1, cz),
                  (cx, cy-1, cz), (cx, cy, cz+1), (cx, cy, cz-1)]
        for coord in neighb:
            neigh = Cube(*coord)
            if neigh not in environment:
                stack.append(neigh)

# Find out which droplet sides are also sides of the environment.
exterior_sides = []
for c in environment:
    for s in c.get_sides():
        if s in exposed_sides:
            exterior_sides.append(s)

print(f'Number of sides that are on the exterior: {len(exterior_sides)}')
