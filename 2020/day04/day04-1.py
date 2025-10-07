#!/usr/bin/python3
# Advent of Code 2020 - Day 4, Part 1
# Benedikt Otto
#

# input_file = '../examples/example_4.txt'
input_file = '../inputs/input_4.txt'

# Parse input into list of dicts.
passport_list = []
with open(input_file) as file:
    passport = {field: '' for field in ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid')}
    for line in file.readlines():
        if line == '\n':
            # Save current passport to list and make new empty one.
            passport_list.append(passport)
            passport = {field: '' for field in ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid')}
        else:
            # Add the given fields to the passport.
            for key_value in line.strip().split(' '):
                field, value = key_value.split(':')
                passport[field] = value

    # Save last passport.
    passport_list.append(passport)


# Count valid passports.
valid_passports_count = 0
for passport in passport_list:
    print(passport)
    valid = True
    missing_fields = []
    for field in passport:
        if passport[field] == '':
            missing_fields.append(field)

    if len(missing_fields) == 0:
        print(f'Passport is valid.')
        valid_passports_count += 1
    elif missing_fields == ['cid']:
        print(f'Passport is "valid" (ignoring the country field).')
        valid_passports_count += 1
    else:
        print(f'Passport is not valid, missing: {missing_fields}')

print()
print(f'Total number of "valid" passports: {valid_passports_count}.')
