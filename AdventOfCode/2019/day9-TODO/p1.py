ADD = 1
MUL = 2
SAVE = 3
OUTPUT = 4
JUMP_IF_TRUE = 5
JUMP_IF_FALSE = 6
LESS_THAN = 7
EQUALS = 8
REL_BASE = 9
EXIT = 99

def opcode_to_str(opcode):
    return {
        ADD: 'ADD',
        MUL: 'MUL',
        SAVE: 'SAVE',
        OUTPUT: 'OUTPUT',
        JUMP_IF_TRUE: 'JUMP_IF_TRUE',
        JUMP_IF_FALSE: 'JUMP_IF_FALSE',
        LESS_THAN: 'LESS_THAN',
        EQUALS: 'EQUALS',
        REL_BASE: 'REL_BASE',
        EXIT: 'EXIT'
    }[opcode]


def execute_file(file, input):

    print('new execution')

    code = list(map(lambda x: int(x), open(file).read().split(',')))

    offset = 0
    idx = 0

    while True:
        opcode = code[idx] % 100
        modes = str(int(code[idx] / 100))
        while modes.__len__() != 3:
            modes = '0' + modes
        modes = [int(i) for i in reversed(modes)]

        # print()
        print(opcode, opcode_to_str(opcode), modes, offset, code[idx + 1: idx + 4], code)
        
        def get_value(id, mode):
            if mode == 2:
                for _ in range(len(code), id + offset + 1):
                    code.append(-1)
                return code[id + offset]
            if mode == 1:
                return id
            
            for _ in range(code.__len__(), id + 1, 1):
                code.append(0)
            
            return code[id]

        def write_at(id, val):
            for _ in range(code.__len__(), id + 1, 1):
                code.append(0)
            code[id] = val

        def args_to_values(args):
            values = []
            for arg, mode in zip(args, modes):
                values.append(get_value(arg, mode))
            return values
        
        if opcode == ADD:
            op1, op2 = args_to_values(code[idx + 1: idx + 1 + 2])
            out = code[idx + 3]
            write_at(out, op1 + op2)
            idx += 4
        elif opcode == MUL:
            op1, op2 = args_to_values(code[idx + 1: idx + 1 + 2])
            out = code[idx + 3]
            write_at(out, op1 * op2)
            idx += 4
        elif opcode == EXIT:
            return code[0]
        elif opcode == SAVE: 
            out = code[idx + 1]
            write_at(out, input)
            idx += 2
        elif opcode == OUTPUT: 
            val = get_value(code[idx + 1], modes[0])
            # if val:
            #     return val
            print(f'{val},', end=' ')
            
            idx += 2
        elif opcode == JUMP_IF_TRUE:
            cond = get_value(code[idx + 1], modes[0])
            if cond:
                idx = get_value(code[idx + 2], modes[1])
            else:
                idx += 3
        elif opcode == JUMP_IF_FALSE: 
            cond = get_value(code[idx + 1], modes[0])
            if not cond:
                idx = get_value(code[idx + 2], modes[1])
            else:
                idx += 3
        elif opcode == LESS_THAN: 
            op1, op2 = args_to_values(code[idx + 1: idx + 1 + 2])
            out = code[idx + 3]
            if op1 < op2:
                write_at(out, 1)
            else:
                write_at(out, 0)
            idx += 4
        elif opcode == EQUALS: 
            op1, op2 = args_to_values(code[idx + 1: idx + 1 + 2])
            out = code[idx + 3]
            if op1 == op2:
                write_at(out, 1)
            else:
                write_at(out, 0)
            idx += 4
        elif opcode == REL_BASE:
            offset += get_value(code[idx + 1], modes[0])
            idx += 2
        else:
            raise Exception(f'Unknown opcode: {opcode} code: {code}')
    
    
# print(execute_file('in10', 1))
# print(execute_file('in11', 1))
# print(execute_file('in12', 1))
print(execute_file('in', 1))
