row = int(input("Enter the value: "))
for i in range(row):
    for j in range(i):
        print(" ", end="")
    for k in range(2 * (row - i) - 1):
        print("*", end="")
    print()
    
    '''
    Enter the value: 5
    *********
     *******
      *****
       ***
        *
    '''
    