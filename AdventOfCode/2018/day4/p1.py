from datetime import datetime, timedelta
from pprint import pprint


guards = {}


lines = []
for line in open('in').readlines():
    line = line.strip('\n').replace('[', '').replace('-', ' ').replace(':', ' ').replace(']', '').split()
    date = list(map(lambda x: int(x), line[:5]))
    instr = line[5:]
    lines.append((date, instr))
    if instr[1].startswith('#'):
        instr[1] = int(instr[1][1:])
        guards[instr[1]] = { 'sleep_schedule': [ 0 ] * 60 }


lines.sort(key=lambda x: x[0])
current_guard = None
last_asleep = None
for line in lines:
    time, instr = line
    if instr[0] =='Guard':
        current_guard = instr[1]
    elif instr[0] == 'falls':
        last_asleep = time[-1]
        pass
    elif instr[0] == 'wakes':
        for i in range(last_asleep, time[-1]):
            guards[current_guard]['sleep_schedule'][i] += 1

### PART1
guard_sleep_counter = [(sum(guards[x]['sleep_schedule']), x) for x in guards]
guard_sleep_counter.sort(reverse=True) # sort by the first item
chosen_guard = guard_sleep_counter[0][1]


max_minute = 0
for minute in range(60):
    if guards[chosen_guard]['sleep_schedule'][minute] > guards[chosen_guard]['sleep_schedule'][max_minute]:
        max_minute = minute
        
print(chosen_guard * max_minute)    

    
### PART2
max_minute = 0
max_guard = list(guards.keys())[0]
for guard in guards:
    for minute in range(60):
        if guards[guard]['sleep_schedule'][minute] > guards[max_guard]['sleep_schedule'][max_minute]:
            max_minute = minute
            max_guard = guard

print(max_minute * max_guard)