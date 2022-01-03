inp = '''nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6'''

#cmds = [[op, int(off)] for ent in inp.split('\n') for op, off in ent.split() ]
cmds = []

	
cmds = [line.split() for line in inp.split('\n')]
for cmd in cmds:
	cmd[1] = int(cmd[1])

print(cmds)