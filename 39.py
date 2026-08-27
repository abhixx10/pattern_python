for i in range(1, 7):
    k = 1
    for j in range(i):
        print(k, end="")
        k = 1 - k
    print()
    
    '''
    1
    10
    101
    1010
    10101
    101010
    '''
    