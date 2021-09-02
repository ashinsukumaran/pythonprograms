# 1
# 2 3
# 4 5 6
# 7 8 9 10

# def numpatern():
#     print("star program")
#     n = int(input("enter the level of star"))
#     k=1
#     for i in range(n):
#         for j in range(i):
#                 print(k, end=" ")
#                 k=k+1
#         print()
# numpatern()


# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

def numpatern():
    print("star program")
    n = int(input("enter the level of star"))
    k=1
    for i in range(n):
        for j in range(1,i+1):
                print(j, end=" ")

        print()
numpatern()