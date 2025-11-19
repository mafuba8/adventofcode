#!/usr/bin/python3
# Advent of Code 2021 - Day 21, Part 1
# Benedikt Otto
#

# input_file = '../examples/example_21.txt'
input_file = '../inputs/input_21.txt'

with open(input_file) as file:
    for line in file.readlines():
        if 'Player 1' in line:
            p1_position = int(line.split(': ')[1])
        if 'Player 2' in line:
            p2_position = int(line.split(': ')[1])

# Remember the dice roll.
dice_last_roll = 100

def roll_dice():
    """Rolls the 100-sided deterministic dice and returns its value."""
    global dice_last_roll
    roll = dice_last_roll % 100 + 1
    dice_last_roll = roll
    return roll


def do_turn(pos):
    """Simulates one turn and returns the board position after the turn."""
    global dice_last_roll
    r1, r2, r3 = roll_dice(), roll_dice(), roll_dice()
    forward = r1 + r2 + r3
    new_pos = (pos - 1 + r1 + r2 + r3) % 10 + 1
    print(f' Player rolls {r1}+{r2}+{r3} and moves to space {new_pos}.')
    return new_pos


# Play the game until one player reaches 1000 points.
num_rolls = 0
p1_score = 0
p2_score = 0
while True:
    # Player 1 rolls the dice.
    num_rolls += 3
    p1_position = do_turn(p1_position)
    p1_score += p1_position
    if p1_score >= 1000:
        print(f'Player 1 has reached 1000 points and wins.')
        break

    # Player 2 rolls the dice.
    num_rolls += 3
    p2_position = do_turn(p2_position)
    p2_score += p2_position
    if p2_score >= 1000:
        print(f'Player 2 has reached 1000 points and wins.')
        break

print()
print(f'Final score after {num_rolls} rolls:')
print(f'  Player 1: {p1_score}')
print(f'  Player 2: {p2_score}')

losing_score = min(p1_score, p2_score)
print(f'Result: {losing_score * num_rolls}')
