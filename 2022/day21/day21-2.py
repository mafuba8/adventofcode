#!/usr/bin/python3
# Advent of Code 2022 - Day 21, Part 2
# Benedikt Otto
#
# Not happy with the solution, need to refactor it.

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


def reduce(monkey_name):
    """If the monkey evaluates to a number, return this number. If the monkey evaluates to a term
    that contains the variable 'humn', then it returns a list of inverse operations (None, op, int)
    or (int, op, None) that need to be applied in order to single out that variable. The list needs
    to be applied back-to-front (Stack).

    In that triple the value 'None' stands for the variable, e.g. (3, '-', None) means that we need to
    calculate '3 - x'."""
    monkey = monkey_dict[monkey_name]
    if monkey_name == 'humn':
        return []

    if isinstance(monkey, int):
        return monkey
    else:
        m1, op, m2 = monkey
        r1 = reduce(m1)
        r2 = reduce(m2)

        if isinstance(r1, int) and isinstance(r2, int):
            match op:
                case '+':
                    return r1 + r2
                case '-':
                    return r1 - r2
                case '*':
                    return r1 * r2
                case '/':
                    return r1 // r2

        x = (None, None, None)
        if isinstance(r1, list) and isinstance(r2, int):
            # r1 op <int>
            match op:
                case '+':
                    x = (None, '-', r2)
                case '-':
                    x = (None, '+', r2)
                case '*':
                    x = (None, '/', r2)
                case '/':
                    x = (None, '*', r2)
            return r1 + [x]

        if isinstance(r1, int) and isinstance(r2, list):
            # <int> op r2
            match op:
                case '+':
                    x = (None, '-', r1)
                case '-':
                    x = (r1, '-', None)
                case '*':
                    x = (None, '/', r1)
                case '/':
                    x = (None, '/', r1)
            return r2 + [x]

    return None


# Evaluate both sides of root.
root_monkey = monkey_dict['root']
m1, op, m2 = root_monkey
r1 = reduce(m1)
r2 = reduce(m2)

# We assume that exactly one side is an int and the other one a list.
# Apply all inverse operations of the variable-side to the number on the other side of 'root'.
result = 0
op_list = []
if isinstance(r1, int):
    result = r1
    op_list = r2
if isinstance(r2, int):
    result = r2
    op_list = r1

# Run through all inverse operations.
while len(op_list) > 0:
    left, op, right = op_list.pop()
    if left is None:
        # (None, op, right)
        match op:
            case '+':
                result = result + right
            case '-':
                result = result - right
            case '*':
                result = result * right
            case '/':
                result = result // right
    elif right is None:
        # (left, op, None)
        match op:
            case '+':
                result = left + result
            case '-':
                result = left - result
            case '*':
                result = left * result
            case '/':
                result = left // result

print(f'Number that (humn) needs to yell: {result}.')
