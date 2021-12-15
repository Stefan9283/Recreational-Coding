
seq = open('in').readline().strip('\n')

s = 0

# step = 1 # for part 1
step = len(seq) // 2 # for part 2

for i in range(len(seq)):
    if seq[i] == seq[i - step]: s += int(seq[i])
print(s)