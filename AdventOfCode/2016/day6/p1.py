
lines = [line.strip('\n') for line in open('in').readlines()]

occurs = [ {} for _ in range(len(lines[0]))]

message = []

for i in range(len(lines[0])):
    for line in lines:
        if occurs[i].get(line[i]) == None: occurs[i][line[i]] = 0
        occurs[i][line[i]] += 1
    mostcommon = max(occurs[i], key=lambda c: occurs[i][c])
    message.append(mostcommon)
    
print(''.join(message))
