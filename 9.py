for i in range(1, 6):
    for j in range(5 - i):               
        print(" ", end="")
    num = 1                              
    for k in range(i):                   
        print(num, end=" ")
        num += 1                         
    print()
    
    '''
        1 
       1 2 
      1 2 3 
     1 2 3 4 
    1 2 3 4 5 
    '''
                             