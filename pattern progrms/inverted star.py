n=int(input("enter the level of star"))
for i in range(n):
    for j in range(n-i):
        print("*",end=" ")
    print()