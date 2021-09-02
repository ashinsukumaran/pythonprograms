a = set()
num=int(input("enter size of set "))
for i in range (num):
    n = int(input("enter numbers"))
    a.add(n)
b = set()
for i in a:
  b.add(i*i)
print("set a is",a)
print("set b is",b)