
X = 1
cycle = 0
signal_strenghts = []

def add_signal_strenght(strenghts, cycle, X):
    if (cycle - 20) % 40 == 0 or cycle == 20:
        strenghts.append(X * cycle)
        print(cycle, X)
    else:
        print(cycle, 'dud')
for op in open('in0').readlines():
    tok = op.rstrip().split()
    print(tok)
    if tok[0] == 'noop':
        cycle += 1
        add_signal_strenght(signal_strenghts, cycle, X)
    elif tok[0] == 'addx':
        cycle += 1
        add_signal_strenght(signal_strenghts, cycle, X)
        cycle += 1
        X += int(tok[1])
        add_signal_strenght(signal_strenghts, cycle, X)
        
print(signal_strenghts, sum(signal_strenghts))