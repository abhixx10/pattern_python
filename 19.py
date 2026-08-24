for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()
    #Lower half 
for k in range(4, 0, -1):
    for j in range(k):
        print("*", end="")
    print()
    
    '''
    *
    **
    ***
    ****
    *****
    ****
    ***
    **
    *
    '''
    