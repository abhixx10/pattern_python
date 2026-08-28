for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    for l in range(2 * (5 - i)):
        print(" ", end="")
    for m in range(i):
        print("*", end="")
    print()
    
    '''
    *        *
    **      **
    ***    ***
    ****  ****
    **********
    '''
    