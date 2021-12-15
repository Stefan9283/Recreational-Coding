
#### SOL 1

# ranges = []
# for line in open('in').readlines():
#     x, y = [int(num) for num in line.strip('\n').split('-')]
#     ranges.append((x, y))
    

# ranges.sort(key=lambda x: x[0])

# i = 0
# total = 0
# while i <= 4294967295:
#     isBlacklisted = False
#     for r in ranges:    
#         if i in range(r[0], r[1] + 1):
#             isBlacklisted = True
#             i = r[1]
#     if not isBlacklisted:
#         print(i)
#         total += 1
#     i += 1
# print(total)


#### SOL 2

ranges = []
for line in open('in').readlines():
    x, y = [int(num) for num in line.strip('\n').split('-')]
    ranges.append((x, y))
    
ranges.sort(key=lambda x: x[0])

while True:
    squeezed = False
    for i in range(len(ranges) - 1):
        a,b = ranges[i]
        x,y = ranges[i+1]
        if b in range(x, y + 1) or b >= y:
            ranges.pop(i + 1)
            ranges.pop(i)
            ranges.append((min([a,b,x,y]), max([a,b,x,y])))
            squeezed = True
            break      
    ranges.sort(key=lambda x: x[0])
    if not squeezed:
        break  

allowedIPs = 4294967295 + 1
blackListed = 0

for r in ranges:
    blackListed += r[1] + 1 - r[0]

print(allowedIPs - blackListed)
