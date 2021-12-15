
ranges = []
for line in open('in').readlines():
    x, y = [int(num) for num in line.strip('\n').split('-')]
    ranges.append((x, y))
    

ranges.sort(key=lambda x: x[0])
print(ranges)

i = 0
while i <= 4294967295:
    isBlacklisted = False
    for r in ranges:    
        if i in range(r[0], r[1] + 1):
            isBlacklisted = True
            i = r[1]
            
    if not isBlacklisted:
        print(i)
        break
    i += 1
