
with open('in') as f:
    opcodes = list(map(int, f.read().strip().split(',')))
    print(opcodes)
    opcodes[1] = 12
    opcodes[2] = 2
    for i in range(0, len(opcodes), 4):
        instr = opcodes[i]
        if instr == 99:
            break
        elif instr == 1:
            ad1, ad2, res = opcodes[i + 1], opcodes[i + 2], opcodes[i + 3]
            opcodes[res] = opcodes[ad1] + opcodes[ad2]
            pass
        elif instr == 2:
            ad1, ad2, res = opcodes[i + 1], opcodes[i + 2], opcodes[i + 3]
            opcodes[res] = opcodes[ad1] * opcodes[ad2]

print(opcodes[0])
        
        