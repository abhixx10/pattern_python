for i in range(1, 6):
    for j in range(5 - i):
        print(" ", end="")
    if i == 1:
        print("*")
    elif i == 5:
        for k in range(5):
            print("*", end=" ")
        print()
    else:
        print("*", end="")
        for k in range(2*i - 3):
            print(" ", end="")
        print("*")
        
    '''
        *
       * *
      *   *
     *     *
    * * * * * 
    '''
    