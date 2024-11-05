#!/usr/bin/python3
# Advent of Code 2022 - Day 11, Part 1
# Benedikt Otto
import re

# input_file = '../examples/example_11.txt'
input_file = '../inputs/input_11.txt'

# Define the Monkey class
class Monkey:
    """ Monkey Class
    self.inventory:     List of items in its inventory.
    self.operation:     Tuple, e.g. ('*', '1') or ('+', 'old').
    self.div_by:        Divisor for the divisibility check.
    self.throw_target:  Throw target, list [target_if_true, target_if_false]
    self.inspect_count: Counts the number of item inspects that the monkey did.
    """
    def __init__(self, inventory, operation, div_by, throw_target):
        self.inventory = inventory
        self.operation = operation
        self.div_by = div_by
        self.throw_target = throw_target
        self.inspect_count = 0
    def throw(self, item):
        """ Returns the throw target when the monkey holds the item. """
        if item % self.div_by == 0:
            return self.throw_target[0]
        else:
            return self.throw_target[1]
    def inspect(self, item):
        """ Monkey inspects the given item. Returns the new value of it. """
        self.inspect_count += 1
        op = self.operation[0]
        if self.operation[1] == 'old':
            match op:
                case '*':
                    item = item * item
                case '+':
                    item = item + item
        else:
            val = int(self.operation[1])
            match op:
                case '*':
                    item = item * val
                case '+':
                    item = item + val
        return item


# Regexes for the parsing nightmare.
re_monkey_num = re.compile(r'^Monkey\s(\d)+:$')
re_monkey_oper = re.compile(r'^\s{2}Operation:\snew\s=\sold\s([+|*])\s(\d+|old)$')
re_monkey_div_by = re.compile(r'^\s{2}Test:\sdivisible\sby\s(\d+)$')
re_monkey_throw = re.compile(r'^\s{4}If\s(true|false):\sthrow\sto\smonkey\s(\d)$')

# Parse input into list of monkeys.
monkey_list = []
with open(input_file) as file:
    for line in file.readlines():
        monkey_inventory = []
        match line[:6]:
            case 'Monkey':
                search_monkey_num = re_monkey_num.search(line)
                new_monkey = Monkey([], ['+', 0], 1, [0, 0])
                monkey = new_monkey
                monkey_list.append(new_monkey)

            case '  Star':
                i_list = line.split(':')[1]
                for i in i_list.split(','):
                    monkey_inventory.append(int(i))
                monkey.inventory = monkey_inventory

            case '  Oper':
                search_oper = re_monkey_oper.search(line)
                monkey_oper = search_oper.group(1)
                monkey_oper_num = search_oper.group(2)
                monkey.operation = [monkey_oper, monkey_oper_num]

            case '  Test':
                search_div_by = re_monkey_div_by.search(line)
                monkey_div_by = search_div_by.group(1)
                monkey.div_by = int(monkey_div_by)

            case '    If':
                search_throw = re_monkey_throw.search(line)
                if search_throw.group(1) == 'true':
                    throw_true = search_throw.group(2)
                    monkey.throw_target[0] = int(throw_true)
                elif search_throw.group(1) == 'false':
                    throw_false = search_throw.group(2)
                    monkey.throw_target[1] = int(throw_false)


# Execute the game rounds.
for game_round in range(20):
    for monkey in monkey_list:
        while len(monkey.inventory) > 0:
            # Monkey grabs new item, inspects it and gets bored with it.
            game_item = monkey.inventory.pop(0)
            game_item = monkey.inspect(game_item)
            game_item = game_item // 3

            # Monkey throws item.
            game_throw_target = monkey.throw(game_item)
            monkey_list[game_throw_target].inventory.append(game_item)

    print(f'After round {game_round + 1}, the monkeys are holding items with these worry levels:')
    for monkey in monkey_list:
        print(f'Monkey {monkey_list.index(monkey)}:' , monkey.inventory)
    print()

# Get total inspect count of all monkeys:
inspect_count_list = [monkey.inspect_count for monkey in monkey_list]
inspect_count_list.sort()
print(f'Top two inspect counts: {inspect_count_list[-1]}, {inspect_count_list[-2]}')
print(f'Level of monkey business: {inspect_count_list[-1] * inspect_count_list[-2]}')
