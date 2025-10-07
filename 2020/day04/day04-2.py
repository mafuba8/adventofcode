#!/usr/bin/python3
# Advent of Code 2020 - Day 4, Part 2
# Benedikt Otto
#
import re

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


# Regexes for field validations.
re_4digits = re.compile(r'^\d{4}$')
re_hgt = re.compile(r'^((\d{3})cm|(\d{2})in)$')
re_hcl = re.compile(r'^#[a-f0-9]{6}$')
re_pid = re.compile(r'^\d{9}$')

def validate_field(field, value):
    match field:
        case 'byr':
            if re_4digits.search(value) and 1920 <= int(value) <= 2002:
                return True
        case 'iyr':
            if re_4digits.search(value) and 2010 <= int(value) <= 2020:
                return True
        case 'eyr':
            if re_4digits.search(value) and 2020 <= int(value) <= 2030:
                return True
        case 'hgt':
            s = re_hgt.search(value)
            if s:
                hgt_cm = s.group(2)
                hgt_in = s.group(3)
                if hgt_cm and 150 <= int(hgt_cm) <= 193:
                    return True
                if hgt_in and 59 <= int(hgt_in) <= 76:
                    return True
        case 'hcl':
            if re_hcl.search(value):
                return True
        case 'ecl':
            if value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                return True
        case 'pid':
            if re_pid.search(value):
                return True
        case 'cid':
            return True
    return False


# Count valid passports.
valid_passports_count = 0
for passport in passport_list:
    print(passport)
    valid = True
    invalid_fields = []
    for field in passport:
        if not validate_field(field, passport[field]):
            invalid_fields.append(field)

    if len(invalid_fields) == 0:
        print(f'  Passport is valid.')
        valid_passports_count += 1
    else:
        print(f'  Passport is not valid, wrong fields: {invalid_fields}')

print()
print(f'Total number of "valid" passports: {valid_passports_count}.')
