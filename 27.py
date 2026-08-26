for i in range(1, 6):
    for j in range(5 - i): 
        print(" ", end="")
    for k in range(i): 
        print(i, end="")
    print()
    # lower
for i in range(i-1, 0, -1):
    for j in range(5 - i): 
        print(" ", end="")
    for k in range(i): 
        print(i, end="")
    print()
    
    '''
        1
       22
      333
     4444
    55555
     4444
      333
       22
        1
    '''
    