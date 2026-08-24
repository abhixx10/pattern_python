for i in range(4):
    for j in range(7):
        if j < 4 - i:
            print(chr(65 + j), end="")
        elif j >= 3 + i:
            print(chr(65 + 6 - j), end="")
        else:
            print(" ", end="")
    print()
    
    '''
    ABCDCBA
    ABC CBA
    AB   BA
    A     A 
    '''
    