


nums = list(map(lambda x: int(x), open('in').read().split()))
# print(nums)


def buildTree(arr, depth):
    node_count = arr[0]
    meta_count = arr[1]
    curr = {'children': [], 'meta': []}
    rest = arr[2:]
    # print(node_count, meta_count, rest, depth)
    for _ in range(node_count):
        _, rest, value = buildTree(rest, depth+1)
        curr['children'].append(value)
    meta = rest[:meta_count]
    rest = rest[meta_count:]
    # print(node_count, meta_count, meta, depth)
    value = 0
    if node_count == 0:
        value = sum(meta)
    else:
        for idx in meta:
            if idx <= curr['children'].__len__():
                value += curr['children'][idx - 1]
    
    return curr, rest, value   
    
_, _, value = buildTree(nums, 0)
print(value)
