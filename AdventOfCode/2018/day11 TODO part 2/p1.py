
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

val = grid[0][0]
pos = None

for x in range(300 - 3):
    for y in range(300 - 3):
        cell_power = 0
        for i in range(3):
            for j in range(3):
                cell_power += grid[x + i][y + j]
        if cell_power > val:
            val = cell_power
            pos = (x, y)

print(val, pos)
