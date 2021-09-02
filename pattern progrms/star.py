print("star program")
n=int(input("enter the level of star"))
# n=int(input("enter no"))
for i in range(n) :
    for j in range(i+1):
        print("*",end=" ")
    print()
