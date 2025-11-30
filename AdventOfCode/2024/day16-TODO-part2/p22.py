
with open('in', 'r') as f:
    MAP = list(map(lambda x: list(x.rstrip()), f.readlines()))

# print('\n'.join([''.join(line) for line in MAP]))

S, E = None, None

for i in range(len(MAP)):
    for j in range(len(MAP[i])):
        if MAP[i][j] == 'S':
            S = (i, j)
        if MAP[i][j] == 'E':
            E = (i, j)

print(S, E)

from enum import Enum
import math
lowest_score = math.inf 

stack = [(S, (0, 1), 0)]

class RotationDir(Enum):
    LEFT = 1
    RIGHT = 2
def rotate(dir, rot: RotationDir):
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    dir_idx = dirs.index(dir)
    if rot == RotationDir.LEFT:
        dir_idx -= 1
    else:
        dir_idx += 1
    
    if dir_idx == 4:
        dir_idx = 0
    
    return dirs[dir_idx]
    
# key = (pos, dir)
smallest_score_to_get_to = {}
shortest_path_to_get_to = {}

stack = [(S, (0, 1), 0)]

rotated = set()

while stack:
    # print(stack)
    stack.sort(key=lambda x: x[2])
    (pos, dir, score) = stack.pop(0)

    if (pos, dir) not in smallest_score_to_get_to.keys():
        smallest_score_to_get_to[(pos, dir)] = score
    else:
        if score < smallest_score_to_get_to[(pos, dir)]:
            smallest_score_to_get_to[(pos, dir)] = score
            shortest_path_to_get_to[]
        smallest_score_to_get_to[(pos, dir)] = min(score, smallest_score_to_get_to[(pos, dir)])
    
    # front
    next_pos = (pos[0] + dir[0], pos[1] + dir[1])
    if MAP[next_pos[0]][next_pos[1]] != '#':
        stack.append((next_pos, dir, score+1))
        
    # rotate -90 90 and 180 degrees
    if pos in rotated: continue
    stack.append((pos, rotate(dir, RotationDir.LEFT),  score+1000))
    stack.append((pos, rotate(rotate(dir, RotationDir.LEFT), RotationDir.LEFT),  score+2000))
    stack.append((pos, rotate(dir, RotationDir.RIGHT), score+1000))
    rotated.add(pos)
    
for (pos, _) in smallest_score_to_get_to:
    MAP[pos[0]][pos[1]] = 'O'
    
print('\n'.join([''.join(line) for line in MAP]))

print(smallest_score_to_get_to)
    
ret = math.inf
for key, val in smallest_score_to_get_to.items():
    (pos, dir) = key
    if pos != E: continue
    print(key, val)
    ret = min(ret, val)
    


print(ret)
