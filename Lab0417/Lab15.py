for i in range(1, 11):
    for j in range(10 - i, -1, -1):
        print(" ", end="")
    for j in range(0, i - 1):
        print("*", end="")
    for j in range(0, i):
        print("*", end="")
    print("")