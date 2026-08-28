for i in range(8):
    for j in range(i):
        if j<=2*i-1:
            if j%2==0:
                print("#", end="")
            else:
                print("*", end="")
        else:
            print(" ", end="")
    print()    
    
    '''
    #
    #*
    #*#
    #*#*
    #*#*#
    #*#*#*
    #*#*#*#
    '''
    