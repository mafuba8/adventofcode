#!/usr/bin/python3
# Advent of Code 2022 - Day 17, Part 1
# Benedikt Otto

# input_file = '../examples/example_17.txt'
input_file = '../inputs/input_17.txt'

# Number of rocks that are simulated.
NUM_ROCKS=2022

with open(input_file) as file:
    jet_pattern = file.readline().strip()

# Global area with pixels, as a dict(key=xy, val=pixel).
area = {}

class Rock:
    def __init__(self, base_pixels, offset_col):
        self.pixels = []
        for p in base_pixels:
            self.pixels.append((3 + p[0] + offset_col, 2 + p[1]))

    def jet_push(self, direction):
        """Modifies the <self.pixels> values according to the direction.
        If the push results in it hitting something, no values are changed."""
        y_dir = 0
        match direction:
            case '>':
                y_dir = 1
            case '<':
                y_dir = -1

        # Determine pixel positions when pushed by the jet.
        new_pixels = []
        for p in self.pixels:
            new_pos = (p[0], p[1] + y_dir)
            new_pixels.append(new_pos)

        # Check if the new position would hit the wall or another rock.
        movable = True
        for p in new_pixels:
            if p[1] < 0 or p[1] > 6 or p in area:
                movable = False
                break
        if movable:
            self.pixels = new_pixels

    def move_down(self):
        """Moves all pixels of the rock down once, returning True if it worked. If the move results in it
        hitting something, no values are changed, returns False instead."""
        # Determine pixel positions when moved one pixel down.
        new_pixels = []
        for p in self.pixels:
            new_pos = (p[0] - 1, p[1])
            new_pixels.append(new_pos)

        # Check if the new position would hit the wall or another rock.
        movable = True
        for p in new_pixels:
            if p[0] < 0 or p in area:
                movable = False
        if movable:
            self.pixels = new_pixels
            return True
        else:
            return False


# Types of rocks, with its points relative to bottom-left pixel (0,0).
rock_row = [(0,0), (0,1), (0,2), (0,3)]
rock_plus = [(0,1), (1,0), (1,1), (1,2), (2,1)]
rock_corner = [(0,0), (0,1), (0,2), (1,2), (2,2)]
rock_col = [(0,0), (1,0), (2,0), (3,0)]
rock_square = [(0,0), (0,1), (1,0), (1,1)]
base_rock_tiles = [rock_row, rock_plus, rock_corner, rock_col, rock_square]

# Offset defines the highest row with a block in it. Then the Floor is -1.
offset = -1
jet_num = 0
for rock_num in range(NUM_ROCKS):
    # New rock starts falling.
    rock = Rock(base_rock_tiles[rock_num % 5], offset + 1)

    # Simulate the falling rock.
    movable = True
    while movable:
        # Rock gets pushed by the next jet.
        jet = jet_pattern[jet_num]
        #print(f' Push rock {jet}')
        rock.jet_push(jet)
        jet_num = (jet_num + 1) % len(jet_pattern)

        # Rock falls down one row.
        #print(' Move Rock down')
        movable = movable and rock.move_down()

    # Rock stopped falling and its pixels get saved to the area dict.
    for p in rock.pixels:
        area.setdefault(p, '#')

    # Save the highest occupied row as new offset.
    for p in area.keys():
        offset = max(offset, p[0])


print(f'Height of Tower after {NUM_ROCKS} rocks have fallen: {offset + 1}')
