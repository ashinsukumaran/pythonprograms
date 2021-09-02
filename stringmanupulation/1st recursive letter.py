a=input("enter string")
b=""
for i in a:
    if i not in b:
        b=b+i
    else:
        print("1st recursive charecter is",a,"is",i)
        break
