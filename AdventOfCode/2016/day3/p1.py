def isTriangleValid(edges):
    a,b,c = edges
    return a + b > c and a + c > b and b + c > a

l = [isTriangleValid( \
    [int(num) for num in line.strip('\n').split()] \
    ) for line in open('in').readlines()]
print(l.count(True))