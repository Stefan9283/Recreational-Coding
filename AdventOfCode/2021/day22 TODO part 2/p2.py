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
    def isInside(self, Vec: tuple[int]):
        return \
                Vec[0] in range(self.minVec[0], self.maxVec[0] + 1) and \
                Vec[1] in range(self.minVec[1], self.maxVec[1] + 1) and \
                Vec[2] in range(self.minVec[2], self.maxVec[2] + 1) 
    def intersect(self, c2: Cube) -> Cube:
        if self.isInside(c2.minVec):
            return Cube(c2.minVec, Cube.min(self.maxVec, c2.maxVec))
        if self.isInside(c2.maxVec):
            return Cube(Cube.max(c2.minVec, self.minVec), c2.maxVec)
        
        min_maxV = Cube.min(c2.maxVec, self.maxVec)
        max_minV = Cube.max(c2.minVec, self.minVec)
        if min_maxV not in [c2.maxVec, self.maxVec] or max_minV not in [c2.minVec, self.minVec]:
            return Cube(max_minV, min_maxV)    
        

    def subdivide(self, c2: Cube) -> list[Cube]:
        aabbs = []
        # https://stackoverflow.com/questions/66135217/how-to-subdivide-set-of-overlapping-aabb-into-non-overlapping-set-of-aabbs
        # https://adventofcode.com/2021/day/22
        # if not c2.intersect(self): return [self]
        # returns a list of non overlapping AABBs that 
        # are inside of self but outside of c2
        x = [self.minVec[0], self.maxVec[0]]
        y = [self.minVec[1], self.maxVec[1]]
        z = [self.minVec[2], self.maxVec[2]]
        
        if c2.minVec[0] in range(x[0], x[1] + 1):
            if c2.minVec[0] in x: x.remove(c2.minVec[0])
            x.append(c2.minVec[0] - 1)
            x.append(c2.minVec[0] + 1)
        if c2.minVec[1] in range(y[0], y[1] + 1):
            if c2.minVec[1] in y: y.remove(c2.minVec[1])
            y.append(c2.minVec[1] - 1)
            y.append(c2.minVec[1] + 1)
        if c2.minVec[2] in range(z[0], z[1] + 1):
            if c2.minVec[2] in z: z.remove(c2.minVec[2])
            z.append(c2.minVec[2] - 1)
            z.append(c2.minVec[2] + 1)
            
        if c2.maxVec[0] in range(x[0], x[1] + 1):
            if c2.maxVec[0] in x: x.remove(c2.maxVec[0])
            x.append(c2.maxVec[0] - 1)
            x.append(c2.maxVec[0] + 1)
        if c2.maxVec[1] in range(y[0], y[1] + 1):
            if c2.maxVec[1] in y: y.remove(c2.maxVec[1])
            y.append(c2.maxVec[1] - 1)
            y.append(c2.maxVec[1] + 1)
        if c2.maxVec[2] in range(z[0], z[1] + 1):
            if c2.maxVec[2] in z: z.remove(c2.maxVec[2])
            z.append(c2.maxVec[2] - 1)
            z.append(c2.maxVec[2] + 1)
        
        x.sort()
        y.sort()
        z.sort()
        x = list(set(x))
        y = list(set(y))
        z = list(set(z))
            
        print('subdivide', self, c2)
        print(x,y,z)
        for i in range(len(x) - 1):
            print(i)
            tmpy = list(y)
            for j in range(len(y) - 1):
                tmpz = list(z)
                for k in range(len(z) - 1):
                    aabb = Cube((x[i], y[j], z[i]), (x[i + 1], y[j + 1], z[k + 1]))
                    print(aabb)
        #             if aabb.intersect(c2) == None:
        #                 print(aabb)
        #                 aabbs.append(aabb)
                    z[k + 1] += 1
                z = tmpz
                y[j + 1] += 1
            y = tmpy
            x[i + 1] += 1
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
