
with open('in', 'r') as f:
    input = f.read()

rules_index = set()
rules = []
for line in input.split('\n\n')[0].split('\n'):
    before, after = list(map(int, line.rstrip().split('|')))
    rules.append((before, after))
    rules_index.add((before, after))

updates_index = [] 
updates = []

for line in input.split('\n\n')[1].split('\n'):
    nums = line.rstrip().split(',')
    nums = list(map(int, nums))
    indices = {}
    for i, num in enumerate(nums):
        indices[num] = i         
    updates_index.append(indices)
    updates.append(nums)
        
import functools

result = 0
for i, update in enumerate(updates_index):
    bad_update = False
    for (fst, snd) in rules:
        if fst in update.keys() and snd in update.keys():
            fst, snd = update[fst], update[snd]
            if fst > snd:
                bad_update = True
            
    if bad_update:
        def cmp(x, y):
            if (x, y) in rules_index:
                return 1
            if (y, x) in rules_index:
                return -1
            return 1
            
        newupdates = sorted(updates[i], key=functools.cmp_to_key(cmp))
        mid = newupdates[len(update)//2]
        result += mid

print(result)
