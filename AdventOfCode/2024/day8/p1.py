
with open('in', 'r') as f:
    input = list(map(lambda x: list(x.rstrip()), f.readlines()))
    output = [list(row) for row in input]
    
antennas = {}

for i, row in enumerate(input):
    for j, freq in enumerate(row):
        if freq == '.': continue
        if freq not in antennas.keys():
            antennas[freq] = []
        antennas[freq].append((i, j))

for freq, antenna in antennas.items():
    for i in range(len(antenna)):
        for j in range(i+1, len(antenna)):
            pos1, pos2 = antenna[i], antenna[j]
            diff = (pos1[0] - pos2[0], pos1[1] - pos2[1])
            p3 = (pos1[0] + diff[0], pos1[1] + diff[1])
            p4 = (pos2[0] - diff[0], pos2[1] - diff[1])
            diff = (-diff[0], -diff[1])
            print(p3, pos1, pos2, p4)
            
            x, y = p3
            if x in range(len(output)) and y in range(len(output[0])):
                output[x][y] = '#'
            x, y = p4
            if x in range(len(output)) and y in range(len(output[0])):
                output[x][y] = '#'
            
    # print(freq, antenna)


output = '\n'.join([''.join(row) for row in output])
print(output, output.count('#'))
