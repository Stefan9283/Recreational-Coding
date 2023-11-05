program = list(map(int, open('in').readline().split(',')))
pc = 0
input_val = 1

output = []

def val(n, mode) -> int:
    if mode == 1:
        return n
    return program[n]

def executeCmd(op, args, modes):
    if len(args) == 3:
        a, b, res = args
    
    while len(modes) != 3:
        modes.append(0)
    ma, mb, mc = modes
    
    
    # print(op, args, modes, '->', end=' ')
    if op == 1:
        program[res] = val(a, ma) + val(b, mb)
    elif op == 2:
        # print([val(a, ma), val(b, mb)], a, ma, b, mb)
        # print([val(a, ma), val(b, mb)])
        program[res] = val(a, ma) * val(b, mb)
    elif op == 3:
        a = args[0]
        # print(a)
        program[a] = input_val
        
    elif op == 4:
        a = args[0]
        # print(a)
        output.append(program[a])

# print(program)

while program[pc] != 99:
    cmd = str(program[pc])
    op = int(cmd[-1])
    print("original cmd", cmd, pc)
    args = []
    args.append(program[pc + 1])
    # print(pc)
    print(pc, '/', len(program))
    
    if cmd.endswith('1') or cmd.endswith('2'):
        args.append(program[pc + 2])
        args.append(program[pc + 3])
        pc += 4
    else: pc += 2
    
    modes = []
    if cmd.__len__() > 2:
        cmd = cmd[:-2]
        for c in cmd:
            modes.append(int(c)) 
        # print(modes)
        modes = list(modes.__reversed__())
    else:
        modes = [0, 0, 0]      
   
    executeCmd(op, args, modes)
    print(pc, program, output, "\n")

