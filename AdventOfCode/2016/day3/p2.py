def isTriangleValid(edges):
    a,b,c = edges
    return a + b > c and a + c > b and b + c > a

triangles = []
i = 0
for line in open('in').readlines():
    if i == 0:
        triangles.append([])        
        triangles.append([])        
        triangles.append([])        
    i = (i + 1) % 3
    line = line.strip('\n')
    vals = [int(num) for num in line.split()]
    for tri in range(1, 4):
        triangles[- tri].append(vals[tri - 1])
        
print([isTriangleValid(edges) for edges in triangles].count(True))