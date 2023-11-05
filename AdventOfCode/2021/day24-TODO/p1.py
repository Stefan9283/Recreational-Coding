

def runMONAD(num: int) -> int:
    vars = {
        'x' : 0,
        'y' : 0,
        'z' : 0,
        'w' : 0,
    }

    def getValue(s: str):
        if vars.get(s) != None:
            return vars[s]
        return int(s)

    inp = [int(x) for x in str(13579246899999)]
    inp_cursor = 0
    inp_len = len(str(13579246899999))

    for cmd in open('in').readlines():
        cmd = cmd.strip('\n').split()
        # print(cmd)
        if cmd[0] == 'inp': 
            vars[cmd[1]] = int(inp[inp_cursor])
            inp_cursor += 1
            inp_cursor %= inp_len
        elif cmd[0] == 'add': 
            vars[cmd[1]] += getValue(cmd[2])
        elif cmd[0] == 'mul': 
            vars[cmd[1]] *= getValue(cmd[2])
        elif cmd[0] == 'div': 
            vars[cmd[1]] //= getValue(cmd[2])
        elif cmd[0] == 'mod': 
            vars[cmd[1]] %= getValue(cmd[2])
        elif cmd[0] == 'eql': 
            if vars[cmd[1]] == getValue(cmd[2]):
                vars[cmd[1]] = 1
            else:
                vars[cmd[1]] = 0
        
    return vars['z']


for num in range(99999999999999, 10000000000000, -1):
    if str(num).find('0') != -1: continue
    print(num)
    if runMONAD(num) == 1:
        print(num)
        break
