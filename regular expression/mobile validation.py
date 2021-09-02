import re
n="8943693868"
x='\d{10}'
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")
#
#

# import re
# n=input("enter")
# x='[+][9][1]\d{10}$'
# match=re.fullmatch(x,n)
# if match is not None:
#     print("valid")
# else:
#     print("invalid")