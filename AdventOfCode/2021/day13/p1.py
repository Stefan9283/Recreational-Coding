

xys = []
size = [0, 0]
instr = []

for line in open('in').readlines():
    line = line.strip('\n')
    if len(line) == 0: continue
    if line.startswith('fold along'):
        tok = line.split()
        tok = tok[-1].split('=')
        instr.append((tok[0], int(tok[1])))        
    else:
        tok = line.split(',')
        xys.append((int(tok[0]), int(tok[1])))
        size[0] = max(size[0], xys[-1][0])
        size[1] = max(size[1], xys[-1][1])

print(size)
mat = [['.' for _ in range(size[0] + 1)] for _ in range(size[1] + 1)]

# for row in mat:
#     print(row)

for x, y in xys:
    mat[y][x] = '#'
# for row in mat:
#     print(row)
# print()

for coord, pos in instr:
    if coord == 'x':
        for i in range(pos):
            mirror = len(mat[0]) - 1 - i
            for j in range(len(mat)):
                if mat[j][i] == '#': pass
                else: mat[j][i] = mat[j][mirror]
        for i in range(len(mat)):
            mat[i] = mat[i][:pos]
    else:
        for i in range(pos):
            mirror = len(mat) - 1 - i
            for j in range(len(mat[0])):
                if mat[i][j] == '#': pass
                else: mat[i][j] = mat[mirror][j]
        mat = mat[:pos]
    

dots = 0
for row in mat:
    dots += row.count('#')
print(dots)

for row in mat:
    print(row)
print()