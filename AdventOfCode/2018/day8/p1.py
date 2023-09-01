


nums = list(map(lambda x: int(x), open('in').read().split()))
# print(nums)

metasum = 0

def buildTree(arr, depth):
    global metasum
    node_count = arr[0]
    meta_count = arr[1]
    rest = arr[2:]
    # print(node_count, meta_count, rest, depth)
    for _ in range(node_count):
        rest = buildTree(rest, depth+1)
    meta = rest[:meta_count]
    rest = rest[meta_count:]
    # print(node_count, meta_count, meta, depth)
    metasum += sum(meta)
    return rest    
    
buildTree(nums, 0)
print(metasum)