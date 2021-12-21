
import json
import numpy as np
from scipy.spatial.transform import Rotation as R
from scipy.spatial.transform.rotation import Rotation
import time

def toRotMat(rot: list[int]):
    return R.from_euler('xyz', rot, degrees=True)
def toRotVec(rot, v):
    return list(map(int, toRotMat(rot).apply(v).round().tolist()))

scanners = {}
for line in open('in').readlines():
    line = line.strip('\n')
    if len(line) == 0: continue
    if line.startswith('---'):
        scanners[len(scanners)] = []
    else:
        scanners[len(scanners) - 1].append(json.loads('[' + line + ']'))


# generate all the possible rotations
rotations = []
angles = [0, 90, 180, 270]
for a in angles:
    for b in angles:
        for c in angles:
            rotations.append([a,b,c])
tmp = []
rotated = []
for rot in rotations:
    v = tuple(toRotVec(rot, [1,20,300]))
    if v in rotated: continue
    tmp.append(rot)
    rotated.append(v)
rotations = tmp
################################

def countBeacons(scan1, scan2, rot1, rot2) -> int:
    beac1 = [np.array(toRotVec(rot1, v)) for v in scanners[scan1]]
    beac2 = [np.array(toRotVec(rot2, v)) for v in scanners[scan2]]
    
    # we assume that b1 and b2 are one and the same
    for b1 in beac1:
        for b2 in beac2:
            count = 0
            distance = b1 - b2
            beac1tup = set(list(map(tuple, beac1)))
            beac2tup = set(list(map(lambda x: tuple((x + distance).tolist()), beac2)))
            common = beac1tup.intersection(beac2tup)
            if common.__len__() >= 12:
                return common.__len__(), distance
    return 1, []

def manhattanDistance(pos1: list[int], pos2: list[int]) -> int:
    d = 0
    for p1, p2 in zip(pos1, pos2):
        d += abs(p1 - p2)
    return d

def addDistToPos(dist: list[int], pos: list[int]) -> int:
    pos2 = []
    for d, p in zip(dist, pos):
        pos2.append(d + p)
    return tuple(pos2)


known = [0]
beacons = set()

coords = {0: (0, 0, 0)}

while len(known) != len(scanners):
    oldknown = list(known)
    for scan1 in oldknown:
        for scan2 in scanners:
            if scan2 in known: continue
            sc1, sc2 = scan1, scan2
            for rot in rotations:
                count, dist = countBeacons(sc1, sc2, rotations[0], rot)
                if count >= 12:
                    if sc2 not in known:
                        beacs = [(np.array(toRotVec(rot, v)) + np.array(dist)).tolist() for v in scanners[sc2]]
                        scanners[sc2] = beacs
                        coords[sc2] = tuple(dist)
                        known.append(sc2)
                    break
  
maxDist = 0
for scan1 in scanners:
    for scan2 in scanners:
        if scan1 >= scan2: continue
        d = manhattanDistance(coords[scan1], coords[scan2])
        maxDist = max(maxDist, d)
           
for scanner in scanners:
    for beac in scanners[scanner]:
        beacons.add(tuple(beac))      
                          
print('unique beacons', len(beacons))
print('max distance between 2 beacons', maxDist)

