
from collections import defaultdict

lines = [line.strip('\n') for line in open('in1').readlines()]

template = lines[0]
inst = {}

occurs = defaultdict(int)

lines = lines[2:]
for line in lines:
    fst, _, snd = line.split()
    inst[fst] = [fst[0] + snd, snd + fst[1]]
    occurs[fst] = template.count(fst)
    

steps = 40

# Template:     NNCB
# After step 1: NCNBCHB
# After step 2: NBCCNBBBCBHCB
# After step 3: NBBBCNCCNBBNBNBBCHBHHBCHB
# After step 4: NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB

for i in range(steps):
    oldoccurs = occurs
    occurs = defaultdict(int)
    for src in inst:
        l, r = inst[src]
        if oldoccurs[src] == 0: continue
        occurs[l] += oldoccurs[src]
        occurs[r] += oldoccurs[src]

letter_occurs = defaultdict(int)
for oc in occurs:
    l, r = oc
    letter_occurs[l] += occurs[oc]
letter_occurs[template[-1]] += 1

print([(c, letter_occurs[c]) for c in letter_occurs])

minOcc = letter_occurs[min(letter_occurs, key=lambda x: letter_occurs[x])]
maxOcc = letter_occurs[max(letter_occurs, key=lambda x: letter_occurs[x])]
print(maxOcc - minOcc)