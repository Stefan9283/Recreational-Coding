
calories = []

sum_f = sum
sum = 0

for line in open('input').readlines():
    line = line.rstrip()
    if line == '':
       calories.append(sum)
       sum = 0 
    else:
        sum += int(line)
calories.append(sum)

calories.sort()
print(max(calories))
print(sum_f(calories[-3:]))