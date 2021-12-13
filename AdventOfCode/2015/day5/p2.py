import re

f = open("in")

nice = 0

for line in f.readlines():
    line = line.strip('\n')
    
    if re.match("[a-zA-Z]*([a-zA-Z][a-zA-Z])[a-zA-Z]*\\1[a-zA-Z]*", line) != None \
        and re.match("[a-zA-Z]*([a-zA-Z])[a-zA-Z]\\1[a-zA-Z]*", line) != None:
        print(line)
        nice += 1

print(nice)    
    