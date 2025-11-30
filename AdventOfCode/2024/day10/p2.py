
with open('in') as f:
    m = list(map(lambda x: list(map(lambda x: int(x) if x.isnumeric() else '.', list(x.rstrip()))), f.readlines()))

def find_trails(start):
    found = 0
    stack = [start]
    
    while stack:
        (i, j) = stack.pop()
        curr = m[i][j]
        
        if curr == '.':
            continue
        
        if curr == 9:
            found += 1
            continue
        
        if i > 0 and type(m[i-1][j]) == int and m[i-1][j] - curr == 1:
            stack.append((i-1, j))
        if i < len(m) - 1 and type(m[i+1][j]) == int and m[i+1][j] - curr == 1:
            stack.append((i+1, j))
        if j > 0 and type(m[i][j-1]) == int and m[i][j-1] - curr == 1:
            stack.append((i, j-1))
        if j < len(m[0]) - 1 and type(m[i][j+1]) == int and m[i][j+1] - curr == 1:
            stack.append((i, j+1))
        
    return found

sum = 0
for i in range(len(m)):
    for j in range(len(m[0])):
        if m[i][j] == 0:
            sum += find_trails((i, j))    
print(sum)