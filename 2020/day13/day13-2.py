#!/usr/bin/python3
# Advent of Code 2020 - Day 13, Part 2
# Benedikt Otto
#
import math

# input_file = '../examples/example_13.txt'
input_file = '../inputs/input_13.txt'

# Parse input.
bus_list = []
with open(input_file) as file:
    file.readline()  # we don't need the first line anymore.
    idx = 0
    for e in file.readline().strip().split(','):
        if e != 'x':
            bus = (int(e), idx)
            bus_list.append(bus)
        idx += 1

print(bus_list)

def extended_euclid(a: int, b: int):
    """
    Extended Euclidean Algorithm: Calculates the integers x and y so that we have
       a * x + b * y == gcd(a, b).
    Returns x, y and gcd(a, b).
    """
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1

    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    gcd = old_r
    x, y = old_s, old_t
    return x, y, gcd


# We need to find the value t such that for all buses (bus_num, idx) we have:
#   t + idx % bus_num == 0    or    t % bus_num == -idx
# We use the chinese remainder theorem and assume, that all bus numbers are coprime.
M = math.lcm(*(bus[0] for bus in bus_list))

result = 0
for bus_num, idx in bus_list:
    M_bus = M // bus_num
    # r_bus * bus_num + s_bus * M_bus == 1
    r_bus, s_bus, _ = extended_euclid(bus_num, M_bus)
    result += -idx * s_bus * M_bus

# Ensure that we have the smallest such timestamp.
result = result % M
print(f'Result: {result}')

# Sanity Check.
for bus_num, idx in bus_list:
    print(f'({result} - {idx}) % {bus_num} == {result + idx} % {bus_num} == {(result + idx) % bus_num}')
