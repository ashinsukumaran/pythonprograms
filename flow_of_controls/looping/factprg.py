print("factorial program")
num = int(input("enter a number"))
if(num>0):
    fact = 1
    for i in range(1,num+1):
        fact=fact*i
    print(fact)
elif num==0:
    print("factorial of 0 is 1")
else:
    print("factorial for -ve numbers is no exists")






