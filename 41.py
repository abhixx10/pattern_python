for i in range(1, 8):
    for j in range(1, 8):
        if ((i == 1 or i == 3 or j == 1 or j == 3) or
            (i == 5 or i == 7 or j == 5 or j == 7)):
            print("*", end="")
        else:
            print(" ", end="")
    print()
    
    '''
    *******
    * * * *
    *******
    * * * *
    *******
    * * * *
    *******
    '''
    