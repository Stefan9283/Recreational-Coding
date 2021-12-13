file1 = open('in1', 'r')
Lines = file1.readlines()

            # numOfChars  | Value
numOfLines = {
                2:             1, 
                4:             4, 
                3:             7, 
                7:             8
            }

count = 0
for l in Lines:
    for tok in l.split('|')[1].strip('\n').split():
        if numOfLines.get(len(tok)) != None:
            count += 1
    
print(count)
