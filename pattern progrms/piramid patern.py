def squarepatern():
    print("star program")
    n = int(input("enter the level of star"))
    # n=int(input("enter no"))
    k=9
    for i in range(n):
        for r in range(n):
            print(end="  ")
            k=k-1
            for j in range(0,i + 1):
             print("*", end=" ")
        print()


squarepatern()