for i in range(1, 5):
    for j in range(4 - i):
        print(" ", end="")
    for j in range(i, 0, -1):
        print(j, end="")
    for j in range(2, i + 1):
        print(j, end="")
    print()
    
    '''
       1
      212
     32123
    4321234
    '''
    