total = 0

for line in [l.strip('\n') for l in open('in').readlines()]:
    chars = len(line)
    
    content = chars + 4
    # print(chars, content)
    line = line[1:-1]
    # print(line)

    content += 2 * line.count("\\\"")
    # print(chars, content, 2 * line.count("\\\""), '\\\"')
    line = line.replace("\\\"", '')
    # print(line)
    
    content += 2 * line.count("\\\\")     
    # print(chars, content, 2 * line.count("\\\\"), '\\\\')
    line =  line.replace("\\\\", '')
    # print(line)
    
    content += line.count('\\x')
    # print(chars, content, line.count("\\x"), '\\x"')
    
    total += abs(chars - content)
print(total)    
