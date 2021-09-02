print("age checker")
age=int(input("enter your age"))
if age<18:
    raise Exception("You are not eligible for vaccination")
else:
    print("eligible")