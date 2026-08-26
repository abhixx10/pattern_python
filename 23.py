for i in range(1, 5):
    for j in range(5 - i):
        print(" ", end="")
    for k in range(i, 2*i):
        print(k, end="")
    for l in range(2*i - 2, i - 1, -1):
        print(l, end="")
    print()
    
    '''
        1
       232
      34543
     4567654
    '''
    