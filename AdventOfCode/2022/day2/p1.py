score = 0

def toInt(val: str):
    return {'A': 1, 'X': 1, 'B': 2, 'Y': 2, 'C': 3, 'Z': 3}[val]

for line in open('input').readlines():
    line = line.rstrip()
    opponent, me = line.split()
    opponent = toInt(opponent)
    me = toInt(me)
    if opponent == me:
        score += 3
    elif (opponent == 1 and me == 2) or (opponent == 2 and me == 3) or (opponent == 3 and me == 1):
        score += 6
    score += me
        
    print(score)