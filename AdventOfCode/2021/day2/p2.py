file1 = open('in', 'r')
Lines = file1.readlines()

y = 0
x = 0
aim = 0
for line in Lines:
    tok = line.split()
    num = int(tok[1])
    cmd = tok[0]
    if cmd == 'down':
        aim += num
    elif cmd == "up":
        aim -= num
    elif cmd == "forward":
        x += num
        y += aim * num
    
print(x * y)