

with open('in', 'r') as f:
    A = int(f.readline().rstrip().split(' ')[-1])
    B = int(f.readline().rstrip().split(' ')[-1])
    C = int(f.readline().rstrip().split(' ')[-1])
    f.readline()
    program = list(map(int, f.readline().rstrip().split(' ')[1].split(',')))


def get_value(v):
    if v < 0 or v >= 7:
        raise Exception("Illegal value")
    if v <= 3:
        return v
    return [A, B, C][v-4] 

import math, traceback

try:


    pc = 0
    output = []
    while pc < len(program):
        op = program[pc]
        print(pc, '/', len(program), [A, B, C], op, program, output)
        if op == 0: # adv
            power = get_value(program[pc+1])
            A = math.floor(A / pow(2, power)) 
            pc += 2
        if op == 1: # bxl
            literal = program[pc+1]
            B = B ^ literal
            pc += 2
        if op == 2: # bst
            literal = get_value(program[pc+1])
            B = literal % 8
            pc += 2
        if op == 3: # jnz
            if A == 0:
                pc += 2
            else:
                pc = program[pc+1]
        if op == 4: # bxc
            # literal = get_value(program[pc+1]) # ignore
            B = B ^ C
            pc += 2
        if op == 5: # out
            literal = get_value(program[pc+1]) 
            output.append(literal % 8)
            pc += 2        
        if op == 6: # bdv
            power = get_value(program[pc+1])
            B = math.floor(A / pow(2, power)) 
            pc += 2
        if op == 7: # cdv
            power = get_value(program[pc+1])
            C = math.floor(A / pow(2, power)) 
            pc += 2
            
    print(','.join(map(str, output)))

except Exception as e:
    traceback.print_exception(e)
    print(pc, op, [A, B, C], program, output)

