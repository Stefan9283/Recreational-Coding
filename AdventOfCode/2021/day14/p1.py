
lines = [line.strip('\n') for line in open('in1').readlines()]

template = lines[0]
inst = {}

def extend(s: str):
    new = []
    for i in range(len(s) - 1):
        group = s[i:i+2]
        new.append(s[i])
        if inst.get(group) != None:
            new.append(inst[group])
    new.append(s[-1])
    return ''.join(new)

def getOccurs(template):
    occur = {}
    for c in template:
        if occur.get(c) == None:
            occur[c] = 0
        occur[c] += 1
    return occur

lines = lines[2:]
for line in lines:
    fst, _, snd = line.split()
    inst[fst] = snd
    

steps = 40

for i in range(steps):
    template = extend(template)
    occur = getOccurs(template) 
    # print(i + 1, occur, template)
    print(i+1, len(template)) #, template)





occur = [(c, occur[c]) for c in occur]
occur.sort(key=lambda x: x[1])
print(occur[-1][1] - occur[0][1])
