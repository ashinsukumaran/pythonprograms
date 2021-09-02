def add():
    num1=int(input("enter a number 1"))
    num2 = int(input("enter a number 2"))
    sum=num1+num2
    print("sum is ",sum)
def substraction():
    num1 = int(input("enter a number 1"))
    num2 = int(input("enter a number 2"))
    sub = num1 - num2
    print("difference is ",sub)

def multiplicatoin():
    num1 = int(input("enter a number 1"))
    num2 = int(input("enter a number 2"))
    mul = num1 * num2
    print("product is ",mul)

def divisoin():
    num1 = int(input("enter a number 1"))
    num2 = int(input("enter a number 2"))
    div = num1 * num2
    print("division is ",div)


def floor_division():
    num1 = int(input("enter a number 1"))
    num2 = int(input("enter a number 2"))
    div = num1 // num2
    print(" floor division is ", div)

def exponent():
    num1 = int(input("enter a number 1"))
    power = int(input("enter a power"))
    exp = num1 ** power
    print("exponent  is ", exp)


while True:
    print("select operation")
    print("1.Add")
    print("2.substraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Floor Division")
    print("6.Expoent")
    print("7.exit")
    n=int(input("enter selection"))
    if n==1:
        add()
    elif n==2:
        substraction()
    elif n==3:
        multiplicatoin()
    elif n==4:
        divisoin()
    elif n==5:
        floor_division()
    elif n==6:
        exponent()
    else:
        break



