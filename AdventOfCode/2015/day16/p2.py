import re

TheSue = {
    'children': 3,
    'samoyeds': 2,
    'akitas': 0,
    'cars': 2,
    'vizslas': 0,
    'perfumes': 1,
    # fewer than
    'goldfish': 5,
    'pomeranians': 3,
    # greater than
    'trees': 3,
    'cats': 7,
}

Sues = []

for line in open('in').readlines():
    tok = re.split(': |, | ', line.strip('\n'))
    index = int(tok[1])
    Sue = {'index':index}
    valid = True
    for i in range(2, len(tok), 2):
        Sue[tok[i]] = int(tok[i + 1])
        if tok[i] in ['trees', 'cats']:
            if not Sue[tok[i]] > TheSue[tok[i]]: 
                valid = False
                break
        elif tok[i] in ['goldfish', 'pomeranians']: 
            if not Sue[tok[i]] < TheSue[tok[i]]: 
                valid = False
                break
        elif Sue[tok[i]] != TheSue[tok[i]]:
            valid = False
            break
    if valid:
        Sues.append(Sue)
print(Sues)