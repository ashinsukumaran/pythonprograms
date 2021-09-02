def fib(n):
    if  n<=1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
num=int(input("enter number"))
print("fibanocci series")
for i in range(num):
    print(fib(i))