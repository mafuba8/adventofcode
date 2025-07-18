#!/usr/bin/python3
# Advent of Code 2021 - Day 19, Part 1
# Benedikt Otto
#

# input_file = '../examples/example_19.txt'
input_file = '../inputs/input_19.txt'

# Parse input into list of lists.
scanner_reports = []
with open(input_file) as file:
    scanner_num = -1
    for line in file.readlines():
        if '---' in line:
            scanner_num += 1
            scanner_reports.append([])

        if ',' in line:
            p = [int(x) for x in line.strip().split(',')]
            scanner_reports[scanner_num].append(tuple(p))


# Mapping of the transformation rules to their vectors.
VEC = {'x': (1, 0, 0), '-x': (-1, 0, 0), 'y': (0, 1, 0), '-y': (0, -1, 0), 'z': (0, 0, 1), '-z': (0, 0, -1)}
VEC_REV = {(1, 0, 0): 'x', (-1, 0, 0): '-x', (0, 1, 0): 'y', (0, -1, 0): '-y', (0, 0, 1): 'z', (0, 0, -1): '-z'}

class Orientation:
    def __init__(self, xmap, ymap):
        """An orientation is defined by setting where the vectors x=(1,0,0) and y=(0,1,0) are mapped to.
        The mapping of z=(0,0,1) is automatically chosen so, that the orientation is positive."""
        self.xmap = xmap
        self.ymap = ymap
        self.zmap = VEC_REV[self._cross(VEC[xmap], VEC[ymap])]

        # True = '+', False = '-'
        map_sign = {'x': True, '-x': False, 'y': True, '-y': False, 'z': True, '-z': False}
        map_idx = {'x': 0, '-x': 0, 'y': 1, '-y': 1, 'z': 2, '-z': 2}
        self._mapper_sign = map_sign[xmap], map_sign[ymap], map_sign[self.zmap]
        self._mapper_idx = map_idx[xmap], map_idx[ymap], map_idx[self.zmap]

    def __repr__(self):
        return f'({self.xmap}, {self.ymap}, {self.zmap})'

    def __mul__(self, other):
        """Multiplication = composition of orientations so that
           transform_A*B(v) = transform_A(transform_B(v))."""
        new_xmap = VEC_REV[self.transform_reverse(other.transform_reverse(VEC['x']))]
        new_ymap = VEC_REV[self.transform_reverse(other.transform_reverse(VEC['y']))]
        return Orientation(xmap=new_xmap, ymap=new_ymap)

    @staticmethod
    def _cross(a, b):
        """Simple cross product of vectors to get triples with positive orientation."""
        c = (a[1] * b[2] - a[2] * b[1],
             a[2] * b[0] - a[0] * b[2],
             a[0] * b[1] - a[1] * b[0])
        return c

    def transform(self, vector):
        """Transforms the given coordinate by applying the orientation, e.g. for ('-y', 'z', '-x'):
            (1, 2, 3) -> (-2, 3, -1).
        """
        l = [0, 0, 0]
        for idx in range(3):
            new_idx = self._mapper_idx[idx]
            if self._mapper_sign[idx]:
                l[idx] = vector[new_idx]
            else:
                l[idx] = -vector[new_idx]
        return tuple(l)

    def transform_reverse(self, vector):
        """Inverse transformation of self.transform, e.g. for ('-y', 'z', '-x'):
            (-2, 3, -1) -> (1, 2, 3).
        """
        l = [0, 0, 0]
        for idx in range(3):
            new_idx = self._mapper_idx[idx]
            if self._mapper_sign[idx]:
                l[new_idx] = vector[idx]
            else:
                l[new_idx] = -vector[idx]
        return tuple(l)


def find_scanner_position(base_scanner, new_scanner, or_relative):
    """Tries to determine the (relative) position of new_scanner in the coordinate system of base_scanner, assuming
    that the two scanners have the relative orientation or_new. If there are not enough beacons in the overlapping
    search to ensure that they are the same scanner, it returns None instead."""
    for base_beacon in base_scanner:
        for new_beacon in new_scanner:
            # Assuming that the beacon at new_beacon is the same beacon as base_beacon
            # but in the base_scanner coordinate system.
            new_beacon_in_base_coord = or_relative.transform_reverse(new_beacon)
            # Potential coordinate for the position of new_scanner in the base_scanner coord system.
            new_scanner_pos_candidate = (base_beacon[0] - new_beacon_in_base_coord[0],
                                         base_beacon[1] - new_beacon_in_base_coord[1],
                                         base_beacon[2] - new_beacon_in_base_coord[2])

            # Check if the remaining beacons also map right.
            count = 0
            for b in base_scanner:
                d = (b[0] - new_scanner_pos_candidate[0],
                     b[1] - new_scanner_pos_candidate[1],
                     b[2] - new_scanner_pos_candidate[2])
                b_rel_1 = or_relative.transform(d)
                if b_rel_1 in new_scanner:
                    count += 1
            if count >= 12:
                return new_scanner_pos_candidate
    return None


