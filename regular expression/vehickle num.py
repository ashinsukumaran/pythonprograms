import re
n=input("enter")
x='[K][L]\d{2}[a-z]{2}\d{4}$'
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")