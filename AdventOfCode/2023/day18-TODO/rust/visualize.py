import matplotlib.pyplot as plt
import numpy as np

f = open('data')
xpoints = []
ypoints = []
for line in f.readlines():
    x = int(line.rstrip()[1:-1].split(', ')[0])
    y = int(line.rstrip()[1:-1].split(', ')[1])
    xpoints.append(x)
    ypoints.append(y)

# tuples = []

# for (x, y) in zip(xpoints, ypoints):
#     tuples.append((x, y))
    
# tuples.sort(key=lambda x: x[1])

# # xpoints = np.array(xpoints)
# # ypoints = np.array(ypoints)

# xpoints = list(map(lambda x: x[0], tuples))
# ypoints = list(map(lambda x: x[1], tuples))

# print(xpoints)
# print(ypoints)

# plt.plot(xpoints, ypoints, 'ro-')
plt.scatter(xpoints, ypoints)

plt.show()