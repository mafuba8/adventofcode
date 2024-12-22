#!/usr/bin/python3
# Advent of Code 2024 - Day 22, Part 2
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


def get_sequence(idx, banana_prices):
    """Returns the sequences of changes in the given banana_prices list,
     starting at the given index, where idx >= 4."""
    window = banana_prices[idx-4:idx+1]
    changes_window = []
    for k in range(4):
        changes_window.append(window[k+1] - window[k])

    return changes_window


# Build a list of dictionaries that give us the number of bananas for each sequence.
changes_dict_list = []
for secret in initial_secret_numbers:
    banana_prices = [secret % 10]
    # Generate 2000 numbers from each initial secret and the banana prices.
    for n in range(2000):
        secret = next_secret(secret)
        banana_prices.append(secret % 10)

    # Build dict(key=(a, b, c, d), val=banana_count).
    changes_dict = {}
    for n in range(4, len(banana_prices)):
        t = tuple(get_sequence(n, banana_prices))
        # This is to make sure that we only get the first occurence of the sequence.
        if t not in changes_dict:
            changes_dict.setdefault(t, banana_prices[n])

    changes_dict_list.append(changes_dict)


# Run through all sequence combinations and check how many bananas we can get.
max_bananas = 0
max_sequence = (0, 0, 0, 0)
for a in range(-9, 9 + 1):
    for b in range(-9, 9 + 1):
        for c in range(-9, 9 + 1):
            for d in range(-9, 9 + 1):
                t = (a, b, c, d)
                total_bananas = 0
                for buyer_dict in changes_dict_list:
                    if t in buyer_dict:
                        total_bananas += buyer_dict[t]
                if total_bananas > max_bananas:
                    max_bananas = total_bananas
                    max_sequence = t
                    print(f'Nex Maximum: {max_bananas} @ {max_sequence}')

print(f'The maximum number of bananas we can obtain is {max_bananas} with the sequence {max_sequence}.')
