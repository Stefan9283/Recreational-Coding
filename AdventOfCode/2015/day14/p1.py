
reindeer = []

for line in open('in').readlines():
    tok = line.strip('\n').split()
    name = tok[0]
    speed = int(tok[3])
    untilrest = int(tok[6])
    hastorest = int(tok[13])
    reindeer.append({'name': name, 'speed': speed, 'position': 0,
                     'restPeriod':   hastorest, 'runPeriod':   untilrest, 
                     'hasToRestFor': hastorest, 'canStillRun': untilrest})
    
    
secs = 2503

for sec in range(secs):
    print(sec + 1)
    for r in reindeer:
        if r['canStillRun'] != 0:
            r['canStillRun'] -= 1
            r['position'] += r['speed']
        elif r['hasToRestFor'] > 0:
            r['hasToRestFor'] -= 1
        else:
            r['hasToRestFor'] = r['restPeriod']
            r['canStillRun'] = r['runPeriod'] - 1
            r['position'] += r['speed']
        print('\t', [r['name'], r['position'], [r['canStillRun'], r['runPeriod']], [r['hasToRestFor'], r['restPeriod']]])
    print()

print(max(reindeer, key=lambda x: x['position']))
