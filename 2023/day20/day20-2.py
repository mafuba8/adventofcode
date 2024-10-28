#!/usr/bin/python3
# Advent of Code 2023 - Day 20, Part 2
import math

HIGH = 'high'
LOW = 'low'
high_pulse_count = 0
low_pulse_count = 0

# Open puzzle file and parse it.
input_list = []
#with open('example_20-2.txt') as file:
with open('../inputs/input_20.txt') as file:
    lines = file.read().split('\n')
    del lines[-1]
    for line in lines:
        li = line.split(' -> ')
        module_name = li[0]
        dest_modules = li[1].split(', ')
        input_list.append((module_name, dest_modules))


class Broadcaster():
    def __init__(self, dest_modules):
        self.name = 'broadcaster'
        self.dest_modules = dest_modules

    def pulse(self, initiator, pulse):
        for dest_name in self.dest_modules:
            event = (self.name, pulse, dest_name)
            queue.append(event)


class FlipFlop():
    def __init__(self, name, dest_modules):
        self.name = name
        self.state = 'OFF'
        self.dest_modules = dest_modules

    def pulse(self, initiator, pulse):
        if pulse == LOW:
            if self.state == 'OFF':
                self.state = 'ON'
                for dest_name in self.dest_modules:
                    event = (self.name, HIGH, dest_name)
                    queue.append(event)
            elif self.state == 'ON':
                self.state = 'OFF'
                for dest_name in self.dest_modules:
                    event = (self.name, LOW, dest_name)
                    queue.append(event)


class Conjunction():
    def __init__(self, name, dest_modules):
        self.name = name
        self.input_states = {}
        self.dest_modules = dest_modules

    def pulse(self, initiator, pulse):
        self.input_states[initiator] = pulse
        if all([s == HIGH for s in self.input_states.values()]):
            for dest_name in self.dest_modules:
                event = (self.name, LOW, dest_name)
                queue.append(event)
        else:
            for dest_name in self.dest_modules:
                event = (self.name, HIGH, dest_name)
                queue.append(event)


# Parse input_list into dict of modules.
# Dictionary with key=module_name, val=ModuleObject.
module_dict = {}
module_dict.setdefault('output', FlipFlop('output', []))  # Untyped module for example_20-2.txt.
module_dict.setdefault('rx', FlipFlop('rx', []))  # Untyped module for input_20.txt.

for input in input_list:
    (module_name, dest_modules) = input
    if module_name == 'broadcaster':
        name = 'broadcaster'
        module = Broadcaster(dest_modules)

    elif module_name[0] == '%':
        name = module_name[1:]
        module = FlipFlop(name, dest_modules)

    elif module_name[0] == '&':
        name = module_name[1:]
        module = Conjunction(name, dest_modules)

    module_dict.setdefault(module.name, module)

# Set input_states on all Conjunction modules.
for module_name in module_dict:
    module = module_dict[module_name]

    for dest_name in module.dest_modules:
        dest_module = module_dict[dest_name]
        if isinstance(dest_module, Conjunction):
            dest_module.input_states[module_name] = LOW


def send_pulse(initiator_name, module_name, pulse):
    """Handles a single pulse as it appears in the queue."""
    # print(f'{initiator_name} -{pulse}-> {module_name}')
    global high_pulse_count
    global low_pulse_count
    if pulse == HIGH:
        high_pulse_count += 1
    if pulse == LOW:
        low_pulse_count += 1
    module = module_dict[module_name]
    module.pulse(initiator_name, pulse)


# Event queue for the button presses.
queue = []
NUM_BUTTON_PRESSES = 100000

# Since 'rx' has the single input 'lv' and 'lv' has the four inputs 'st', 'tn', 'hh', 'dt',
# we track the least amount of button presses necessary for them to recieve a LOW pulse.
min_st = None
min_tn = None
min_hh = None
min_dt = None

# Process each button press and simulate the pulses.
for k in range(NUM_BUTTON_PRESSES):
    # print(f'!!Button press #{k}...')
    queue.append(('button', LOW, 'broadcaster'))  # Button press.
    while len(queue) > 0:  # Simulate until all pulses are resolved.
        (initiator_name, pulse, module_name) = queue.pop(0)

        # Find least amount of button presses needed to get a LOW pulse to the respective modules.
        if module_name == 'st' and pulse == LOW and min_st is None:
            min_st = k + 1
        if module_name == 'tn' and pulse == LOW and min_tn is None:
            min_tn = k + 1
        if module_name == 'hh' and pulse == LOW and min_hh is None:
            min_hh = k + 1
        if module_name == 'dt' and pulse == LOW and min_dt is None:
            min_dt = k + 1

        send_pulse(initiator_name, module_name, pulse)


print('-----')
print(f'#Low_pulses: {low_pulse_count}, #High_pulses: {high_pulse_count}')
print(f'Multiplied together: {low_pulse_count * high_pulse_count}')
print('-----')
# The minimum number of button presses for rx = LOW is the least common multiple of min_st, min_tn, min_hh and min_dt.
print(f'Minimum button presses for st/tn/hh/dt low: {min_st}/{min_tn}/{min_hh}/{min_dt}')
print(f'Minimum button presses for rx: {math.lcm(min_st, min_tn, min_hh, min_dt)}')
