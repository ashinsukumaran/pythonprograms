import re
n=input("enter string")
x='[a-zAZ]+[0-9]$'
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")