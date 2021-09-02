a="hello this is a string"
b=input("enter string")
flag=0
for i in a:
    if i in b:
        flag=1
if flag==1:
    print("present")
else:
    print("not present")