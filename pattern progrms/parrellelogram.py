# * * * * * *
# * * * * * *
# * * * * * *
# * * * * * *
# * * * * * *
def parellel(n):
    n=int(input("enter level"))
    # k=1
    for i in range(n):
        for r in range(0,n):
            print(end=" ")
        n=n+1
        for j in range(6):
            print("*",end=" ")
        print()
parellel(8)