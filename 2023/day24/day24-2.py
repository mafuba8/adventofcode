#!/usr/bin/python3
# Advent of Code 2023 - Day 24, Part 2
# Benedikt Otto
import re
import numpy

# Open puzzle file and parse into list of tuples.
hailstone_list = []
regex = re.compile(r'(\d+),\s(\d+),\s(\d+)\s@\s+(-?\d+),\s+(-?\d+),\s+(-?\d+)')
#with open('example_24.txt') as file:
with open('../inputs/input_24.txt') as file:
    for line in file.readlines():
        search = regex.search(line.strip())
        hailstone = (int(search.group(1)), int(search.group(2)), int(search.group(3)),
                     int(search.group(4)), int(search.group(5)), int(search.group(6)))
        hailstone_list.append(hailstone)


def cross_matrix(vector):
    vec0 = vector[0]
    vec1 = vector[1]
    vec2 = vector[2]
    return numpy.array([[0, -vec2, vec1], [vec2, 0, -vec0], [-vec1, vec0, 0]])


# Please make coding problems, not linear algebra problems...
# As in https://github.com/alxmk/adventofcode/blob/master/2023/day24/main.go
# inspired by https://www.reddit.com/r/adventofcode/comments/18pnycy/comment/kepu26z/
h0 = numpy.array(hailstone_list[0][:3])
v0 = numpy.array(hailstone_list[0][3:])
h1 = numpy.array(hailstone_list[1][:3])
v1 = numpy.array(hailstone_list[1][3:])
h2 = numpy.array(hailstone_list[2][:3])
v2 = numpy.array(hailstone_list[2][3:])

s1 = numpy.cross(h1, v1) - numpy.cross(h0, v0)
s2 = numpy.cross(h2, v2) - numpy.cross(h0, v0)

rhs = numpy.array([s1[0], s1[1], s1[2], s2[0], s2[1], s2[2]])

m00 = cross_matrix(v0) - cross_matrix(v1)
m03 = cross_matrix(v0) - cross_matrix(v2)
m30 = cross_matrix(h1) - cross_matrix(h0)
m33 = cross_matrix(h2) - cross_matrix(h0)

m = numpy.array([
    [m00[0][0], m00[0][1], m00[0][2], m30[0][0], m30[0][1], m30[0][2]],
    [m00[1][0], m00[1][1], m00[1][2], m30[1][0], m30[1][1], m30[1][2]],
    [m00[2][0], m00[2][1], m00[2][2], m30[2][0], m30[2][1], m30[2][2]],
    [m03[0][0], m03[0][1], m03[0][2], m33[0][0], m33[0][1], m33[0][2]],
    [m03[1][0], m03[1][1], m03[1][2], m33[1][0], m33[1][1], m33[1][2]],
    [m03[2][0], m03[2][1], m03[2][2], m33[2][0], m33[2][1], m33[2][2]]])

b = numpy.linalg.inv(m)
result = numpy.dot(b, rhs)

print(f'Throw coordinates: ({round(result[0])}, {round(result[1])}, {round(result[2])}')
print(f'Sum: {round(result[0] + result[1] + result[2])}')
