for i in range(1,5):
    for j in range(4-i):
        print(" ", end="")
    for k in range(1, i+1):
        print(k, end="")
    for l in range(i-1):
        print(chr(65+l), end="")
    print()
    
    '''
       1
      12A
     123AB
    1234ABC
    '''
    