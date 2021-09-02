a=int(input("enter n1"))
b=int(input("enter n2"))
if b>a:
    raise Exception("no2 is greater")
else:
    print(a/b)