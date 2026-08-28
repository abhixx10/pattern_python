for i in range(1, 5):
    k = 64 + i
    for j in range(i):
        if j <= i:
            print(chr(k), end="")
            k += 1
        else:
            print(" ", end="")
    print()
    
    '''
    A
    BC
    CDE
    DEFG
    '''
    