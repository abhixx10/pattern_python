for i in range(5):
    for j in range(9):
        if j <= 4 - i or j >= 4 + i:
            print("*", end="")
        else:
            print(" ", end="")
    print()
        
    '''
    *********
    **** ****
    ***   ***
    **     **
    *       *
    '''
        