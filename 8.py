for i in range(5, 0, -1):
    if i == 5:
        for j in range(5):
            print("*", end=" ")
        print()
    elif i == 1:
        print("*")
    else:
        print("*", end="")  
        for j in range(2*i - 3): 
            print(" ", end="")
        print("*") 
        
        '''
        * * * * * 
        *     *
        *   *
        * *
        *
        '''
        