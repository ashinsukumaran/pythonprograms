def fact(x):
    if x==0:
        return 1
    # elif x==0:
    #     return 1
    else:
        return x * fact(x-1)
num = int(input("enter number"))
print("faxtorial of",num, "is",fact(num))
