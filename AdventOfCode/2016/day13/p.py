
input = 1364

def getCell(y, x):
    r = x*x + 3*x + 2*x*y + y + y*y + input
    return format(r, 'b').count('1') % 2 == 1
print(getCell(0, 0))

for i in range(10):
    for j in range(10):
        if getCell(i, j):
            print('#', end='')
        else:
            print('.', end='')
    print()

            
min_steps = {}

stack = [((1, 1), 0)]

while stack:
    pos, depth = stack[0]
    stack = stack[1:]
    if min_steps.get(pos) != None:
        depth = min(min_steps[pos], depth)
        min_steps[pos] = depth
    else:   
        min_steps[pos] = depth
        for add in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            neigh = (pos[0] + add[0], pos[1] + add[1])
            if getCell(neigh[0], neigh[1]) == False and neigh[0] >= 0 and neigh[1] >= 0:
                stack.append((neigh, depth + 1))
    
print(min_steps[(39, 31)])
    
    

print(list(filter(lambda x : x <= 50, min_steps.values())).__len__())




            