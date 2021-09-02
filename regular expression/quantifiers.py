# quantifires

# x='a+' a including group
# x='a*' count including zero number of a
# x='a?' count a as each including zero no or a
# x='a{2}' 2 no of a position
# x='a{2,3}' minimum 2 a and maximum 3 a
# x='^a' check starting with a
# x='a$' check ending with a







# import re
# x="a+"
# r="aaa abc aaaa cga"
# matcher= re.finditer(x,r)
# for match in matcher:
#     print(match.start())
#     print(match.group())

# import re
# x="a*"
# r="aaa abc aaaa cga"
# matcher= re.finditer(x,r)
# for match in matcher:
#     print(match.start())
#     print(match.group())


# import re
# x="a?"
# r="aaa abc aaaa cga"
# matcher= re.finditer(x,r)
# for match in matcher:
#     print(match.start())
#     print(match.group())

# import re
# x="a{2}"
# r="aaa abc aaaa cga"
# matcher= re.finditer(x,r)
# for match in matcher:
#     print(match.start())
#     print(match.group())


# import re
# x="a{2,3}" #min 2 a and max 3 a
# r="aaa abc aaaa cga"
# matcher= re.finditer(x,r)
# for match in matcher:
#     print(match.start())
#     print(match.group())



# import re
# x="^a" #check starting with a
# r="aaa abc aaaa cga"
# matcher= re.finditer(x,r)
# for match in matcher:
#     print(match.start())
#     print(match.group())

# import re
# x="a$" #check endind with a
# r="aaa abc aaaa cga"
# matcher= re.finditer(x,r)
# for match in matcher:
#     print(match.start())
#     print(match.group())

import re
n="hello"
x='[a-z]+' #\w+
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")


# import re
# n="hello"
# x='[a-z]+'
# match=re.fullmatch(x,n)
# if match is not None:
#     print("valid")
# else:
#     print("invalid")



