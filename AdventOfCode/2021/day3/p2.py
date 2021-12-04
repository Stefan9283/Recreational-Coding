file1 = open('in', 'r')
Lines = file1.readlines()

oxi = ""
co = ""

bitsize = len(Lines[0]) - 1

remoxi = Lines
for bit in range(0,bitsize):
    zeros = 0
    n = len(remoxi)
    for line in remoxi:
        if line[bit] == '0':
            zeros += 1
    if zeros > n - zeros:
        oxi += "0"
        remoxi = [l for l in remoxi if l[bit] == '0']
    else:
        oxi += "1"
        remoxi = [l for l in remoxi if l[bit] == '1']

remco2 = Lines
for bit in range(0,bitsize):
    zeros = 0
    n = len(remco2)
    if n == 1:
        for i in range(bit, bitsize):
            co += remco2[0][i]
        break
    for line in remco2:
        if line[bit] == '0':
            zeros += 1
    if zeros <= n - zeros:
        co += "0"
        remco2 = [l for l in remco2 if l[bit] == '0']
        print(n, remco2, 0, zeros, n - zeros)
    else:
        co += "1"
        remco2 = [l for l in remco2 if l[bit] == '1']
        print(n, remco2, 1, zeros, n - zeros)
  
print(co, oxi)
print(int(oxi, 2) * int(co, 2))
