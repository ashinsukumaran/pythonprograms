import re
f=open("phn",'r')
x = x='[+][9][1]\d{10}$'
for n in f:
    number=n.rstrip("\n")
    match = re.fullmatch(x,number)
    if match!=None:
        print(n)

