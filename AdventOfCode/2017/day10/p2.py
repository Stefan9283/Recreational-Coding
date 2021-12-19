input = [ord(num) for num in open('in').read() \
        .strip('\n')] + [17, 31, 73, 47, 23]

v = [i for i in range(256)]

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

for _ in range(64):
    for size in input:
        end = (current + size) % N
        w = list(v)
        w[end - 1] = (v[end - 1],)
        w[current] = [w[current]]
        
        v = reverse(v, current, end)
        current = (current + size + skipSize) % N
        skipSize += 1
   
import functools
    
hash = []
for i in range(256//16):
    s = list(hex(functools.reduce(lambda x, y: x ^ y, v[i * 16 : (i + 1) * 16], 0)))[2:]
    if len(s) == 1:
        s.insert(0, '0')
    hash.append(''.join(s))
hash = ''.join(hash)
print(hash)