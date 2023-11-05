
ADD = 1
MUL = 2
SAVE = 3
OUTPUT = 4
JUMP_IF_TRUE = 5
JUMP_IF_FALSE = 6
LESS_THAN = 7
EQUALS = 8
EXIT = 99

def execute_file(file):
    code = list(map(lambda x: int(x), open(file).read().split(',')))
    
    idx = 0
    while True:
        print()
        print(code[:idx], code[idx], code[idx + 1:])
        opcode = code[idx] % 100
        modes = code[idx] / 100
        if opcode == ADD:
            op1, op2, out = code[idx + 1: idx + 1 + 3]
            code[out] = code[op1] + code[op2]
            idx += 4
        elif opcode == MUL:
            args = code[idx + 1: idx + 1 + 3]
            op1, op2, out = code[idx + 1: idx + 1 + 3]
            code[out] = code[op1] * code[op2]
            idx += 4    
        elif opcode == EXIT:
            print()
            print(code[:idx], code[idx], code[idx + 1:])
            return code[0]
        elif opcode == SAVE: pass
        elif opcode == OUTPUT: pass
        elif opcode == JUMP_IF_TRUE: pass
        elif opcode == JUMP_IF_FALSE: pass
        elif opcode == LESS_THAN: pass
        elif opcode == EQUALS: pass
        else:
            raise Exception('Unknown opcode')
        
    
ret = execute_file('in0')
print(ret)

