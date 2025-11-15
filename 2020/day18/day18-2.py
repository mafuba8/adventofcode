#!/usr/bin/python3
# Advent of Code 2020 - Day 18, Part 2
# Benedikt Otto
#

# input_file = '../examples/example_18.txt'
input_file = '../inputs/input_18.txt'

# Parse input into a list of expressions.
expressions = []
with open(input_file) as file:
    for line in file.readlines():
        # This time we actually want the newline in the expression.
        expressions.append(line)


# Dictionary with allowed operators and their priority.
operators = {'+': 3, '*': 2}

def parse_expression(expr):
    """Parses and evaluates the given expression using the Shunting Yard algorithm."""
    num_stack = []
    op_stack = []

    for c in expr:
        if c == ' ':
            # Ignore space characters.
            continue

        if str.isdigit(c):
            # Push digits to number stack.
            num_stack.append(int(c))

        if c in '+*':
            # Before adding the operator to the stack, work through all
            # operators on the top of the stack with >= priority.
            # (we assume that all operators are left-associative).
            while (len(op_stack) > 0 and op_stack[-1] != '('
                   and operators[op_stack[-1]] >= operators[c]):
                op_top = op_stack.pop()
                arg1 = num_stack.pop()
                arg2 = num_stack.pop()
                x = eval(f'{arg1} {op_top} {arg2}')
                num_stack.append(x)
            op_stack.append(c)

        if c == '(':
            # A left parenthesis get pushed to stack.
            op_stack.append(c)

        if c == ')':
            # A right parenthesis will clear all operations on the stack until we get the corresponding left one.
            while len(op_stack) > 0 and op_stack[-1] != '(':
                op_top = op_stack.pop()
                arg1 = num_stack.pop()
                arg2 = num_stack.pop()
                x = eval(f'{arg1} {op_top} {arg2}')
                num_stack.append(x)
            # Discard the corresponding opening bracket.
            op_stack.pop()

        if c == '\n':
            # Clean up remaining operator stack.
            while len(op_stack) > 0:
                op_top = op_stack.pop()
                arg1 = num_stack.pop()
                arg2 = num_stack.pop()
                x = eval(f'{arg1} {op_top} {arg2}')
                num_stack.append(x)

    assert len(num_stack) == 1 and len(op_stack) == 0
    return num_stack[0]


# Evaluate all expressions.
sum_of_results = 0
for expression in expressions:
    print(f'{expression.strip()} == {parse_expression(expression)}')
    sum_of_results += parse_expression(expression)

print(f'The sum of all results is {sum_of_results}.')
