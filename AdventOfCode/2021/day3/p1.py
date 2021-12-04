file1 = open('in', 'r')
Lines = file1.readlines()
 

gamma = ""
epsil = ""

n = len(Lines)

for bit in range(0,len(Lines[0]) - 1):
    zeros = 0
    for line in Lines:
        if line[bit] == '0':
            zeros += 1
    if zeros > n - zeros:
        gamma += "0"
        epsil += "1"
    else:
        gamma += "1"
        epsil += "0"
    
print(int(gamma, 2) * int(epsil, 2))
