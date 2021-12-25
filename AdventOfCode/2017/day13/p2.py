import collections

firewall = {}

max_depth = 0
for line in open('in').readlines():
    Depth, Range = map(int, line.strip('\n').split(': '))
    firewall[Depth] = Range
    max_depth = max(max_depth, Depth)


offset = 0
while True:
    caught = 0
    for step in firewall:
        i = (step + offset) % (2 * firewall[step] - 2)
        if i >= firewall[step]:
            isAt = firewall[step] - (i - firewall[step] + 2)
        else:
            isAt = i
        # print(step, isAt)
        if isAt == 0:
            caught += 1
    if caught == 0:
        print('lowest offset', offset)
        break
    offset += 1

    
# picosec 0
#  0   1   2   3   4   5   6
# [S] [S] ... ... [S] ... [S]
# [ ] [ ]         [ ]     [ ]
# [ ]             [ ]     [ ]
#                 [ ]     [ ]

# picosec 1
#  0   1   2   3   4   5   6
# [ ] [ ] ... ... [ ] ... [ ]
# [S] [S]         [S]     [S]
# [ ]             [ ]     [ ]
#                 [ ]     [ ]

# picosec 2
#  0   1   2   3   4   5   6
# [ ] [S] ... ... [ ] ... [ ]
# [ ] [ ]         [ ]     [ ]
# [S]             [S]     [S]
#                 [ ]     [ ]

# picosec 3
#  0   1   2   3   4   5   6
# [ ] [ ] ... ... [ ] ... [ ]
# [S] [S]         [ ]     [ ]
# [ ]             [ ]     [ ]
#                 [S]     [S]

# picosec 4
#  0   1   2   3   4   5   6
# [S] [S] ... ... [ ] ... [ ]
# [ ] [ ]         [ ]     [ ]
# [ ]             [S]     [S]
#                 [ ]     [ ]

# picosec 5
#  0   1   2   3   4   5   6
# [ ] [ ] ... ... [ ] ... [ ]
# [S] [S]         [S]     [S]
# [ ]             [ ]     [ ]
#                 [ ]     [ ]

# picosec 6
#  0   1   2   3   4   5   6
# [ ] [S] ... ... [S] ... [S]
# [ ] [ ]         [ ]     [ ]
# [S]             [ ]     [ ]
#                 [ ]     [ ]

# picosec 7
#  0   1   2   3   4   5   6
# [ ] [ ] ... ... [ ] ... [ ]
# [S] [S]         [S]     [S]
# [ ]             [ ]     [ ]
#                 [ ]     [ ]

# picosec 8
#  0   1   2   3   4   5   6
# [S] [S] ... ... [ ] ... [ ]
# [ ] [ ]         [ ]     [ ]
# [ ]             [S]     [S]
#                 [ ]     [ ]

# picosec 9
#  0   1   2   3   4   5   6
# [ ] [ ] ... ... [ ] ... [ ]
# [S] [S]         [ ]     [ ]
# [ ]             [ ]     [ ]
#                 [S]     [S]

# picosec 10
#  0   1   2   3   4   5   6
# [ ] [S] ... ... [ ] ... [ ]
# [ ] [ ]         [ ]     [ ]
# [S]             [S]     [S]
#                 [ ]     [ ]

# picosec 11
#  0   1   2   3   4   5   6
# [ ] [ ] ... ... [ ] ... [ ]
# [S] [S]         [S]     [S]
# [ ]             [ ]     [ ]
#                 [ ]     [ ]

# picosec 12
#  0   1   2   3   4   5   6
# [S] [S] ... ... [S] ... [S]
# [ ] [ ]         [ ]     [ ]
# [ ]             [ ]     [ ]
#                 [ ]     [ ]