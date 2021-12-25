
def run(opcodes: list[int], noun, verb) -> int:
    opcodes_copy = list(opcodes)
    opcodes_copy[1] = noun
    opcodes_copy[2] = verb
    for i in range(0, len(opcodes_copy), 4):
        instr = opcodes_copy[i]
        if instr == 99:
            break
        elif instr == 1:
            ad1, ad2, res = opcodes_copy[i + 1], opcodes_copy[i + 2], opcodes_copy[i + 3]
            opcodes_copy[res] = opcodes_copy[ad1] + opcodes_copy[ad2]
            pass
        elif instr == 2:
            ad1, ad2, res = opcodes_copy[i + 1], opcodes_copy[i + 2], opcodes_copy[i + 3]
            opcodes_copy[res] = opcodes_copy[ad1] * opcodes_copy[ad2]
    return opcodes_copy[0]

import sys

with open('in') as f:
    opcodes = list(map(int, f.read().strip().split(',')))
    for noun in range(100):
        for verb in range(100):
            if run(opcodes, noun, verb) == 19690720:
                print(100 * noun + verb)
                sys.exit()    
        
        