f = open("in")

total = 0
for line in f.readlines():
    l, w, h = [int(num) for num in line.strip('\n').split('x')]
    dims = [l, w, h]
    dims.sort()
    total += 2 * (l * w + w * h + h * l) + dims[0] * dims[1]
print(total)    