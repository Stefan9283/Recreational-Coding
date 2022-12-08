
forest = list(map(str.rstrip, open('input').readlines()))



for idx, row in enumerate(forest):
    new_row = []
    for c in row:
        new_row.append(int(c))
    forest[idx] = new_row
    
Nrows = forest.__len__()
Ncols = forest[0].__len__()


def is_visible(forest, i, j) -> bool:
    Nrows = forest.__len__()
    Ncols = forest[0].__len__()
    
    h = forest[i][j]
    
    visible = [True] * 4
    
    for i_ in range(i - 1, -1, -1):
        if forest[i_][j] >= h:
            visible[0] = False
            break
    for i_ in range(i + 1, Nrows):
        if forest[i_][j] >= h:
            visible[1] = False
            break
    for j_ in range(j + 1, Ncols):
        if forest[i][j_] >= h:
            visible[2] = False
            break
    for j_ in range(j - 1, -1, -1):
        if forest[i][j_] >= h:
            visible[3] = False
            break
    return any(visible)
    
import copy
visible = copy.deepcopy(forest)

for i in range(Nrows):
    for j in range(Ncols):
        if is_visible(forest, i, j):
            visible[i][j] = 1
        else:
            visible[i][j] = 0
        

        
# print('\n'.join(str(row) for row in forest))
# print()
# print('\n'.join(str(row) for row in visible))

print(sum([val for row in visible for val in row ]))