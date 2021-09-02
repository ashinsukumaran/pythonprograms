# vowels="aeiou"
# string=input("enter string")
# count=0
# for i in string:
#     if i in vowels:
#         count=count+1
# print(count)

vowels="aeiou"
string=input("enter string")
for i in string:
    if i not in vowels:
        print(i, end =" ")



