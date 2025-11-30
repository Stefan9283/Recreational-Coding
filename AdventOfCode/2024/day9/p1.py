
with open('in') as f:
    s = f.read()

sum = 0
odd = False
disk = []
id = 0
for c in s:
    sum += int(c)
    if odd:
        disk += ['.' for _ in range(int(c))]
        odd = False
    else:
        disk += [id for _ in range(int(c))]
        id += 1
        odd = True

# print(disk)

l, r = 0, len(disk) - 1
while l < r:
    while disk[l] != '.':
        l += 1
        
    while disk[r] == '.':
        r -= 1
    
    if l >= r: break
    
    disk[l], disk[r] = disk[r], disk[l]
    
    # print(disk)

checksum = 0
for i, val in enumerate(disk):
    if val == '.':
        break
    checksum += i * val

print(checksum)