def find_scanner_data(base_scanner, new_scanner):
    """Finds the position of new_scanner and its orientation relative to the pos and orientation of base_scanner."""
    for or_new in all_orientations:
        pos_new = find_scanner_position(base_scanner, new_scanner, or_new)
        if pos_new is not None:
            return pos_new, or_new
    return None


def find_abs_position(rel_pos, base_abs_pos, base_abs_or):
    """Takes a position relative to a given scanner (base_abs_pos, base_abs_or) and
    returns the absolute coordinate of this position."""
    x = base_abs_or.transform_reverse(rel_pos)
    return base_abs_pos[0] + x[0], base_abs_pos[1] + x[1], base_abs_pos[2] + x[2]


# Make list of all (positive) orientations.
all_orientations = []
for xy in [('x', 'y'), ('x', '-y'), ('x', 'z'), ('x', '-z'),
           ('-x', 'y'), ('-x', '-y'), ('-x', 'z'), ('-x', '-z'),
           ('y', 'x'), ('y', '-x'), ('y', 'z'), ('y', '-z'),
           ('-y', 'x'), ('-y', '-x'),('-y', 'z'),('-y', '-z'),
           ('z', 'x'), ('z', '-x'), ('z', 'y'), ('z', '-y'),
           ('-z', 'x'), ('-z', '-x'), ('-z', 'y'), ('-z', '-y')]:
    orientation = Orientation(xy[0], xy[1])
    all_orientations.append(orientation)


# We now build up a list of scanner data. Here the scanner data consists of
#  - the absolute position
#  - the absolute orientation
# of the scanner.
scanner_data = {0: ((0, 0, 0), Orientation('x', 'y'))}

# For each known scanner, check all unknown scanners if there is some scanner data
# that matches the beacon pattern they both see.
scanner_done = []
while len(scanner_data) < len(scanner_reports):
    new_scanner_data = []
    for base_id in [i for i in scanner_data if i not in scanner_done]:
        scanner_done.append(base_id)

        print(f'Finding matching scanners relative to scanner {base_id}...')
        scanner_base = scanner_reports[base_id]
        base_abs_pos, base_abs_or = scanner_data[base_id]

        # Check all the scanners of which we don't have data yet.
        for scanner_id in [k for k in range(len(scanner_reports)) if k not in scanner_data]:
            scanner_new = scanner_reports[scanner_id]
            x = find_scanner_data(scanner_base, scanner_new)
            if x is not None:
                # Here we have found a coordinate and orientation pair where scanner_new
                # sees the same beacons as scanner_base. Both are relative to scanner_base though.
                rel_pos, rel_or = x

                # Determine the absolute position and orientation of this scanner (relative to scanner 0).
                abs_pos = find_abs_position(rel_pos, base_abs_pos, base_abs_or)
                abs_or = base_abs_or * rel_or

                print(f'  Matching scanner {scanner_id}:')
                print(f'    relative: {rel_pos} / {rel_or}')
                print(f'    absolute: {abs_pos} / {abs_or}')
                new_scanner_data.append((scanner_id, abs_pos, abs_or))

    # Add the found data to the list of known scanners.
    for s_id, s_pos, s_or in new_scanner_data:
        scanner_data.setdefault(s_id, (s_pos, s_or))

print()
# List all the scanners.
print('All scanners have been identified. They have the following data:')
for scanner_id in scanner_data:
    s_pos, s_or = scanner_data[scanner_id]
    print(f'  Scanner {scanner_id} @ {s_pos} (Orientation: {s_or})')

# Build set of all beacons by transforming their relative coordinates into their absolute ones.
beacons = set()
for scanner_id in scanner_data:
    s_pos, s_or = scanner_data[scanner_id]
    for rel_beacon in scanner_reports[scanner_id]:
        abs_beacon = find_abs_position(rel_beacon, s_pos, s_or)
        beacons.add(abs_beacon)

print(f'There are {len(beacons)} beacons on the map.')
