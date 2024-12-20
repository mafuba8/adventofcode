#!/usr/bin/python3
# Advent of Code 2024 - Day 20, Part 1
# Benedikt Otto
#

# input_file = '../examples/example_20.txt'
input_file = '../inputs/input_20.txt'

# CHEAT_THRESHOLD = 1
CHEAT_THRESHOLD = 100

# Parse input into dict(key=xy, val=char)
racetrack_map = {}
start_tile, end_tile = (0, 0), (0, 0)
with open(input_file) as file:
    for row_num, row in enumerate(file.readlines()):
        for col_num, char in enumerate(row.strip()):
            if char == 'S':
                start_tile = (row_num, col_num)
                racetrack_map.setdefault((row_num, col_num), '.')
            elif char == 'E':
                end_tile = (row_num, col_num)
                racetrack_map.setdefault((row_num, col_num), '.')
            else:
                racetrack_map.setdefault((row_num, col_num), char)


# Find the normal (un-cheated) path.
normal_path = [start_tile]
while normal_path[-1] != end_tile:
    x, y = normal_path[-1]
    for n in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
        if racetrack_map[n] == '.' and n not in normal_path:
            normal_path.append(n)
            break  # We know that there is only one path from S to E.

# Time of the normal path.
normal_time = len(normal_path) - 1  # tile count is always one more than step count.
print(f'Normal track time: {normal_time}')


# Find all cheats and their saved time.
cheat_time_saved_count = {}
for cheat_start in normal_path:
    x, y = cheat_start

    # Check what possible cheats we get when we decide to use the cheat at cheat_start.
    idx = normal_path.index(cheat_start)
    path_so_far = normal_path[:idx]
    path_rest = normal_path[idx + 1:]

    # The following 8 tiles are reachable in two steps from (x, y).
    reachable = [(x-2, y),
                 (x-1, y-1), (x-1, y+1),
                 (x, y-2), (x, y+2),
                 (x+1, y-1), (x+1, y+1),
                 (x+2, y)]
    cheat_steps = 2

    for r in reachable:
        # We only save time when we use the cheat to jump to a later part of the track.
        if r in path_rest:
            # One possible cheat. Find the new time when we run the path
            #   [path_so_far] -> cheat_start -> # -> r -> [path_after_cheat]
            idx_cheat = normal_path.index(r)
            path_after_cheat = normal_path[idx_cheat:]

            # Time spent for the race when we use the new cheated path.
            cheating_path_time = len(path_so_far) + cheat_steps + len(path_after_cheat) - 1

            # Record the cheats if we save enough time.
            time_saved = normal_time - cheating_path_time
            if time_saved >= CHEAT_THRESHOLD:
                print(f' Possible cheat: {cheat_start} -> {r} - Time: {cheating_path_time} ({time_saved} saved)')
                cheat_time_saved_count.setdefault(time_saved, 0)
                cheat_time_saved_count[time_saved] = cheat_time_saved_count[time_saved] + 1


# Count how many cheats past the threshold there are in total.
cheat_count = 0
for cheat in cheat_time_saved_count:
    cheat_count += cheat_time_saved_count[cheat]

print(f'Number of cheats that save us {CHEAT_THRESHOLD} or more picoseconds: {cheat_count}')
