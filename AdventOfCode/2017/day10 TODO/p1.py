

input = [int(num) for num in open('in').read() \
        .strip('\n').replace(' ', '').split(',')]

v = [i for i in range(5)]

# print(input)

def reverse(l: list[int], start: int, end: int) -> list[int]:
    if start < end:
        e1 = l[:start]
        e2 = l[end:]
        mid = l[start:end]
        return l[:start] + l[start:end][::-1] + l[end:]
    else:
        e1 = l[start:]
        e2 = l[:end]
        mid = l[end:start]
        edges = e1 + e2
        edges.reverse()
        cut = len(l) - end
        return edges[cut:] + mid + edges[:cut] 



# print(reverse([3, 0, 1, 2, 4], 3, 2))

# skipSize = 0
# current  = 0

# N = len(v)
# print(v)

# for size in input:
#     end = (current + size) % N
#     v = reverse(v, current, end)
#     print(current, end, v)
#     current = (current + size + skipSize) % N
#     skipSize += 1
    
v = reverse([0, 1, 2, 3, 4], 0, 3)
print(v)
v = reverse([2, 1, 0, 3, 4], 3, 2)
print(v)
v = reverse([3, 0, 1, 2, 4], 3, 4)
print(v)
v = reverse(v, 1, 1)
print(v)
    
# print(v[0] * v[1])

# [3, 4, 1, 5]
# [0, 1, 2, 3, 4]
# #############################
# [[0], 1, 2, 3, 4]
# (0, 3)->[2, 1, 0, [3], 4]
# (3, 2)->[4, [3], 0, 1, 2]
# (3, 4)->[4, 3, 0, [1], 2]
# (1, 1)->2

# [[0] 1 2 3 4] 0 3                         [2 1 0 [3] 4]
# [2 1 0 [3] 4] 0 + 3 + 0 = 3, 4            [4 3 0 [1] 2]
# [4 3 0 [1] 2] 3 + 4 + 1 = 8 % 5 = 3, 1    [4 [3] 0 1 2]
# [4 [3] 0 1 2] 3 + 5 + 2 = 10 % 5 = 0, 5   [3 4 2 1 [0]]
