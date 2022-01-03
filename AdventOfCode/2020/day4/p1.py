import re


def checkPass(p, checkValue: bool = True):
    # check if all the needed fields exist
    foundFields = sorted(list(p))
    if 'cid' in foundFields: foundFields.remove('cid')
    neededFields = sorted(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
    if foundFields != neededFields: return False
    
    if not checkValue: return True

    # check the value of each field
    if int(p['byr']) not in range(1920, 2002 + 1): return False
    if int(p['iyr']) not in range(2010, 2020 + 1): return False
    if int(p['eyr']) not in range(2020, 2030 + 1): return False
    hgt_unit = p['hgt'][-2:]
    if hgt_unit not in ['cm', 'in']: return False
    if hgt_unit == 'cm' and int(p['hgt'][:-2]) not in range(150, 193 + 1): return False
    elif hgt_unit == 'in' and int(p['hgt'][:-2]) not in range( 59,  76 + 1): return False
    if not re.match(r'#[0-9,a-f]*', p['hcl']) or len(p['hcl']) != 7: return False
    if p['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']: return False
    if not re.match(r'[0-9]*', p['pid']) or len(p['pid']) != 9: return False
    return True

passports = []
passport = dict()

for line in open('in').readlines():
    line = line.strip('\n')
    if len(line) == 0 and len(passport):
        passports.append(dict(passport))
        passport = dict()
    else:
        for prop in line.split():
            # print('prop',prop)
            name, val = prop.split(':')
            passport[name] = val
            ##	print(name, val, passport)

invalid = 0
for idx, passport in enumerate(passports):
    if not checkPass(passport, False):
        invalid += 1
    # else:
    #     print('$' * 10, idx, '$' * 10)
    #     print(passport)
    #     print('\n')

print('part1', len(passports) - invalid)


invalid = 0
for idx, passport in enumerate(passports):
    if not checkPass(passport):
        invalid += 1

print('part2', len(passports) - invalid)
