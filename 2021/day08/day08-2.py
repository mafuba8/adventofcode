#!/usr/bin/python3
# Advent of Code 2021 - Day 8, Part 2
# Benedikt Otto
#

# input_file = '../examples/example_8.txt'
input_file = '../inputs/input_8.txt'

# Parse input into list of entries.
entries = []
with open(input_file) as file:
    for line in file.readlines():
        sig, out = line.strip().split(' | ')

        # Sort each signal alphabetically.
        sig_list = []
        for s in sig.split(' '):
            sig_list.append(''.join(sorted(s)))
        out_list = []
        for o in out.split(' '):
            out_list.append(''.join(sorted(o)))

        entries.append((sig_list, out_list))


def map_digits(signals):
    digit_mapping = {sig: None for sig in signals}

    # There is only one digit with 2, 3, 4 or 7 segments ('1', '7', '4' or '8').
    for sig in signals:
        match len(sig):
            case 2:
                digit_mapping[sig] = '1'  # 2 segments => '1'
                segments_one = sig        # remember the signals of '1' for later.
            case 3:
                digit_mapping[sig] = '7'  # 3 segments => '7'
            case 4:
                digit_mapping[sig] = '4'  # 4 segments => '4'
                segemtns_four = sig       # remember the signals for '4' for later.
            case 7:
                digit_mapping[sig] = '8'  # 7 segments => '8'

    # Digits displayed with 6 segments can be '0', '6' or '9'.
    for sig in [s for s in signals if len(s) == 6]:
        a = set(sig)
        s_one = set(segments_one)
        s_four = set(segemtns_four)
        if len(a.intersection(s_one)) == 1:
            # One matching segment with digit '1' => '6'
            digit_mapping[sig] = '6'
            segments_six = sig  # remember the signals of '6' for later.
        else:
            match len(a.intersection(s_four)):
                case 3:
                    # Three matching segment with digit '4' => '0'
                    digit_mapping[sig] = '0'
                case 4:
                    # Three matching segment with digit '4' => '9'
                    digit_mapping[sig] = '9'

    # Digits displayed with 5 segments can be '2', '3' or '5'.
    for sig in [s for s in signals if len(s) == 5]:
        a = set(sig)
        s_one = set(segments_one)
        s_six = set(segments_six)

        if len(a.intersection(s_one)) == 2:
            # Two matching segments with digit '1' => '3'
            digit_mapping[sig] = '3'
        else:
            match len(a.intersection(s_six)):
                case 4:
                    # Four matching segments with digit '6' => '2'
                    digit_mapping[sig] = '2'
                case 5:
                    # Five matching segments with digit '6' => '5'
                    digit_mapping[sig] = '5'

    return digit_mapping


# Run through all the entries and figure out what number it did represent.
sum_of_outputs = 0
for num, entry in enumerate(entries):
    signals, output = entry
    digit_mapping = map_digits(signals)

    # Build the displayed number out of the mapped digits.
    displayed_number = ''
    for o in output:
        displayed_number += digit_mapping[o]

    print(f'Entry #{num+1}: {displayed_number}')
    sum_of_outputs += int(displayed_number)

print(f'Sum of all output values: {sum_of_outputs}')
