total = 0

for line in [l.strip('\n') for l in open('in').readlines()]:
    chars = len(line)
    
    content = chars - 2 - line.count("\\\"")
    print(line)

    line = line.replace("\\\"", '')
    print(line)
    
    content -=  line.count("\\\\")     
    line =  line.replace("\\\\", '')
    print(line)
    
    content -= line.count('\\x') * 3
    
    print(chars, content)
    total += chars - content
    
print(total)    
