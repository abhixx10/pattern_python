for i in range(1, 6):
    for j in range(5 - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        print(6 - i + j, end="")
    print()
    '''
        5
       456
      34567
     2345678
    123456789
    '''
    