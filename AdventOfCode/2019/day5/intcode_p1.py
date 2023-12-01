


import sys


ADD = 1
MUL = 2
SAVE = 3
OUTPUT = 4
JUMP_IF_TRUE = 5
JUMP_IF_FALSE = 6
LESS_THAN = 7
EQUALS = 8
EXIT = 99

def execute_file(file, input_):
    code = list(map(lambda x: int(x), open(file).read().split(',')))
        
    idx = 0
    while True:
        opcode = code[idx] % 100
        modes = str(int(code[idx] / 100))
        while modes.__len__() != 3:
            modes = '0' + modes
        modes = [int(i) for i in reversed(modes)]

        print()

        print(idx, ')', opcode, modes, code[idx: idx + 4])
        
        def get_value(id, mode):
            if mode == 1:
                return id
            return code[id]

        def args_to_values(args):
            values = []
            for arg, mode in zip(args, modes):
                values.append(get_value(arg, mode))
            return values
        
        if opcode == ADD:
            op1, op2 = args_to_values(code[idx + 1: idx + 1 + 2])
            out = code[idx + 3]
            print(op1, op2, out)
            code[out] = op1 + op2
            idx += 4
        elif opcode == MUL:
            op1, op2 = args_to_values(code[idx + 1: idx + 1 + 2])
            out = code[idx + 3]
            print(op1, op2, out)
            code[out] = op1 * op2
            idx += 4
        elif opcode == EXIT:
            return code[0]
        elif opcode == SAVE: 
            out = code[idx + 1]
            code[out] = input_
            idx += 2
        elif opcode == OUTPUT: 
            addr = get_value(code[idx + 1], modes[0])
            # print(addr, code[addr])
            # if code[addr]:
            #     sys.exit(-1)
            print('out', code[addr])
            idx += 2
        # elif opcode == JUMP_IF_TRUE: pass
        # elif opcode == JUMP_IF_FALSE: pass
        # elif opcode == LESS_THAN: pass
        # elif opcode == EQUALS: pass
        else:
            raise Exception('Unknown opcode')
        
    
ret = execute_file('in', 1)
print(ret)

