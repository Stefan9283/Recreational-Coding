

line = open('in').readline().strip('\n')
print(line)

size = 0
while line:
    if line[-1] == ')':
        times = ''
        chars = ''
        line = line[:-1] # remove ')'
        
        print('\ta', line, size)
        
        while line[-1] != 'x':
            times = line[-1] + times
            line = line[:-1]
            print('\tb', line, times)
        
        line = line[:-1] # remove 'x'
        print('\tc', line, size)
        
        while line[-1] != '(':
            chars += line[-1]
            line = line[:-1] 
            print('\tc', line, chars)
            
        line = line[:-1] # remove ')'
        print('\te', line, size)
            
        print('\tfin', times, '--', chars)
    
        size += 
    
    else:
        size += 1
        line = line[:-1]
    
print(size)