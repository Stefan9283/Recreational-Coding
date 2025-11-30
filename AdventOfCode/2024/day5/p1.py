
with open('in', 'r') as f:
    input = f.read()

rules = []
for line in input.split('\n\n')[0].split('\n'):
    before, after = line.rstrip().split('|')
    rules.append((int(before), int(after)))

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
        
result = 0
for i, update in enumerate(updates_index):
    bad_update = False
    for (fst, snd) in rules:
        if fst in update.keys() and snd in update.keys():
            fst, snd = update[fst], update[snd]
            if fst > snd:
                bad_update = True
            
    if not bad_update:
        mid = updates[i][len(update)//2]
        result += mid

print(result)
