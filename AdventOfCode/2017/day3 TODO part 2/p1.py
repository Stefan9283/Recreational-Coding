import math

input = 325489

left = int(math.sqrt(input))
if left % 2 == 0: left -= 1

right = left + 2
d = (right**2 - left**2) // 4


for i in range(4):
    ends = [left**2 + 1 + i * d, left**2 + (i + 1) * d]
    if input in range(ends[0], ends[1] + 1):
        edgeCenter = sum(ends) // 2
        distanceToEdgeCenter = abs(edgeCenter - input)
        steps = distanceToEdgeCenter + (left + 1) // 2
        print(steps)
        break
   
    