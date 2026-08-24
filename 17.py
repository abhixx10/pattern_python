for i in range(1,5):
    for j in range(i):
        print("*", end=" ")
    print()
    # lower half code
for k in range(i-1, 0,-1):
    for l in range(k):
        print("*", end=" ")
    print()
    
    '''
    * 
    * * 
    * * * 
    * * * * 
    * * * 
    * * 
    *
    '''
    