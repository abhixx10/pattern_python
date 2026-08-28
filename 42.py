for i in range(1, 8):
    for j in range(1, 8):
        if (i == 1 or i == 7 or j == 1 or j == 7) or (3 <= i <= 5 and 3 <= j <= 5):
            print("*", end="")
        else:
            print(" ", end="")
    print()