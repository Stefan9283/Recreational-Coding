file1 = open('in1', 'r')
Lines = file1.readlines()

grid = [[int(c) for c in l.strip('\n')] for l in Lines]

for row in grid:
    print(row)

s = 0


for i in range(0, len(grid)):
    for j in range(0, len(grid[i])):
        neigh = [grid[i][j]]
        if i != 0: neigh.append(grid[i - 1][j])
        if i != len(grid) - 1: neigh.append(grid[i + 1][j])
        if j != 0: neigh.append(grid[i][j - 1])
        if j != len(grid[i]) - 1: neigh.append(grid[i][j + 1])
        if min(neigh) == grid[i][j] and neigh.count(grid[i][j]) == 1:
            print(grid[i][j])
            s += 1 + grid[i][j]
print(s)
