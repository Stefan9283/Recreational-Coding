

vars = {'a':0, 'b':0, 'c':0, 'd':0}
# vars = {'a':0, 'b':0, 'c':1, 'd':0} # for part 2


instr = []

for line in open('in').readlines():
    instr.append(line.strip('\n').split())
# print(instr)

instr_ptr = 0

while instr_ptr < len(instr):
    # print(instr[instr_ptr])
    if instr[instr_ptr][0] in ['cpy', 'jnz']:
        cmd, x, y = instr[instr_ptr]
        if cmd == 'cpy': 
            if x.isnumeric():  
                vars[y] = int(x)
            else:
                vars[y] = vars[x]
        else: 
            if x.isnumeric():
                if int(x) != 0:
                    instr_ptr += int(y)
                    continue
            elif vars[x] != 0: 
                instr_ptr += int(y)
                continue
    else:
        cmd, x = instr[instr_ptr]
        if cmd == 'inc': vars[x] += 1
        else: vars[x] -= 1
    instr_ptr += 1
    # print('\t', instr_ptr, vars)
''
print(vars)