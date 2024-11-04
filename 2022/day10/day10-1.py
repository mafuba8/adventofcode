#!/usr/bin/python3
# Advent of Code 2022 - Day 10, Part 1
# Benedikt Otto

# input_file = '../examples/example_10.txt'
input_file = '../inputs/input_10.txt'

# Start value of the register
register_x = 1

# Instructions modeled as classes.
class Instruction:
    def __init__(self, cycles):
        self.cycles = cycles
    def __str__(self):
        pass
    def execute(self):
        pass

class Noop(Instruction):
    def __init__(self):
        super().__init__(1)
    def __str__(self):
        return 'Noop'
    def execute(self):
        pass

class AddX(Instruction):
    def __init__(self, value):
        super().__init__(2)
        self.value = value
    def __str__(self):
        return f'AddX({self.value})'
    def execute(self):
        global register_x
        register_x += self.value


# Parse input into list of Instructions:
instruction_list = []
with open(input_file) as file:
    for line in file.readlines():
        l = line.strip().split(' ')
        cmd = l[0]
        if cmd == 'noop':
            instr = Noop()
            instruction_list.append(instr)
        elif cmd == 'addx':
            instr = AddX(int(l[1]))
            instruction_list.append(instr)


# Sum of the signal strengths.
signal_strength_sum = 0

# Iterate through cycles until all instructions are executed.
cycle_num = 1
current_instruction = instruction_list.pop(0)  # Prepare first instruction.
while len(instruction_list) > 0 or current_instruction.cycles > 0:
    # Start Cycle.
    current_instruction.cycles -= 1

    # During Cycle.
    signal_strength = cycle_num * register_x
    if cycle_num in (20, 60, 100, 140, 180, 220):
            print(f'Cycle {cycle_num}:')
            print(f'> Signal Strength: {signal_strength}')
            signal_strength_sum += signal_strength

    # After Cycle.
    if current_instruction.cycles == 0:
        # Necessary cycles for instruction execution are completed.
        current_instruction.execute()

        # Set next instruction
        if len(instruction_list) > 0:
            new_instr = instruction_list.pop(0)
            current_instruction = new_instr

    cycle_num += 1


print(f'Sum of Signal Strengths: {signal_strength_sum}')
