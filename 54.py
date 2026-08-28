for i in range(1, 6):
    for j in range(5 - i):
        print(" ", end="")
    k = 64 + (i * (i + 1)) // 2
    for j in range(i):
        print(chr(k), end="")
        k -= 1
    print()
    
    '''
        A
       CB
      FED
     JIHG
    ONMLK
    '''
    