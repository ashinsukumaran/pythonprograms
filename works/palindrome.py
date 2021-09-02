a=input("enter the word to check string")
# a="malayalam"
b=a[::-1]
print(b)
if a == b:
    print("it is a palidrome")
else:
    print("not a palindrsome")