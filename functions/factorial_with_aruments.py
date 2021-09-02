print("factorial program with arguments")
def fact(num):
    fact=1
    if num>0:
        for i in range(1,num+1):
         fact=fact*i
        print(fact)
    elif num==0:
        print("factorial of 0 is 1")
    else:
        print("factorial of -ve mumbers doesnot exists")
fact(-1)