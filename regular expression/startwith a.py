import re
n=input("enter value")
x = '(^[A-Z]{1}[a-zA-Z0-9]*)'
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")
#