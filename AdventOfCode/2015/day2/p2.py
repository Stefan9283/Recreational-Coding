f = open("in")

ribbon = 0
for line in f.readlines():
    l, w, h = [int(num) for num in line.strip('\n').split('x')]
    dims = [l, w, h]
    dims.sort()
    ribbon += 2 * (dims[0] + dims[1]) + l * w * h
print(ribbon)    