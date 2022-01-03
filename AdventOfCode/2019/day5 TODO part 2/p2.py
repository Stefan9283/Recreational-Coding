program = list(map(int, open('in').readline().split(',')))
pc = 0
input_val = 0

output = []

def val(n, mode) -> int:
    if mode == 1:
        return n
    return program[n]

def executeCmd(op, args, modes):
    global pc
    
    while len(modes) != 3:
        modes.append(0)
    ma, mb, mc = modes
    
    if len(args) == 3:
        a, b, res = args
        a = val(a, ma)
        b = val(b, mb)
    elif len(args) == 2:
        a, ptr = args
        a = val(a, ma)
        # ptr = val(a, mb)
      
    if op == 1:
        program[res] = a + b
    elif op == 2:
        program[res] = a * b
    elif op == 3:
        a = args[0]
        program[a] = input_val
    elif op == 4:
        a = args[0]
        output.append(program[a])
        
    elif op == 5: 
        if a != 0: pc = ptr
    elif op == 6: 
        if a == 0: pc = ptr
    elif op == 7: 
        program[res] = 0
        if a < b:
            program[res] = 1
    elif op == 8: 
        
        program[res] = 0
        if a == b:
            program[res] = 1

print(program)

while program[pc] != 99:
    print(pc, '/', len(program), program, output)
    cmd = str(program[pc])
    op = int(cmd[-1])
    # print("original cmd", cmd, pc)
    args = []
    args.append(program[pc + 1])
    # print(pc)
    # print(pc, '/', len(program))
    
    if op in [1, 2, 7, 8]:
        args.append(program[pc + 2])
        args.append(program[pc + 3])
        pc += 4
    elif op in [5, 6]:
        args.append(program[pc + 2])
        pc += 3
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
    

