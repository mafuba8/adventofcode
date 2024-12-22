#!/usr/bin/python3
# Advent of Code 2024 - Day 22, Part 1
# Benedikt Otto
#

# input_file = '../examples/example_22.txt'
input_file = '../inputs/input_22.txt'

# Parse input into list of integers.
initial_secret_numbers = []
with open(input_file) as file:
    for line in file.readlines():
        initial_secret_numbers.append(int(line.strip()))


def next_secret(secret):
    """Calculates the next secret from the given one."""
    k = secret * 64
    secret = k ^ secret
    secret = secret % 16777216

    k = secret // 32
    secret = k ^ secret
    secret = secret % 16777216

    k = secret * 2048
    secret = k ^ secret
    secret = secret % 16777216

    return secret


sum_of_final_secrets = 0
for secret in initial_secret_numbers:
    print(f'Initial secret: {secret}')
    # Generate 2000 numbers from each initial secret.
    for n in range(2000):
        secret = next_secret(secret)
    sum_of_final_secrets += secret
    print(f' => Secret after 2000 generations: {secret}')

print(f'Sum of all final secrets: {sum_of_final_secrets}')
