# import re
# x="[abc]" #either a,b or
# matcher = re.finditer(x, "abt c@5kzabc")
# for match in matcher:
#     print(match.start())
#     print(match.group())

# import  re
# x="[^abc]" #except all other than abc
# matcher = re.finditer(x, "abt c@5kzbc")
# for match in matcher:
#     print(match.start())
#     print(match.group())
#
# import  re    #small letters from a-z
# x="[a-z]" #either a-z
# matcher = re.finditer(x, "abt c@5kzAbc")
# for match in matcher:
#     print(match.start())
#     print(match.group())

# import  re    #small letters from a-z
# x="[A-Z]" #either a-z
# matcher = re.finditer(x, "abt c@5kzAbc")
# for match in matcher:
#     print(match.start())
#     print(match.group())



# import  re
# x="[a-zA-Z]" #either a-z
# matcher = re.finditer(x, "abt c@5kzabcz")
# for match in matcher:
#     print(match.start())
#     print(match.group())
#
# import  re
# x="[0-9]" #either a-z
# matcher = re.finditer(x, "abt9 c@5kzabcz")
# for match in matcher:
#     print(match.start())
#     print(match.group())




# import  re
# x="[^0-9a-zA-Z]" #either a-z
# matcher = re.finditer(x, "abt c@5kzabcz")
# for match in matcher:
#     print(match.start())
#     print(match.group())


# import  re
# x="[\w]"
# matcher = re.finditer(x, "abt c@5kzabcz")
# for match in matcher:
#     print(match.start())
#     print(match.group())

# import  re
# x="[\d]"
# matcher = re.finditer(x, "abt6 c@5kzabcz")
# for match in matcher:
#     print(match.start())
#     print(match.group())

#
# import  re
# x="[\D]"
# matcher = re.finditer(x, "abt c@5kzabcz")
# for match in matcher:
#     print(match.start())
#     print(match.group())




