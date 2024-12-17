#!/usr/bin/python3
# Advent of Code 2024 - Day 17, Part 1
# Benedikt Otto
#
import re

# input_file = '../examples/example_17.txt'
input_file = '../inputs/input_17.txt'

# Parse input.
regex_reg_a = re.compile(r'^Register\sA:\s(\d+)$')
regex_reg_b = re.compile(r'^Register\sB:\s(\d+)$')
regex_reg_c = re.compile(r'^Register\sC:\s(\d+)$')
regex_prog = re.compile(r'^Program:\s([\d,]*)$')

register_a = 0
register_b = 0
register_c = 0
program = []
with open(input_file) as file:
    for line in file.readlines():
        search_a = regex_reg_a.search(line)
        if search_a:
            register_a = int(search_a.group(1))
        search_b = regex_reg_b.search(line)
        if search_b:
            register_b = int(search_b.group(1))
        search_c = regex_reg_c.search(line)
        if search_c:
            register_c = int(search_c.group(1))
        search_pr = regex_prog.search(line)
        if search_pr:
            program = search_pr.group(1).split(',')
    program = [int(x) for x in program]


def combo(operand):
    """Returns the contents of the combo operands."""
    global register_a, register_b, register_c
    match operand:
        case 0: return 0
        case 1: return 1
        case 2: return 2
        case 3: return 3
        case 4: return register_a
        case 5: return register_b
        case 6: return register_c
        case 7: return None


def execute_instruction(opcode, operand):
    """Executes the given instruction opcode-operand pair. Modifies the registers, output
    and the instruction pointers as necessary."""
    global register_a, register_b, register_c, instruction_pointer, output
    match opcode:
        case 0:
            # adv instruction (A division)
            denominator = 2 ** combo(operand)
            register_a = int(register_a / denominator)
            instruction_pointer += 2
        case 1:
            # bxl instruction (bitwise XOR)
            register_b = register_b ^ operand
            instruction_pointer += 2
        case 2:
            # bst instruction (set B register)
            register_b = combo(operand) % 8
            instruction_pointer += 2
        case 3:
            # jnz instruction (jump if A nonzero)
            if register_a != 0:
                instruction_pointer = operand
            else:
                instruction_pointer += 2
        case 4:
            # bxc instruction (bitwise XOR)
            register_b = register_b ^ register_c
            instruction_pointer += 2
        case 5:
            # out instruction
            output += str(combo(operand) % 8) + ','
            instruction_pointer += 2
        case 6:
            # bdv instruction (B division)
            denominator = 2 ** combo(operand)
            register_b = int(register_a / denominator)
            instruction_pointer += 2
        case 7:
            # cdv instruction (C division)
            denominator = 2 ** combo(operand)
            register_c = int(register_a / denominator)
            instruction_pointer += 2


# Execute program.
instruction_pointer = 0
output = ''

while instruction_pointer < len(program):
    opcode = program[instruction_pointer]
    operand = program[instruction_pointer + 1]
    execute_instruction(opcode, operand)

output = output[:-1]  # remove trailing comma
print(f'Final register: {register_a} / {register_b} / {register_c}')
print(f'Output of the program: {output}')
