import re
n=input("enter email")
x='[a-zA-Z0-9]+[@][a-z]+[.][a-z]{2,3}$'
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")