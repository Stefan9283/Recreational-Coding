
with open('in') as f:
    s = f.read()

sum = 0
odd = False
disk = []
id = 0
for c in s:
    sum += int(c)
    if odd:
        disk.append([int(c), None])
        odd = False
    else:
        disk.append([int(c), id])
        id += 1
        odd = True

# print(disk)

l = 0
r = len(disk) - 1

def print_disk(d):
    s = ''
    for e in d:
        l, id = e
        for i in range(l):
            s += '.' if id == None else str(id)
    print(s)
    
# print_disk(disk)

already_moved = set()

while r > 0:
    while disk[r][1] == None:
        r -= 1 
    
    if r <= 0: break

    file_size, file_id = disk[r]

    if file_id in already_moved: 
        r -= 1
        continue
    
    for l in range(r): 
        
        free_space, shouldbenone = disk[l]
    
        # print('>', free_space, shouldbenone, file_size, file_id)

        if shouldbenone != None: continue
        # print(l, disk[l], r, disk[r])
        if free_space == file_size:
            # print('just enough')
            disk[l] = [file_size, file_id]
            disk[r] = [free_space, None]
            already_moved.add(file_id)
            break
        elif free_space > file_size:
            # print('more than enough')
            diff = free_space - file_size
            disk[l] = [file_size, file_id]
            disk[r] = [file_size, None]
            disk.insert(l + 1, [diff, None])
            already_moved.add(file_id)
            break
        else:   
            pass
            # print('not enough')
    r -= 1

    # input()
    
    # print_disk(disk)

checksum = 0
i = 0
for occur, id in disk:
    if id == None:
        i += occur
        continue
    
    for _ in range(occur):
        # print(i, id)
        checksum += i * id
        i += 1

print(checksum)