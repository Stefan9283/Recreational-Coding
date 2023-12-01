
import math

map = []

x_station, y_station, input_file = 16, 8, 'in'
# x_station, y_station, input_file = 13, 11, 'in1'
# x_station, y_station, input_file = 3, 8, 'in0'

with open(input_file) as f:
    for line in f.readlines():
        line = line.rstrip()
        map.append(line)

# print(map[x_station][y_station])

h, w = len(map), len(map[0])

asteroids_at_angles = {}

for i in range(len(map)):
    for j in range((len(map[0]))):
        if map[i][j] == '#' and \
            (i, j) != (x_station, y_station):

            length = math.sqrt(
                math.pow(i - x_station, 2) +
                math.pow(j - y_station, 2)
            )
            
            v = [-1, 0]
            w = [
                (i - x_station) / length, 
                (j - y_station) / length
            ]
                        
            # angle = (math.degrees(math.atan2(j - y_station, i - x_station)) + 90) % 360

            angle = - math.atan2(
                w[1] * v[0] - w[0] * v[1],
                w[0] * v[0] + w[1] * v[1],
            ) * 180 / math.pi
          
            if angle not in asteroids_at_angles:
                asteroids_at_angles[angle] = [ (i, j) ]
            else:
                asteroids_at_angles[angle].append( (i, j) )

for angle in asteroids_at_angles:
    asteroids_at_angles[angle] = sorted(asteroids_at_angles[angle], key=lambda x: math.sqrt(
                math.pow(x[0] - x_station, 2) +
                math.pow(x[1] - y_station, 2)
            ))

angles = sorted(list(asteroids_at_angles.keys()))

print(asteroids_at_angles)
print(angles)


circ_idx = angles.index(0)


count = 1
checked = 0
while True:
    angle = angles[circ_idx]
    # print(circ_idx, )
    circ_idx += 1
    circ_idx %= len(angles)
    asteroids = asteroids_at_angles[angle]
    checked += 1
    if len(asteroids):
        removed = asteroids[0]
        asteroids_at_angles[angle] = asteroids[1:]
        print(count, removed, removed[1] * 100 + removed[0], "{angle:.2f}".format(angle=angle))
        count += 1
        checked = 0
    if checked == len(angles):
        break
    if count > 200:
        break
