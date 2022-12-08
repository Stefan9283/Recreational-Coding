
forest = list(map(str.rstrip, open('input').readlines()))



for idx, row in enumerate(forest):
    new_row = []
    for c in row:
        new_row.append(int(c))
    forest[idx] = new_row
    
Nrows = forest.__len__()
Ncols = forest[0].__len__()


import functools

def is_visible(forest, i, j) -> bool:
    Nrows = forest.__len__()
    Ncols = forest[0].__len__()
    
    h = forest[i][j]
    
    visible = [0, 0, 0, 0]
    
    for i_ in range(i - 1, -1, -1):
        visible[0] += 1
        if forest[i_][j] >= h:
            break
    for i_ in range(i + 1, Nrows):
        visible[1] += 1
        if forest[i_][j] >= h:
            break
    for j_ in range(j + 1, Ncols):
        visible[2] += 1
        if forest[i][j_] >= h:
            break
    for j_ in range(j - 1, -1, -1):
        visible[3] += 1
        if forest[i][j_] >= h:
            break
    
    return functools.reduce(lambda x, y: x * y, visible, 1)
    
import copy
visible = copy.deepcopy(forest)

for i in range(Nrows):
    for j in range(Ncols):
        visible[i][j] = is_visible(forest, i, j)
        
# print('\n'.join(str(row) for row in forest))
# print()
# print('\n'.join(str(row) for row in visible))

print(max([val for row in visible for val in row]))