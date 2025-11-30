
with open('in', 'r') as f:
    lines = list(map(lambda x: x.rstrip(), f.readlines()))

def check_left_top_to_bottom_right(i, j, word):
    if j + (len(word) - 1) >= len(lines[0]):
        return False
    if i + (len(word) - 1) >= len(lines):
        return False
    word_ = ''
    for i_ in range(len(word)):
        word_ += lines[i + i_][j + i_]
    return word_ == word    

def check_left_bottom_to_bottom_top(i, j, word):
    if j + (len(word) - 1) >= len(lines[0]):
        return False
    if i - (len(word) - 1) < 0:
        return False
    word_ = ''
    for i_ in range(len(word)):
        word_ += lines[i - i_][j + i_]
    return word_ == word 

xmases = 0

for i in range(len(lines) - 2):
    for j in range(len(lines[0])):
        if lines[i][j] == 'M' or lines[i][j] == 'S':
            results = [func(i, j) for func in [\
                lambda x, y: check_left_bottom_to_bottom_top(x+2, y, 'MAS'),
                lambda x, y: check_left_top_to_bottom_right(x, y, 'MAS'),
                lambda x, y: check_left_bottom_to_bottom_top(x+2, y, 'SAM'),
                lambda x, y: check_left_top_to_bottom_right(x, y, 'SAM')
                ]]
            if results.count(True) == 2:
                xmases += 1
        
print(lines, xmases)
