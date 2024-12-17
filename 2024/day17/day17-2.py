#!/usr/bin/python3
# Advent of Code 2024 - Day 17, Part 1
# Benedikt Otto
#
# The solution builds on the following observation:
#  The program produces one output per cycle, and the output of one cycle only depends
#  on the value of register A at that time. Also, when looking at the input values in octal,
#  we see that an input with the same (octal) prefix leads to the same (octal) suffix, i.e.:
#    run_program(0o1) = 0  |  run_program(0o10) = 3,0  |  run_program(0o100) = 1,3,0
#    run_program(0o2) = 1  |  run_program(0o20) = 5,1  |  run_program(0o200) = 1,5,1
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
instruction_pointer = 0
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
            #print(f'0 (adv) {operand} - Register A = {register_a} // {denominator} = {int(register_a / denominator)}')
            register_a = int(register_a / denominator)
            instruction_pointer += 2
        case 1:
            # bxl instruction (bitwise XOR)
            #print(f'1 (bxl) {operand} - Register B = {register_b} ^ {operand} = {register_b ^ operand}')
            register_b = register_b ^ operand
            instruction_pointer += 2
        case 2:
            # bst instruction (set B register)
            #print(f'2 (bst) {operand} - Register B = {combo(operand)} % 8 = {combo(operand) % 8}')
            register_b = combo(operand) % 8
            instruction_pointer += 2
        case 3:
            # jnz instruction (jump if A nonzero)
            if register_a != 0:
                instruction_pointer = operand
                #print(f'3 (jnz) {operand} - A nonzero > Jump to {operand}')
            else:
                #print(f'3 (jnz) {operand} - A zero > Do not jump.')
                instruction_pointer += 2
        case 4:
            # bxc instruction (bitwise XOR)
            #print(f'4 (bxc) {operand} - Register B = {register_b} ^ {register_c} = {register_b ^ register_c}')
            register_b = register_b ^ register_c
            instruction_pointer += 2
        case 5:
            # out instruction
            output += str(combo(operand) % 8) + ','
            #print(f'5 (out) {operand} - Output {combo(operand) % 8}')
            instruction_pointer += 2
        case 6:
            # bdv instruction (B division)
            denominator = 2 ** combo(operand)
            #print(f'6 (bdv) {operand} - Register B = {register_a} // {denominator} = {int(register_a / denominator)}')
            register_b = int(register_a / denominator)
            instruction_pointer += 2
        case 7:
            # cdv instruction (C division)
            denominator = 2 ** combo(operand)
            #print(f'7 (cdv) {operand} - Register C = {register_a} // {denominator} = {int(register_a / denominator)}')
            register_c = int(register_a / denominator)
            instruction_pointer += 2


def run_program(reg_a):
    """Runs the program where the register A is set to reg_a, and all other registers
    are set to 0."""
    global register_a, register_b, register_c, instruction_pointer, output
    instruction_pointer = 0
    output = ''
    register_a = reg_a
    register_b = 0
    register_c = 0
    while instruction_pointer < len(program):
        opcode = program[instruction_pointer]
        operand = program[instruction_pointer + 1]
        execute_instruction(opcode, operand)
    output = output[:-1]  # remove trailing comma
    return output


# Return a list of input prefixes that will lead to an output with the given output suffix,
# i.e.  find_prefixes([0, 3, 3, 0]) == ['1035', '1065']
def find_prefixes(output_suffix):
    """For a given output suffix, return a list of input prefixes"""
    if len(output_suffix) == 0:
        return ['']

    prefixes = []
    for prefix in find_prefixes(output_suffix[1:]):
        for digit in range(0, 8):
            # We append the digit to the prefix and interpret that as a new octal number.
            s = prefix + str(digit)
            input = int(s, 8)  # as octal number.
            # Check if this input yields to the wanted output.
            output = run_program(input)
            output = [int(x) for x in output.split(',')]
            if output == output_suffix:
                prefixes.append(s)
    return prefixes


# Find all prefixes that return the program code as output.
working_prefixes = find_prefixes(program)

print('The following prefixes give the program code as output:')
for prefix_oct in working_prefixes:
    prefix_dec = int(prefix_oct, 8)
    print(f'Octal: {prefix_oct} - Decimal: {prefix_dec}')

min_prefix = min([int(x, 8) for x in working_prefixes])
print(f'Smallest prefix that works: {min_prefix}')
