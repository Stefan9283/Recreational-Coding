input = [int(num) for num in open('in').read() \
        .strip('\n').replace(' ', '').split(',')]

v = [i for i in range(256)]

# print(input)

def reverse(l: list[int], start: int, end: int) -> list[int]:
    if start == end:
        return l
    if start < end:
        mid = l[start:end]
        mid.reverse()
        return l[:start] + mid + l[end:]
    else:
        e1 = l[start:]
        e2 = l[:end]
        edges = e1 + e2
        edges.reverse()
        i = len(edges) - end
        return edges[i:] + l[end:start] + edges[:i] 

skipSize = 0
current  = 0

N = len(v)
print(v)

for size in input:
    end = (current + size) % N
    w = list(v)
    w[end - 1] = (v[end - 1],)
    w[current] = [w[current]]
    
    v = reverse(v, current, end)
    
    print((current, end), (size, skipSize))
    print(w, '\n' + str(v))
    print()
    
    current = (current + size + skipSize) % N
    skipSize += 1
    
print(v[0] * v[1])
