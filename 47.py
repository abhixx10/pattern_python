for i in range(10):
    for j in range(9 - i):
        print(" ", end="")
    for k in range(i, -1, -1):
        print(k, end="")
    for l in range(1, i + 1):
        print(l, end="")
    print()
for i in range(8, -1, -1):
    for j in range(9 - i):
        print(" ", end="")
    for k in range(i, -1, -1):
        print(k, end="")
    for l in range(1, i + 1):
        print(l, end="")
    print()
    
    '''
             0
            101
           21012
          3210123
         432101234
        54321012345
       6543210123456
      765432101234567
     87654321012345678
    9876543210123456789
     87654321012345678
      765432101234567
       6543210123456
        54321012345
         432101234
          3210123
           21012
            101
             0
    '''
    