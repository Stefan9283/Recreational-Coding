import collections

players = {}

with open('in') as f:
    tok = f.readline().strip('\n').split()
    players[int(tok[1]) - 1] = {'pos': int(tok[-1]) - 1, 'score': 0}
    tok = f.readline().strip('\n').split()
    players[int(tok[1]) - 1] = {'pos': int(tok[-1]) - 1, 'score': 0}

diceSums = collections.defaultdict(int)
for i in range(1,4):
    for j in range(1,4):
        for k in range(1,4):
            diceSums[i + j + k] += 1

def playGame(players: dict) -> tuple[int]:
    states = {}
    
    def takeTurn(sc1, pos1, sc2, pos2) -> int: 
        key = tuple([sc1, pos1, sc2, pos2])
        target = 21
        if max([sc1, sc2]) >= target:
            if sc1 >= target: 
                states[key] = (1, 0)
            else:
                states[key] = (0, 1)

        if states.get(key) != None:
            return states[key]

        total = [0, 0]
        for diceSum in diceSums:
            pos1new = (pos1 + diceSum) % 10
            sc1new = sc1 + pos1new + 1
            won2, won1 = takeTurn(sc2, pos2, sc1new, pos1new)
            total[0] += diceSums[diceSum] * won1
            total[1] += diceSums[diceSum] * won2
        total = tuple(total)
        states[key] = total
        return total
 
    return takeTurn(
                players[0]['score'], players[0]['pos'],
                players[1]['score'], players[1]['pos']
            )

print(max(playGame(players)))
