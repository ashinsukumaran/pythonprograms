# n1=int(input("enter number1"))
# n2=int(input("enter number2"))
# result=n1/n2
# print(result)


# n1=int(input("enter number1"))
# n2=int(input("enter number2"))
# try:
#     result=n1/n2
#     print(result)
# except:
#     print("exception occurred")

n=int(input("enter number"))
lst=[2,3,45]
try:
    print(lst[n])
except:
    print("exception occurred")
finally:
    print("inside finally")





