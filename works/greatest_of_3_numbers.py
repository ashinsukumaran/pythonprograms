no1=int(input("enter number 1"))
no2=int(input("enter number 2"))
no3=int(input("enter number 3"))
if no1>no2 and no1>no3:
    print("number 1 is greater", no1)
elif no2>no1 and no2>no3:
    print("number 2 is greater",no2)
elif no1==no3==no2:
    print("equal numbers")
else:
    print("number 3 greater",no3)

