for i in range(1, 6):
    for j in range(5 - i):
        print(" ", end="")
    for k in range(5, 5 - i, -1):
        print(k, end="")
    for l in range(5 - i + 2, 6):
        print(l, end="")
    print()
    
    '''
        5
       545
      54345
     5432345
    543212345
    '''
    