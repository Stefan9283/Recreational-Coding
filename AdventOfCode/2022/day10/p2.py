
X = 1
cycle = 0
signal_strenghts = []

def add_signal_strenght(strenghts, cycle, X):
    if cycle % 40 in [X, X + 1, X - 1]:
        strenghts.append('#')
    else:
        strenghts.append('.')
    
        
for op in open('in').readlines():
    tok = op.rstrip().split()
    if tok[0] == 'noop':
        add_signal_strenght(signal_strenghts, cycle, X)
        cycle += 1
    elif tok[0] == 'addx':
        add_signal_strenght(signal_strenghts, cycle, X)
        cycle += 1
        add_signal_strenght(signal_strenghts, cycle, X)
        cycle += 1
        X += int(tok[1])


display = '\n'.join([
    ''.join(signal_strenghts[0:40]),
    ''.join(signal_strenghts[40:80]),
    ''.join(signal_strenghts[80:120]),
    ''.join(signal_strenghts[120:160]),
    ''.join(signal_strenghts[160:200]),
    ''.join(signal_strenghts[200:240]),
])

print(display)

    
# print(''.join(signal_strenghts), signal_strenghts.__len__())