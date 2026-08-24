for i in range(4):
    for j in range(i):
        print(" ", end="")
    for k in range(7 - 2*i):
        print("*", end="")
    print()
    
    '''
    *******
     *****
      ***
       *
    '''
    