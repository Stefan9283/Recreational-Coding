import collections

def isPasswordV2(val: int) -> bool:
    if len(str(val)) != 6: 
        return False

    digits = list(map(int, str(val)))
    if sorted(digits) != digits:
        return False

    occur = collections.defaultdict(list[int])
    for idx, d in enumerate(digits):
        occur[d].append(idx)
    
    for occ in occur:
        if len(occur[occ]) == 2:
            return True
    return False

vals = list(map(int, open('in').readline().split('-')))

count = 0
for password in range(vals[0], vals[1] + 1):
    if isPasswordV2(password):
        count += 1
print(count)