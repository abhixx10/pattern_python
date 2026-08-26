for i in range(1, 6):
    for j in range(5 - i): 
        print(" ", end="")
    num = 1
    for k in range(i): 
        print(num, end="")
        num += 1
    print()
    # lower
for i in range(i-1, 0, -1):
    for j in range(5 - i): 
        print(" ", end="")
    num = 1
    for k in range(i): 
        print(num, end="")
        num += 1
    print()
    
    '''
        1
       12
      123
     1234
    12345
     1234
      123
       12
        1
    '''
    