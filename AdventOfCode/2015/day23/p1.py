
skip = 0
vars = {'a': 0, 'b': 0}
# vars = {'a': 1, 'b': 0} # for part 2

instructions = []

for line in open('in').readlines():
    tok = line.strip('\n').replace(',', ' ').split()
    instructions.append(tok)

instr_ptr = 0

# for idx, instr in enumerate(instructions):
#     print(idx, instr)
# print()
    
while instr_ptr < len(instructions):
    # input()
    tok = instructions[instr_ptr]
    instr = tok[0]

    # print(instr_ptr, tok, ' ->\t', end='')

    instr_ptr += 1
    
    r = tok[1]
    
    if instr == 'inc': vars[r] += 1
    elif instr == 'hlf': vars[r] //= 2
    elif instr == 'tpl': vars[r] *= 3
    elif instr == 'jmp': instr_ptr += int(tok[1]) - 1
    elif instr == 'jie' and vars[r] % 2 == 0: instr_ptr += int(tok[2]) - 1
    elif instr == 'jio' and vars[r] == 1: instr_ptr += int(tok[2]) - 1
    # print(vars)

print(vars)
