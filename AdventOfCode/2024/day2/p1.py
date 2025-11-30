


with open('in', 'r') as f:
    m = list(map(lambda x: list(map(int, x.rstrip().split())), f.readlines()))

safe = 0
for row in m:
    sortd = sorted(row)
    if row == sortd or row == list(reversed(sortd)):
        max_diff = 0
        min_diff = abs(row[0] - row[1])
        for i in range(len(row) - 1):
            diff = abs(row[i] - row[i + 1])
            max_diff = max(max_diff, diff)
            min_diff = min(min_diff, diff)
        if max_diff >= 1 and max_diff <= 3 and min_diff > 0:
            safe += 1
print(safe)
