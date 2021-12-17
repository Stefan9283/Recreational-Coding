import re

input = open('in').read().strip('\n')
# print(input)

aftercancel = []
i = 0
while i != len(input):
    if input[i] == '!':
        i += 1
    else:
        aftercancel.append(input[i])
    i += 1
aftercancel = ''.join(aftercancel)
# print(aftercancel)

aftercleanup = []
i = 0

garbage = 0

stack = []
while i != len(aftercancel):
    if aftercancel[i] == '>':
        garbage += len(stack) - 1
        stack = []
    elif aftercancel[i] == '<':
        stack.append('<')
    elif not stack:
        aftercleanup.append(aftercancel[i])
    else:
        garbage += 1
    i += 1
aftercleanup = ''.join(aftercleanup)
# print(aftercleanup)


score = 0
brackets = 0
i = 0
while i != len(aftercleanup):
    if aftercleanup[i] == '{':
        brackets += 1
    elif aftercleanup[i] == '}':
        score += brackets
        brackets -= 1
    i += 1
    
print(score, garbage)
