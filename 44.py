for i in range(1, 8):
    for j in range(7-i):
        print(" ", end="")
    for k in range(2*i-1):
        print("1", end="")
    print()
# lower half
for i in range(6, 0,-1):
    for j in range(7-i):
        print(" ", end="")
    for k in range(2*i-1):
        print("1", end="")
    print()
    
    '''
          1
         111
        11111
       1111111
      111111111
     11111111111
    1111111111111
     11111111111
      111111111
       1111111
        11111
         111
          1
    '''
    