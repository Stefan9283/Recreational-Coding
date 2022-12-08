score = 0

def toInt(val: str):
    return {'A': 1, 'X': 0, 'B': 2, 'Y': 3, 'C': 3, 'Z': 6}[val]

for line in open('input').readlines():
    line = line.rstrip()
    opponent, outcome = line.split()
    opponent = toInt(opponent)
    outcome = toInt(outcome)
    score += outcome
    
    if outcome == 0:
        me = opponent - 1
        if me == 0: me = 3
    elif outcome == 6:
        me = opponent + 1
        if me == 4: me = 1
    else:
        me = opponent

    score += me
    
print(score)