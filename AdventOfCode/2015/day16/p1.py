import re

TheSue = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1
}

Sues = []


for line in open('in').readlines():
    tok = re.split(': |, | ', line.strip('\n'))
    index = int(tok[1])
    Sue = {'index':index}
    
    valid = True
    for i in range(2, len(tok), 2):
        Sue[tok[i]] = int(tok[i + 1])
        if Sue[tok[i]] != TheSue[tok[i]]:
            valid = False
            break
    if valid:
        Sues.append(Sue)
print(Sues)