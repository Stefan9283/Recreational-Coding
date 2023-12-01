import math

class Point2D:
    x, y = None, None
    
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
    def getCoords(self): 
        return (self.x, self.y)        
    def __str__(self):
        return 'Point2D(' + str(self.x) + ', ' + str(self.y) + ')'
    def __eq__(self, p) -> bool:
        return self.x == p.x and self.y == p.y
    
class Line2D:
    def __init__(self, p1: Point2D, p2: Point2D):
        self.x1, self.y1 = p1.getCoords()
        self.x2, self.y2 = p2.getCoords()
        
        try:
            self.m = (self.y2 - self.y1) / (self.x2 - self.x1)
        except:
            self.m = math.inf
        
    def has(self, p: Point2D) -> bool:
        x, y = p.getCoords()
        
        if self.y1 == self.y2:
            return x in range(min(self.x1, self.x2), max(self.x1, self.x2)) and \
                y == self.y1
        if self.x1 == self.x2:
            return y in range(min(self.y1, self.y2), max(self.y1, self.y2)) and \
                x == self.x1
        
        return  self.m * (self.x1 - x) == self.y1 - y and \
                y in range(min(self.y1, self.y2), max(self.y1, self.y2)) and \
                x in range(min(self.x1, self.x2), max(self.x1, self.x2))
        

def check_line_of_sight(pos1: Point2D, pos2: Point2D) -> bool:
    global map
    line = Line2D(pos1, pos2)
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == '.': continue
            p = Point2D(i, j)
            if p in [pos1, pos2]: continue
            if line.has(p):
                return False
    return True

def get_observable_asteroids(pos: Point2D) -> int:
    visible = 0
    global map
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == '.': continue
            if pos == Point2D(i, j): continue
            if check_line_of_sight(pos, Point2D(i, j)):
                visible += 1
    return visible


map = []

with open('in') as f:
    for line in f.readlines():
        line = line.rstrip()
        map.append(line)
        
max_count = 0

res_map = []

for i in range(len(map)):
    row = []
    for j in range(len(map[0])):
        if map[i][j] == '.': 
            row.append(' . ')
            continue
        ast_count = get_observable_asteroids(Point2D(i, j))
        row.append(str(ast_count))
        if ast_count >= max_count:
            max_count = ast_count
            print(i, j, max_count)
              
    res_map.append(row)

print('\n'.join(' '.join(line) for line in res_map))    

print(max_count)    

# print(Line2D(Point2D(4, 4), Point2D(0, 4)).has(Point2D(2, 4)))
