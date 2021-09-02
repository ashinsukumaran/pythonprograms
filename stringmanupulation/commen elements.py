# a="abcd"
# b="acfg"
# a=input("enter word 1")
# b=input("enter word 2")
# for i in a:
#     for j in b:
#         if i==j:
#             print(i)

# one floor loop
a=input("enter word 1")
b=input("enter word 2")
for i in a:
    if i not in b:
        print(i)


