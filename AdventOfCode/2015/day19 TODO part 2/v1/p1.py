import re

def replacenth(string, sub, wanted, n):
    where = [m.start() for m in re.finditer(sub, string)][n-1]
    before = string[:where]
    after = string[where:]
    after = after.replace(sub, wanted, 1)
    newString = before + after
    return newString
    
    
lines = open('in').readlines()

startMolecule = lines[-1]
lines = lines[:-2]

replacements = {}

for rep in lines:
    fst, _, snd = rep.strip('\n').split()
    occur = startMolecule.count(fst)
    if replacements.get(fst) == None:
        replacements[fst] = {'occur':occur, 'replacement':[]}
    if snd not in replacements[fst]['replacement']:
        replacements[fst]['replacement'].append(snd)

molecules = set()
for e in replacements:
    for occur in range(1, replacements[e]['occur'] + 1):
        for repl in range(0, len(replacements[e]['replacement'])):
            molecules.add(replacenth(startMolecule, e, replacements[e]['replacement'][repl], occur))
print(len(molecules))
