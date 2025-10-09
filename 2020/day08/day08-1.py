#!/usr/bin/python3
# Advent of Code 2020 - Day 8, Part 1
# Benedikt Otto
#

# input_file = '../examples/example_8.txt'
input_file = '../inputs/input_8.txt'

# Parse input into a list of instructions. An instruction is a tuple (op, num).
instruction_list = []
with open(input_file) as file:
    for line in file.readlines():
        op, num = line.strip().split(' ')
        instruction = (op, int(num))
        instruction_list.append(instruction)


# We remember instruction indices to see when the program repeats.
instruction_history = []

# Run through instructions.
instruction_pointer = 0
accumulator = 0
while True:
    # Stop when the instruction has been executed before.
    if instruction_pointer in instruction_history:
        break
    instruction_history.append(instruction_pointer)

    # Execute the instruction.
    op, num = instruction_list[instruction_pointer]
    match op:
        case 'acc':
            accumulator += num
            instruction_pointer += 1
        case 'jmp':
            instruction_pointer += num
        case 'nop':
            instruction_pointer += 1
    print(f'{op} {num} -> IP: {instruction_pointer}, ACC: {accumulator}')

print(f'Value in the accumulator right before an instruction is executed a second time: {accumulator}.')
