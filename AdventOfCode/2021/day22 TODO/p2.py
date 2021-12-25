class Cube: pass

class Cube:
    def __init__(self, minVec: tuple[int], maxVec: tuple[int]):
        self.minVec = minVec
        self.maxVec = maxVec
    def __repr__(self):
        return str(self)
    def __str__(self):
        return '[min:' + str(self.minVec) + ', max:'+ str(self.maxVec) + ']'
    def volume(self):
        return \
            (1 + abs(self.minVec[0] - self.maxVec[0])) * \
            (1 + abs(self.minVec[1] - self.maxVec[1])) * \
            (1 + abs(self.minVec[2] - self.maxVec[2]))
    def min(vec1: tuple[int], vec2: tuple[int]):
        minV = []
        for c1, c2 in zip(vec1, vec2):
            minV.append(min(c1, c2))
        return tuple(minV)
    def max(vec1: tuple[int], vec2: tuple[int]):
        maxV = []
        for c1, c2 in zip(vec1, vec2):
            maxV.append(max(c1, c2))
        return tuple(maxV)
    def isInside(self, Vec: tuple):
        return \
                Vec[0] in range(self.minVec[0] + 1, self.maxVec[0]) and \
                Vec[1] in range(self.minVec[1] + 1, self.maxVec[1]) and \
                Vec[2] in range(self.minVec[2] + 1, self.maxVec[2]) 
    def isInsideOrOnEdge(self, Vec: tuple[int]):
        return \
                Vec[0] in range(self.minVec[0], self.maxVec[0] + 1) and \
                Vec[1] in range(self.minVec[1], self.maxVec[1] + 1) and \
                Vec[2] in range(self.minVec[2], self.maxVec[2] + 1) 
    def intersectNotOnEdge(self, c2: Cube) -> Cube:
        if self.isInside(c2.minVec):
            return Cube(c2.minVec, Cube.min(self.maxVec, c2.maxVec))
        if self.isInside(c2.maxVec):
            return Cube(Cube.max(c2.minVec, self.minVec), c2.maxVec)
        
        min_maxV = Cube.min(c2.maxVec, self.maxVec)
        max_minV = Cube.max(c2.minVec, self.minVec)
        if min_maxV not in [c2.maxVec, self.maxVec] or max_minV not in [c2.minVec, self.minVec]:
            return Cube(max_minV, min_maxV)    
    def intersect(self, c2: Cube) -> Cube:
        if self.isInsideOrOnEdge(c2.minVec):
            return Cube(c2.minVec, Cube.min(self.maxVec, c2.maxVec))
        if self.isInsideOrOnEdge(c2.maxVec):
            return Cube(Cube.max(c2.minVec, self.minVec), c2.maxVec)
        
        min_maxV = Cube.min(c2.maxVec, self.maxVec)
        max_minV = Cube.max(c2.minVec, self.minVec)
        if min_maxV not in [c2.maxVec, self.maxVec] or max_minV not in [c2.minVec, self.minVec]:
            return Cube(max_minV, min_maxV)    
        

    def subdivide(self, c2: Cube) -> list[Cube]:
        # if not c2.intersect(self): return [self]
        # returns a list of non overlapping AABBs that 
        # are inside of self but outside of c2
        x = sorted([self.minVec[0], c2.minVec[0], self.maxVec[0], c2.maxVec[0]])
        y = sorted([self.minVec[1], c2.minVec[1], self.maxVec[1], c2.maxVec[1]])
        z = sorted([self.minVec[2], c2.minVec[2], self.maxVec[2], c2.maxVec[2]])
        
        print('subdivide', self, x)

        # intervals
        x_ = [(x[i], x[i+1] - 1) for i in range(3)] + [(x[-1], x[-1])]
        y_ = [(y[i], y[i+1] - 1) for i in range(3)] + [(y[-1], y[-1])]
        z_ = [(z[i], z[i+1] - 1) for i in range(3)] + [(z[-1], z[-1])]

        aabbs = []
        for i in x_:
            print(i)
            for j in y_:
                for k in z_:
                    aabb = Cube((i[0], j[0], k[0]), (i[1], j[1], k[1]))
                    if aabb.intersect(c2) == None:
                        print(aabb)
                        aabbs.append(aabb)
        return aabbs

# c1 = Cube((0,0,0),(3,3,3))
# c2 = Cube((-3,0,-3),(0,3,0))
# print(c1.intersect(c2))

c1 = Cube((0,0,0),(3,3,3))
c2 = Cube((2,2,2),(2,2,2))
print(len(c1.subdivide(c2)))

# class Reactor:
#     def __init__(self):
#         self.on = []
#     def __str__(self):
#         return 'Lit:' + ' '.join(list(map(str, self.on)))
#     def getLit(self) -> int:
#         total = 0
#         for cube in self.on:
#             total += cube.volume()
#         return (total)
#     def turnOn(self, newcube):
#         on = []
#         for cube in self.on:
#             on.extend(cube.subdivide(newcube))
#         on.append(newcube)
#         self.on = on
#     def turnOff(self, newcube):
#         on = []
#         for cube in self.on:
#             on.extend(cube.subdivide(newcube))
#         self.on = on
    
# react = Reactor()

# for line in open('in').readlines():
#     line = line.strip('\n')
#     tok = line.replace('=', ' ').replace('.', ' ')\
#                     .replace(',', ' ').split()
    
#     x1 = int(tok[2])
#     x2 = int(tok[3])
#     y1 = int(tok[5])
#     y2 = int(tok[6])
#     z1 = int(tok[8])
#     z2 = int(tok[9])

#     if tok[0] == 'on': 
#         react.turnOn(Cube((x1,y1,z1), (x2,y2,z2)))
#     else:
#         react.turnOff(Cube((x1,y1,z1), (x2,y2,z2)))
#     print('\n', line, react.getLit(), '\n')
#     # print(react)
    
    
    
    
    
# print(react.getLit())

#
#
#
#   
# 10 ------ 12
#      11 ------- 13
# 10_11-1  11_12-1 12_13-1 13_13
#
# 5 ------------------------ 100
#            7 - 9
#
#  5-6 7-8 9-99 100-100
#
#
