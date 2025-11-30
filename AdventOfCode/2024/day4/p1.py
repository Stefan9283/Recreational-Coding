
with open('in', 'r') as f:
    lines = list(map(lambda x: x.rstrip(), f.readlines()))

def check_left_to_right(i, j, word):
    if j + (len(word) - 1) >= len(lines[0]):
        return False
    return lines[i][j:j+len(word)] == word

def check_top_to_bottom(i, j, word):
    if i + (len(word) - 1) >= len(lines):
        return False
    word_ = ''
    for i_ in range(len(word)):
        word_ += lines[i + i_][j]
    return word_ == word

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

for i in range(len(lines)):
    for j in range(len(lines[0])):
        if lines[i][j] == 'X':
            for func in [\
                lambda x, y: check_left_to_right(x, y, 'XMAS'),
                lambda x, y: check_top_to_bottom(x, y, 'XMAS'),
                lambda x, y: check_left_bottom_to_bottom_top(x, y, 'XMAS'),
                lambda x, y: check_left_top_to_bottom_right(x, y, 'XMAS')
                ]:
                if func(i, j):
                    xmases += 1 
        if lines[i][j] == 'S':
            for func in [\
                lambda x, y: check_left_to_right(x, y, 'SAMX'),
                lambda x, y: check_top_to_bottom(x, y, 'SAMX'),
                lambda x, y: check_left_bottom_to_bottom_top(x, y, 'SAMX'),
                lambda x, y: check_left_top_to_bottom_right(x, y, 'SAMX')
                ]:
                if func(i, j):
                    xmases += 1 
        
print(lines, xmases)
