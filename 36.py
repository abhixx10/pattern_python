for i in range(1,5):
    for j in range(4-i):
        print(" ", end="")
    for k in range(i):
        print(chr(65+k), end="")
    for l in range(1,i+1):
        print(l, end="")
    print()
    
    '''
       A1
      AB12
     ABC123
    ABCD1234
    '''
    