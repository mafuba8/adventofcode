#!/usr/bin/python3
# Advent of Code 2020 - Day 8, Part 2
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


def check_terminate(ins_list):
    # We remember instruction indices to see when the program repeats.
    instruction_history = []

    # Run through instructions.
    instruction_pointer = 0
    accumulator = 0
    while True:
        # Check if the execution reached the end of the code.
        if instruction_pointer >= len(ins_list):
            return True, accumulator

        # Check if a previous instruction is being executed again.
        if instruction_pointer in instruction_history:
            return False, accumulator

        instruction_history.append(instruction_pointer)

        # Execute the instruction.
        op, num = ins_list[instruction_pointer]
        match op:
            case 'acc':
                accumulator += num
                instruction_pointer += 1
            case 'jmp':
                instruction_pointer += num
            case 'nop':
                instruction_pointer += 1


# Get all the instruction indices with a 'jmp' or 'nop' instruction.
potential_indices = [idx for idx in range(len(instruction_list)) if instruction_list[idx][0] in ('nop', 'jmp')]

# Check if swapping one index leads to the program terminating.
for idx in potential_indices:
    # Swap nop and jmp instruction at this index only.
    new_ins_list = instruction_list.copy()
    op, num = instruction_list[idx]
    match op:
        case 'nop':
            new_ins_list[idx] = ('jmp', num)
        case 'jmp':
            new_ins_list[idx] = ('nop', num)

    does_terminate, acc = check_terminate(new_ins_list)
    if does_terminate:
        print(f'Swapping {idx} leads to the program terminating.')
        print(f'Final value in the accumulator: {acc}')
        break
