for i in range(1, 6):
    for j in range(5 - i):
        print(" ", end="")
    for k in range(i):
        print("*", end=" ")
    print()
#       <lower Half>
for i in range(4, 0, -1):
    for j in range(5 - i):
        print(" ", end="")
    for k in range(i):
        print("*", end=" ")
    print()
    
    '''
        * 
       * * 
      * * * 
     * * * * 
    * * * * * 
     * * * * 
      * * * 
       * * 
        * 
    '''
    
    
