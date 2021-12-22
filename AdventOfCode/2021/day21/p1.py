
players = {}

with open('in') as f:
    tok = f.readline().strip('\n').split()
    players[int(tok[1])] = {'pos': int(tok[-1]) - 1, 'score': 0}
    tok = f.readline().strip('\n').split()
    players[int(tok[1])] = {'pos': int(tok[-1]) - 1, 'score': 0}

def gen3() -> int:
    current = 1
    while True:
        yield current
        current += 1
        if current >= 1000:
            current = 1

gen = gen3()

step = 0
while players[1]['score'] < 1000 and players[2]['score'] < 1000:
    ID = step % 2 + 1
    step += 1
    diceSum = gen.__next__() + gen.__next__() + gen.__next__()
    players[ID]['pos'] += diceSum
    players[ID]['pos'] %= 10
    players[ID]['score'] += players[ID]['pos'] + 1

rolls = step * 3
    
print(rolls * min(players[1]['score'], players[2]['score']))