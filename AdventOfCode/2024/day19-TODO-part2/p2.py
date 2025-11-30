with open('in', 'r') as f:
    patterns = f.readline().rstrip().split(', ')
    patterns = set(patterns)
    f.readline() # empty line
    desired = list(map(lambda x: x.rstrip(), f.readlines()))

# TODO

def can_be_generated(target, patterns):
    # TODO
    # potentiala idee de rezolvare
    # ia split lui target dupa in doua alte string-uri 
    # la fiecare pozitie unde se poate face split
    # Continua sa faci split pana nu se mai poate.
    # Numarul de moduri in care un substring se poate genera este egal cu numarul in care se pot genera partile stanga respectiv dreapta inmultite
    # exemplu:
    # 
    # r, wr, b, g, bwu, rb, gb, br
    # 
    # rrbgbr can be made 6 different ways:
    # r, r, b, g, b, r
    # r, r, b, g, br
    # r, r, b, gb, r
    # r, rb, g, b, r
    # r, rb, g, br
    # r, rb, gb, r
    # 
    # daca am face split 
    #           rrb gbr
    #       r(1) rb(1 + 1 + 1)   g(1)  br(1 + 1 + 1)
    #         r(1) b(1)     b(1) r(1)
    #
    # NU! Ideea pica pentru ca se pot gasi aceleasi substring-uri de mai multe ori
    # de exemplu split la r-rbgbr vs rr-bgbr rezulta in aproximativ aceleasi substring-uri in partea dreapta
    # aka le numaram de prea multe ori. 
    # 
    # Idee 2
    # Dar ideea se poate mentine ca metoda de generare a tuturor combinatiilor care permit generare target-ului
    # La final toate solutiile sunt puse intr-un set si numarate
    # 
    # Numar prea mare de solutii generate?
    # 
    # 
    # 
    
    solutions=set()
    
    stack=[(target,)]
    
    visited = set()
    
    iter = 0
    
    while stack:
        stack = list(filter(lambda x: x not in visited, stack))
        
        curr = stack.pop()
        
        # if curr in visited:
            # continue
        visited.add(curr)


        if iter == 2:
            print(len(stack), len(visited), len(set(stack)))
            for line in stack:
                print(line)

        iter += 1

        # check if curr is a solution
        solution = True
        for word in curr:
            if word not in patterns:
                solution = False
                break
        if solution:
            solutions.add(curr)
        
        for i in range(len(curr)):
            # split curr[i]
            for j in range(1, len(curr[i])):
                next = list(curr[:i])
                next += [curr[i][:j], curr[i][j:]]
                next += curr[i+1:]
                stack.append(tuple(next))            
        
        stack = list(set(stack))
        
    print(solutions)
    return len(solutions)
     
# print(desired, len(patterns))
# print(patterns)
    
ret = 0
for idx, line in enumerate(desired):
    # print(idx, line)
    r = can_be_generated(line, patterns)
    print(line, f'can be generated in {r} ways')
    ret += r
    
print(ret)