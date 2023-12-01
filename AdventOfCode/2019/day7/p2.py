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


class Program:

    def __init__(self, file, phase, id) -> None:
        self.code = list(map(lambda x: int(x), open(file).read().split(',')))
        self.used_phase = False
        self.idx = 0
        self.phase = phase
        self.last_out = 0
        self.id = id
        
    def halted(self):
        return self.code[self.idx] == 99
    
    def output(self):
        return self.last_out

    def run(self, input_) -> None:
        code = self.code
        idx = self.idx
        while True:
            opcode = code[idx] % 100
            modes = str(int(code[idx] / 100))
            while modes.__len__() != 3:
                modes = '0' + modes
            modes = [int(i) for i in reversed(modes)]

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
                code[out] = op1 + op2
                idx += 4
            elif opcode == MUL:
                op1, op2 = args_to_values(code[idx + 1: idx + 1 + 2])
                out = code[idx + 3]
                code[out] = op1 * op2
                idx += 4
            elif opcode == EXIT:
                self.idx = idx
                return
            elif opcode == SAVE: 
                out = code[idx + 1]
                if not self.used_phase:
                    code[out] = self.phase
                    self.used_phase = True
                else:
                    code[out] = input_
                idx += 2
            elif opcode == OUTPUT: 
                val = get_value(code[idx + 1], modes[0])
                self.idx = idx + 2
                self.last_out = val
                return
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
                    code[out] = 1
                else:
                    code[out] = 0
                idx += 4
            elif opcode == EQUALS: 
                op1, op2 = args_to_values(code[idx + 1: idx + 1 + 2])
                out = code[idx + 3]
                if op1 == op2:
                    code[out] = 1
                else:
                    code[out] = 0
                idx += 4
            else:
                raise Exception('Unknown opcode')
        
from itertools import permutations

max_thrust = 0

for phases in permutations(range(5, 10)):
    def test_config(phases):
        programs = [Program('in', phase=phases[i], id=i) for i in range(5)]
        while not all([p.halted() for p in programs]):
            for i in range(5):
                programs[i].run(programs[i - 1].output())
        return programs[4].output()
    
    max_thrust = max(max_thrust, test_config(phases))
    
print(max_thrust)