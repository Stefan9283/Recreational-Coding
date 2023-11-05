input = '01111010110010011'

# p1
size = 272

# p2
size = 35651584

def fill(input: str, target_size: int = size) -> str:
    a = input
    b = input[::-1]
    b = b.replace('0', '2')
    b = b.replace('1', '0')
    b = b.replace('2', '1')
    
    a = a + '0' + b
    
    if a.__len__() < target_size:
        return fill(a, target_size)
    
    return a[:target_size]
    
def checksum(input: str) -> str:
    if input.__len__() % 2 == 1:
        return input

    output = ''
    
    for i in range(0, input.__len__(), 2):
        group = input[i:i+2]
        output += {
            '11': '1',
            '00': '1',
            '10': '0',
            '01': '0',
        }[group]

    return checksum(output)

print(checksum(fill(input)))
