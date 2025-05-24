#!/usr/bin/python3
# Advent of Code 2022 - Day 21, Part 1
# Benedikt Otto
#

# input_file = '../examples/example_21.txt'
input_file = '../inputs/input_21.txt'

# Parse input into dict(key=name, val=int or tuple)
monkey_dict = {}
with open(input_file) as file:
    for line in file.readlines():
        name, job = line.strip().split(': ')
        if job.isdecimal():
            monkey_dict.setdefault(name, int(job))
        else:
            m1, op, m2 = job.split(' ')
            monkey_dict.setdefault(name, (m1, op, m2))


def evaluate_monkey(monkey_name):
    """Returns the number the given monkey will yell."""
    monkey = monkey_dict[monkey_name]
    if isinstance(monkey, int):
        return monkey
    else:
        m1, op, m2 = monkey
        x1 = evaluate_monkey(m1)
        x2 = evaluate_monkey(m2)
        match op:
            case '+':
                return x1 + x2
            case '-':
                return x1 - x2
            case '*':
                return x1 * x2
            case '/':
                return x1 // x2
    return None


print(f'The root monkey will yell {evaluate_monkey('root')}.')
