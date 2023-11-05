
# 1 2 3
# 1 1 1

# 1 2 3
# 2 0 1

# 1 2 3
# 0 0 3
# --> 3


# 1 2 3 4
# 1 1 1 1 

# 1 2 3 4
# 2 0 1 1

# 1 2 3 4
# 2 0 2 0

# 1 2 3 4
# 4 0 0 0
# --> 1



# 1 2 3 4 5 6
# 1 1 1 1 1 1 

# 1 2 3 4 5 6
# 2 0 2 0 2 0

# 1 2 3 4 5 6
# 4 0 0 0 2 0

# 1 2 3 4 5 6
# 0 0 0 0 6 0
# --> 5


# 1 2 3 4 5 6 7
# 1 1 1 1 1 1 1

# 1 2 3 4 5 6 7
# 2 0 2 0 2 0 1

# 1 2 3 4 5 6 7
# 0 0 2 0 2 0 3

# 1 2 3 4 5 6 7
# 0 0 2 0 2 0 3


### NAIVE SOL

# elfsCount = 6

# elfs = [i + 1 for i in range(elfsCount)]

# print(elfs)
    
# while elfs.__len__() != 1:
#     current = 0
#     if len(elfs) % 2 == 0:
#         while current < len(elfs) - 1:
#             elfs.pop(current + 1)
#             current += 1
#     else:
#         while current < len(elfs) - 1:
#             elfs.pop(current + 1)
#             current += 1
#         elfs = elfs[-1:] + elfs[:-1]
#     print(elfs)
    
elfsCount = 10
cursor = elfsCount // 2 + 3
step = 1
while elfsCount != 1:
    if elfsCount % 2 == 1:
        cursor += step
        pass
    else:
        cursor -= step
        pass
    print(cursor)
    elfsCount //= 2
    step *= 2

'''
1 2 3 4 5 6 7 8 9 10
1   3   5   7   9
1       5       9
        5       9
        5        

1 2 3 4 5 6 7 8 9
1   3   5   7   9
    3       7    
    3            

1 2 3 4 5 6 7 8
1   3   5   7  
1       5      
1             

1 2 3 4 5 6 7
1   3   5   7
    3       7
            7

1 2 3 4 5 6
1   3   5  
1       5  
        5  

1 2 3 4 5
1   3   5
    3   5
    3   

1 2 3 4
1   3  
1     


1 2 3
1   3
    3

'''





























































