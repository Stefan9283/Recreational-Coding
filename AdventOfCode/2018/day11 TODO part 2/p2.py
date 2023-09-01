
serial = 9221

grid = [[0 for _ in range(300)] for _ in range(300)]

for x in range(300):
    for y in range(300):
        rackID = x + 10
        power = rackID * y
        power += serial
        power *= rackID
        power = int(power / 100) % 10
        power -= 5
        grid[x][y] = power


print(grid[10][:10])

# gridx = [[0 for _ in range(300)] for _ in range(300)]
# for x in range(0, 300):
#     s = 0
#     for y in range(300):
#         s += grid[x][y]
#         gridx[x][y] = s
# print(gridx[10][:10])


gridy = [[0 for _ in range(300)] for _ in range(300)]
for y in range(0, 300):
    s = 0
    for x in range(300):
        s += grid[x][y]
        gridy[x][y] = s
        
        
for i in range(10):
    print(grid[i][0], gridy[i][0])

